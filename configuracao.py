class Configuracao:
    def __init__(self, modo, atendentes, politica, verbose, entrada=None, tempo=None, prob_chegada=None, tempo_min=None, tempo_max=None, prioritarios=None, seed=None):
        self.set_modo(modo)
        self.set_atendentes(atendentes)
        self.set_politica(politica)
        self.set_verbose(verbose)
        self.set_entrada(entrada)
        self.set_tempo(tempo)
        self.set_prob_chegada(prob_chegada)
        self.set_tempo_min(tempo_min)
        self.set_tempo_max(tempo_max)
        self.set_prioritarios(prioritarios)
        self.set_seed(seed)

    # -------- GETTERS E SETTERS --------

    def get_modo(self) : return self._modo

    def set_modo(self, modo) : self._modo = modo

    def get_atendentes(self) : return self._atendentes

    def set_atendentes(self, atendentes) : self._atendentes = atendentes

    def get_politica(self) : return self._politica

    def set_politica(self, politica) : self._politica = politica

    def get_verbose(self) : return self._verbose

    def set_verbose(self, verbose) : self._verbose = verbose

    def get_entrada(self) : return self._entrada

    def set_entrada(self, entrada) : self._entrada = entrada

    def get_tempo(self) : return self._tempo

    def set_tempo(self, tempo) : self._tempo = tempo

    def get_prob_chegada(self) : return self._prob_chegada

    def set_prob_chegada(self, prob_chegada) : self._prob_chegada = prob_chegada

    def get_tempo_min(self) : return self._tempo_min

    def set_tempo_min(self, tempo_min) : self._tempo_min = tempo_min

    def get_tempo_max(self) : return self._tempo_max

    def set_tempo_max(self, tempo_max) : self._tempo_max = tempo_max

    def get_prioritarios(self) : return self._prioritarios

    def set_prioritarios(self, prioritarios) : self._prioritarios = prioritarios

    def get_seed(self) : return self._seed

    def set_seed(self, seed) : self._seed = seed