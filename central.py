from fila import Fila
from atendente import Atendente
from cliente import Cliente

class CentralAtendimento: 
    def __init__(self,fila,tempo_atual,clientes_atendidos=[],atendentes=[]):
        self.set_fila(fila)
        self.set_atendentes(atendentes)
        self.set_clientes_atendidos(clientes_atendidos)
        self.set_tempo_atual(tempo_atual)

    # --------- GETTERS E SETTERS -------------

    def get_fila(self) : return self._fila
        
    def set_fila(self, fila):
        if fila is None or isinstance(fila, Fila) : self._fila = fila
        else : return 0

    def get_atendentes(self) : return self._atendentes

    def set_atendentes(self,atendentes):
        if atendentes is None or isinstance(atendentes, Atendente) : self._atendentes = atendentes
        else : return 0

    def get_clientes_atendidos(self) : return self._clientes_atendidos

    def set_clientes_atendidos(self,clientes_atendidos):
        if clientes_atendidos is None or isinstance(clientes_atendidos, Cliente) : self._clientes_atendidos = clientes_atendidos
        else : return 0

    def get_tempo_atual(self) : return self._tempo_atual

    def set_tempo_atual(self,tempo_atual):
        if tempo_atual < 0 : return 0
        else : self._tempo_atual = tempo_atual

    # ------------------ MÉTODOS ----------------

    def receber_cliente(self, cliente):
        if cliente is None or not isinstance(cliente, Cliente) : return 0
            
        self.get_fila().enfileira(cliente)

    def distribuir_clientes(self):
        # FAZER: antes de direcionar o cliente, verificar o tipo de atendimento 
        # que o atendente aceita com o tipo de atendimento do cliente
        
        if self.get_fila().vazia() == True : return 0 # fila vazia, nada ocorre

        for atendente in self.get_atendentes():
            if atendente.esta_livre() == False : conta+=1

        if conta == len(self.get_atendentes()) : return 0 # se todos os atendentes estiverem ocupados, nada ocorre

        cliente = self.get_fila().desinfileira()
        self.get_atendentes().iniciar_atendimento(cliente)

    def processar_atendimentos(self):
        for atendente in self.get_atendentes():
            atendente.processar_unidade_tempo()

            if atendente.get_tempo_restante() == 0:
                self.set_clientes_atendidos(atendente.get_cliente_atual())
                atendente.finalizar_atendimento()

    def executar_simulacao(self):
        pass

    def calcular_metricas(self):
        '''
        A Central terá informações como:

        clientes que chegaram
        clientes atendidos
        clientes que ficaram esperando
        tempo de espera
        tempo total no sistema
        tamanho das filas
        tempo ocupado dos atendentes

        E daí calcula:

        média de espera;
        espera mínima;
        espera máxima;
        tamanho médio da fila;
        tamanho máximo da fila;
        utilização dos atendentes;
        throughput etc.
        '''