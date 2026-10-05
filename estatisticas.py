class Estatisticas:
    def __init__(self):
        self._tamanhos_fila = []

    def registrar_fila(self, tamanho) : self._tamanhos_fila.append(tamanho)

    def calcular(self,clientes,atendentes,tempo_simulado):
        atendidos = []
        aguardando = []
        em_atendimento = []
        tempos_espera = []
        tempos_sistema = []

        for cliente in clientes:
            if cliente.get_tempo_inicio_atendimento() is None : aguardando.append(cliente)
            elif cliente.get_tempo_fim_atendimento() is None : em_atendimento.append(cliente)
            else : atendidos.append(cliente)

            espera = cliente.get_tempo_espera()
            if espera is not None : tempos_espera.append(espera)

            tempo_total = cliente.get_tempo_total_sistema()

            if tempo_total is not None : tempos_sistema.append(tempo_total)

        if len(tempos_espera) > 0:
            espera_media = (sum(tempos_espera) / len(tempos_espera))
            espera_minima = min(tempos_espera)
            espera_maxima = max(tempos_espera)
        else:
            espera_media = 0
            espera_minima = 0
            espera_maxima = 0

        if len(tempos_sistema) > 0 : tempo_medio_sistema = (sum(tempos_sistema) / len(tempos_sistema))
        else : tempo_medio_sistema = 0

        if len(self._tamanhos_fila) > 0:
            fila_media = (sum(self._tamanhos_fila) / len(self._tamanhos_fila))
            fila_maxima = max(self._tamanhos_fila)
        else:
            fila_media = 0
            fila_maxima = 0

        utilizacoes = []

        for atendente in atendentes:
            if tempo_simulado > 0 : utilizacao = (atendente.get_tempo_total_ocupado() / tempo_simulado) * 100
            else : utilizacao = 0

            utilizacoes.append((atendente.get_id(), utilizacao))

        if tempo_simulado > 0 : vazao = (len(atendidos) / tempo_simulado)
        else : vazao = 0

        return {

            "clientes_chegaram":
                len(clientes),

            "clientes_atendidos":
                len(atendidos),

            "clientes_aguardando":
                len(aguardando),

            "clientes_em_atendimento":
                len(em_atendimento),

            "espera_media":
                espera_media,

            "espera_minima":
                espera_minima,

            "espera_maxima":
                espera_maxima,

            "tempo_medio_sistema":
                tempo_medio_sistema,

            "fila_media":
                fila_media,

            "fila_maxima":
                fila_maxima,

            "utilizacao":
                utilizacoes,

            "vazao":
                vazao,

            "tempo_simulado":
                tempo_simulado
        }