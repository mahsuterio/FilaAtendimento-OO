import os
class Relatorio:

    @staticmethod
    def montar_texto(resultados, configuracao, eventos):
        texto = ""
        texto += "\n--- CONFIGURAÇÕES ---\n"

        texto += f"\nModo: {configuracao.get_modo()}\n"
        texto += f"Atendentes: {configuracao.get_atendentes()}\n"
        texto += f"Política: {configuracao.get_politica()}\n"

        if configuracao.get_modo() == "arquivo":

            texto += f"Entrada: {configuracao.get_entrada()}\n"

        else:

            texto += f"Tempo: {configuracao.get_tempo()}\n"
            texto += (
                f"Probabilidade de chegada: "
                f"{configuracao.get_prob_chegada()}\n"
            )
            texto += (
                f"Tempo mínimo: "
                f"{configuracao.get_tempo_min()}\n"
            )
            texto += (
                f"Tempo máximo: "
                f"{configuracao.get_tempo_max()}\n"
            )
            texto += (
                f"Prioritários: "
                f"{configuracao.get_prioritarios()}\n"
            )
            texto += f"Seed: {configuracao.get_seed()}\n"

        texto += "\n--- EVENTOS DA SIMULAÇÃO ---\n\n"

        for evento in eventos:
            texto += evento + "\n"

        texto += "\n--- RESULTADOS DA SIMULAÇÃO ---\n\n"

        texto += f"Tempo simulado: {resultados['tempo_simulado']}\n"
        texto += f"Clientes que chegaram: {resultados['clientes_chegaram']}\n"
        texto += f"Clientes atendidos: {resultados['clientes_atendidos']}\n"
        texto += f"Clientes aguardando: {resultados['clientes_aguardando']}\n"
        texto += f"Clientes em atendimento: {resultados['clientes_em_atendimento']}\n"

        texto += f"Espera média: {resultados['espera_media']:.2f}\n"
        texto += f"Espera mínima: {resultados['espera_minima']}\n"
        texto += f"Espera máxima: {resultados['espera_maxima']}\n"

        texto += (
            f"Tempo médio no sistema: "
            f"{resultados['tempo_medio_sistema']:.2f}\n"
        )

        texto += (
            f"Tamanho médio da fila: "
            f"{resultados['fila_media']:.2f}\n"
        )

        texto += (
            f"Tamanho máximo da fila: "
            f"{resultados['fila_maxima']}\n"
        )

        texto += "\nUtilização dos atendentes:\n"

        for id_atendente, utilizacao in resultados["utilizacao"]:

            texto += (
                f"Atendente {id_atendente}: "
                f"{utilizacao:.2f}%\n"
            )

        texto += (
            f"\nVazão: "
            f"{resultados['vazao']:.2f} "
            f"clientes/unidade de tempo\n"
        )

        return texto

    @staticmethod
    def exibir(resultados, configuracao, eventos):
        print(Relatorio.montar_texto(resultados,configuracao,eventos))

    @staticmethod
    def salvar(resultados, configuracao, eventos):
        os.makedirs(
            "relatorios",
            exist_ok=True
        )

        politica = configuracao.get_politica()
        atendentes = configuracao.get_atendentes()

        if configuracao.get_modo() == "arquivo":

            entrada = configuracao.get_entrada()

            nome_entrada = os.path.basename(
                entrada
            )

            nome_entrada = os.path.splitext(
                nome_entrada
            )[0]

            nome_relatorio = (
                f"{nome_entrada}_"
                f"{politica}_"
                f"{atendentes}.txt"
            )

        else:

            seed = configuracao.get_seed()
            tempo = configuracao.get_tempo()

            nome_relatorio = (
                f"{politica}_"
                f"{seed}_"
                f"{tempo}_"
                f"{atendentes}.txt"
            )


        caminho = os.path.join(
            "relatorios",
            nome_relatorio
        )

        texto = Relatorio.montar_texto(resultados,configuracao,eventos)

        with open(
            caminho,
            "w",
            encoding="utf-8"
        ) as arquivo:

            arquivo.write(texto)

        return caminho