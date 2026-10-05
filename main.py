from configuracao import Configuracao
from simulacao import Simulacao
import argparse

def criar_parser():

    parser = argparse.ArgumentParser(
        description="Sistema de Simulação de Atendimento com Filas"
    )

    parser.add_argument(
        "--modo",
        choices=["arquivo", "aleatorio"],
        required=True,
        type=str,
        help="Modo de execução da simulação." \
        "arquivo -> esse modo exige a entrada do caminho de um arquivo" \
        "aleatorio -> esse modo exige proporções de tempo e criação de atendentes"
    )

    parser.add_argument(
        "--entrada",
        type=str,
        help="Caminho de um arquivo csv de geração de clientes." \
        "\n\nO arquivo deve ter as colunas: id, tipo, chegada e duracao" \
        "\n\nid -> identificador do cliente" \
        "\n\ntipo -> tipo de atendimento (comum, prioritario ou tecnico)" \
        "\n\nchegada -> unidade de tempo que o cliente vai chegar" \
        "\n\nduracao -> unidade de tempo que o cliente precisa para ser atendido"
    )

    parser.add_argument(
        "--tempo",
        type=int,
        help="Tempo total da simulação no modo aleatório."
    )

    parser.add_argument(
        "--atendentes",
        type=int,
        required=True,
        help="Quantidade de atendentes para ambos os modos."
    )

    parser.add_argument(
        "--prob-chegada",
        type=float,
        help="Probabilidade de chegada de um cliente no modo aleatório."
    )

    parser.add_argument(
        "--tempo-min",
        type=int,
        help="Tempo mínimo de atendimento no modo aleatório."
    )

    parser.add_argument(
        "--tempo-max",
        type=int,
        help="Tempo máximo de atendimento no modo aleatório."
    )

    parser.add_argument(
        "--prioritarios",
        type=float,
        help="Proporção de clientes prioritários no modo aleatório."
    )

    parser.add_argument(
        "--politica",
        choices=["FIFO", "prioridade"],
        type=str,
        default="FIFO",
        help="Política de atendimento para ambos os modos." \
        "\n\nPode ser escolhido entre FIFO e prioridade" \
        "\n\nFIFO -> clientes comuns, sem prioridade" \
        "\n\nprioridade -> clientes comuns e prioritarios. alterna entre atender um comum e um prioritário"
    )

    parser.add_argument(
        "--seed",
        type=int,
        help="Semente para geração aleatória."
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Mostra os eventos da simulação em ambos os modos."
    )

    return parser

def verificar_argumentos(args, parser):

    if args.modo == "arquivo":

        if args.entrada is None:
            parser.error("--entrada é obrigatório no modo arquivo")

        if args.atendentes is None:
            parser.error("--atendentes é obrigatório")

    elif args.modo == "aleatorio":

        if args.tempo is None:
            parser.error("--tempo é obrigatório no modo aleatorio")

        if args.atendentes is None:
            parser.error("--atendentes é obrigatório")

        if args.prob_chegada is None:
            parser.error("--prob-chegada é obrigatório no modo aleatorio")

        if args.tempo_min is None:
            parser.error("--tempo-min é obrigatório no modo aleatorio")

        if args.tempo_max is None:
            parser.error("--tempo-max é obrigatório no modo aleatorio")

        if args.prioritarios is None:
            parser.error("--prioritarios é obrigatório no modo aleatorio")

        if args.seed is None:
            parser.error("--seed é obrigatório no modo aleatorio")
    
    else:
        parser.error("--modo inválido")


if __name__ == "__main__":

    parser = criar_parser()
    args = parser.parse_args()

    verificar_argumentos(args, parser)

    if args.modo == "aleatorio":
        configuracao = Configuracao(
            modo=args.modo,
            politica=args.politica,
            atendentes=args.atendentes,
            verbose=args.verbose,
            entrada=None,
            tempo=args.tempo,
            prob_chegada=args.prob_chegada,
            tempo_min=args.tempo_min,
            tempo_max=args.tempo_max,
            prioritarios=args.prioritarios,
            seed=args.seed
        )

        simulacao = Simulacao(configuracao)

        simulacao.iniciar_simulacao()
        
    else:
        configuracao = Configuracao(
            modo=args.modo,
            politica=args.politica,
            atendentes=args.atendentes,
            verbose=args.verbose,
            entrada=args.entrada,
            tempo=None,
            prob_chegada=None,
            tempo_min=None,
            tempo_max=None,
            prioritarios=None,
            seed=None
        )

        simulacao = Simulacao(configuracao)

        simulacao.iniciar_simulacao()