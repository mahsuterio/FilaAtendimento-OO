class Cliente:
    def __init__(self, id_cliente, tipo_cliente, tempo_chegada, duracao):
        self.set_id_cliente(id_cliente)
        self.set_tipo_cliente(tipo_cliente)
        self.set_tempo_chegada(tempo_chegada)
        self.set_duracao(duracao)

        # preenchidos durante a simulação
        self.set_tempo_inicio_atendimento(None)
        self.set_tempo_fim_atendimento(None)

    # -------- GETTERS E SETTERS --------

    def get_id_cliente(self) : return self._id_cliente

    def set_id_cliente(self, id_cliente):
        if id_cliente is None : return 0
        self._id_cliente = id_cliente

    def get_tipo_cliente(self) : return self._tipo_cliente

    def set_tipo_cliente(self, tipo_cliente):
        tipos_validos = ["comum", "prioritario", "tecnico"]
        if tipo_cliente not in tipos_validos : return 0
        self._tipo_cliente = tipo_cliente

    def get_tempo_chegada(self) : return self._tempo_chegada

    def set_tempo_chegada(self, tempo_chegada):
        if tempo_chegada is None : return 0
        if tempo_chegada < 0 : return 0
        self._tempo_chegada = tempo_chegada

    def get_duracao(self) : return self._duracao

    def set_duracao(self, duracao):
        if duracao is None : return 0
        if duracao <= 0 : return 0
        self._duracao = duracao

    def get_tempo_inicio_atendimento(self) : return self._tempo_inicio_atendimento

    def set_tempo_inicio_atendimento(self,tempo_inicio_atendimento):
        if tempo_inicio_atendimento is not None:
            if tempo_inicio_atendimento < 0 : return 0

        self._tempo_inicio_atendimento = tempo_inicio_atendimento

    def get_tempo_fim_atendimento(self) : return self._tempo_fim_atendimento

    def set_tempo_fim_atendimento(self,tempo_fim_atendimento):
        if tempo_fim_atendimento is not None:
            if tempo_fim_atendimento < 0 : return 0

        self._tempo_fim_atendimento = tempo_fim_atendimento
        

    # -------- MÉTODOS --------

    def get_tempo_espera(self):
        if self.get_tempo_inicio_atendimento() is None : return None

        tempo_espera = self.get_tempo_inicio_atendimento() - self.get_tempo_chegada()
        return tempo_espera
    
    def get_tempo_total_sistema(self):
        if self.get_tempo_fim_atendimento() is None : return None

        tempo_total = self.get_tempo_fim_atendimento() - self.get_tempo_chegada()
        return tempo_total