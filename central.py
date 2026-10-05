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

    def set_atendentes(self, atendentes):
        if atendentes is None : self._atendentes = []
        elif isinstance(atendentes, list):
            for atendente in atendentes:
                if not isinstance(atendente, Atendente) : return 0

            self._atendentes = atendentes

        else : return 0

    def get_clientes_atendidos(self) : return self._clientes_atendidos

    def set_clientes_atendidos(self, clientes_atendidos):
        if clientes_atendidos is None : self._clientes_atendidos = []

        elif isinstance(clientes_atendidos, list):
            for cliente in clientes_atendidos:
                if not isinstance(cliente, Cliente) : return 0

            self._clientes_atendidos = clientes_atendidos

        else : return 0

    def get_tempo_atual(self) : return self._tempo_atual

    def set_tempo_atual(self,tempo_atual):
        if tempo_atual < 0 : return 0
        else : self._tempo_atual = tempo_atual

    # ------------------ MÉTODOS ----------------

    def receber_cliente(self, cliente):
        if cliente is None or not isinstance(cliente, Cliente) : return 0
        self.get_fila().enfileira(cliente)

    def distribuir_clientes(self, tempo_atual):
        iniciados = []

        for atendente in self.get_atendentes():
            if self.get_fila().vazia() : break
            if atendente.esta_livre():
                cliente = self.get_fila().desinfileira()
                cliente.set_tempo_inicio_atendimento(tempo_atual)

                atendente.iniciar_atendimento(cliente)
                iniciados.append((atendente, cliente))

        return iniciados

    def processar_atendimentos(self, tempo_atual):
        finalizados = []

        for atendente in self.get_atendentes():
            # se não tem cliente, não há nada para processar
            if atendente.esta_livre() : continue

            cliente = atendente.get_cliente_atual()
            atendente.processar_unidade_tempo()

            if atendente.get_tempo_restante() == 0:
                cliente.set_tempo_fim_atendimento(tempo_atual)
                atendente.finalizar_atendimento()
                self._clientes_atendidos.append(cliente)
                finalizados.append((atendente, cliente))

        return finalizados