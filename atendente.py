from cliente import Cliente

class Atendente:
    def __init__(self,id,tipos_atendimento,cliente_atual=None,tempo_restante=0,total_clientes_atendidos=0,tempo_total_ocupado=0):
        self.set_id(id)
        self.set_tipos_atendimento(tipos_atendimento)
        self.set_cliente_atual(cliente_atual)
        self.set_tempo_restante(tempo_restante)
        self.set_total_clientes_atendidos(total_clientes_atendidos)
        self.set_tempo_total_ocupado(tempo_total_ocupado)

    # --------- GETTERS E SETTERS -------------

    def get_id(self) : return self._id

    def set_id(self, id) : self._id = id

    def get_tipos_atendimento(self) : return self._tipos_atendimento

    def set_tipos_atendimento(self, tipos_atendimento):
        tipos_validos = ["Comum", "Prioritário", "Técnico"]

        for tipo in tipos_atendimento:
            if tipo not in tipos_validos:
                return 0 

        self._tipos_atendimento = tipos_atendimento

    def get_cliente_atual(self) : return self._cliente_atual

    def set_cliente_atual(self, cliente_atual):
        if cliente_atual is None or isinstance(cliente_atual, Cliente) : self._cliente_atual = cliente_atual
        else : return 0

    def get_tempo_restante(self) : return self._tempo_restante

    def set_tempo_restante(self, tempo_restante):
        if tempo_restante >= 0 : self._tempo_restante = tempo_restante
        else : return 0

    def get_total_clientes_atendidos(self) : return self._total_clientes_atendidos

    def set_total_clientes_atendidos(self, total_clientes_atendidos):
        if total_clientes_atendidos >= 0 : self._total_clientes_atendidos = total_clientes_atendidos
        else : return 0

    def get_tempo_total_ocupado(self) : return self._tempo_total_ocupado

    def set_tempo_total_ocupado(self, tempo_total_ocupado):
        if tempo_total_ocupado >= 0 : self._tempo_total_ocupado = tempo_total_ocupado
        else : return 0

    # ------------------ MÉTODOS ----------------

    def esta_livre(self):
        if self._cliente_atual == None : True
        else : False

    def iniciar_atendimento(self,cliente):
        if self.esta_livre() == False : return 0
        # pegamos a duracao necessaria de atendimento do cliente e colocamos em tempo restante
        tempo_cliente = cliente.get_duracao()
        self.set_tempo_restante(tempo_cliente)
        return 1

    def processar_unidade_tempo(self):
        if self.esta_livre() == True: return 0 # nenhum atendimento está ocorrendo no momento

        self.set_tempo_restante(self.get_tempo_restante() - 1)
        self.set_tempo_total_ocupado(self.get_tempo_total_ocupado() + 1)

    def finalizar_atendimento(self):
        self.set_total_clientes_atendidos(self.get_total_clientes_atendidos() + 1)
        self.set_cliente_atual(None)
        self.set_tempo_restante(0)
