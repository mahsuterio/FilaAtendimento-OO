from gerador import Gerador
from central import CentralAtendimento
from fila import Fila, FilaPrioritaria
from estatisticas import Estatisticas
from registro import RegistroEventos
from relatorio import Relatorio

class Simulacao:
    def __init__(self, configuracao):
        self.set_configuracao(configuracao)

        self._central = None
        self._clientes = []

        self._registro = RegistroEventos()
        self._estatisticas = Estatisticas()
        self._gerador = Gerador()
        self._tempo_simulado = 0

    # -------- GETTERS E SETTERS --------

    def get_configuracao(self) : return self._configuracao

    def set_configuracao(self, configuracao) : self._configuracao = configuracao

    def get_central(self) : return self._central

    def get_clientes(self) : return self._clientes

    # --------- MÉTODOS ----------------
    
    def iniciar_simulacao(self):
        self.criar_central()
        self._registro.registrar(0,"Simulação iniciada")
        

        if self.get_configuracao().get_modo() == "arquivo":
            self._clientes = self._gerador.gerador_cliente(self.get_configuracao().get_entrada())
            self.executar_arquivo()

        else : self.executar_aleatorio()

        resultados = self._estatisticas.calcular(self._clientes,self._central.get_atendentes(),self._tempo_simulado)
        eventos = self._registro.get_eventos()
        Relatorio.exibir(resultados,self.get_configuracao(),eventos)
        Relatorio.salvar(resultados,self.get_configuracao(),eventos)

        return resultados
    
    def criar_central(self):

        atendentes = self._gerador.gerador_atendentes(self.get_configuracao().get_atendentes(), self.get_configuracao().get_politica())
        politica = self.get_configuracao().get_politica().lower()

        if politica == "fifo" : fila = Fila()
        else : fila = FilaPrioritaria()

        self._central = CentralAtendimento(fila,0,[],atendentes)

    def executar_unidade_tempo(self, tempo, novos_clientes):
        self._central.set_tempo_atual(tempo)
        # 1. clientes chegam
        for cliente in novos_clientes:

            self._central.receber_cliente(cliente)

            self._registro.registrar(
                tempo,
                f"Cliente {cliente.get_id_cliente()} chegou"
            )

            self._registro.registrar(
                tempo,
                f"Cliente {cliente.get_id_cliente()} entrou na fila"
            )

        # 2. processa quem já estava sendo atendido
        finalizados = self._central.processar_atendimentos(tempo)

        for atendente, cliente in finalizados:
            self._registro.registrar(
                tempo,
                f"Cliente {cliente.get_id_cliente()} terminou atendimento"
            )

        # 3. distribui clientes para atendentes livres
        iniciados = self._central.distribuir_clientes(tempo)

        for atendente, cliente in iniciados:
            espera = cliente.get_tempo_espera()

            self._registro.registrar(
                tempo,
                f"Atendente {atendente.get_id()} iniciou atendimento "
                f"do Cliente {cliente.get_id_cliente()} "
                f"(esperou {espera} unidades)"
            )

        # 4. registra o tamanho da fila nesse instante
        self._estatisticas.registrar_fila(self._central.get_fila().tamanho())

    def executar_arquivo(self):
        clientes = sorted(self._clientes,key=lambda cliente: cliente.get_tempo_chegada())
        indice = 0
        tempo = 0

        while True:
            novos_clientes = []

            while (indice < len(clientes) and clientes[indice].get_tempo_chegada() == tempo):
                novos_clientes.append(clientes[indice])
                indice += 1

            self.executar_unidade_tempo(tempo,novos_clientes)

            todos_chegaram = (indice == len(clientes))
            fila_vazia = (self._central.get_fila().vazia())
            atendentes_livres = True

            for atendente in self._central.get_atendentes():
                if not atendente.esta_livre():
                    atendentes_livres = False
                    break
            if (todos_chegaram and fila_vazia and atendentes_livres) : break
            tempo += 1

        self._tempo_simulado = tempo

    def executar_aleatorio(self):
        tempo_total = (self.get_configuracao().get_tempo())
        rng = self._gerador.criar_gerador_aleatorio(self.get_configuracao().get_seed())
        proximo_id = 1

        for tempo in range(tempo_total):
            novos_clientes = []
            cliente = self._gerador.gerador_cliente_aleatorio(rng,proximo_id,tempo,self.get_configuracao().get_prob_chegada(),self.get_configuracao().get_tempo_min(),self.get_configuracao().get_tempo_max(),self.get_configuracao().get_prioritarios())

            if cliente is not None:
                novos_clientes.append(cliente)
                self._clientes.append(cliente)
                proximo_id += 1

            self.executar_unidade_tempo(tempo,novos_clientes)
        self._tempo_simulado = tempo_total