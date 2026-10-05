# gerar clientes e atendentes
from cliente import Cliente
from atendente import Atendente
import pandas as pd
import random

class Gerador:
    @staticmethod
    def criar_gerador_aleatorio(seed) : return random.Random(seed)

    @staticmethod
    def gerador_cliente_aleatorio(rng,id_cliente,tempo_atual,prob_chegada,tempo_min,tempo_max,proporcao_prioritarios):
        sorteio_chegada = rng.random()

        if sorteio_chegada >= prob_chegada : return None
        sorteio_tipo = rng.random()

        if sorteio_tipo < proporcao_prioritarios : tipo = "prioritario"
        else : tipo = "comum"

        duracao = rng.randint(tempo_min,tempo_max)
        cliente = Cliente(id_cliente,tipo,tempo_atual,duracao)

        return cliente
    
    @staticmethod
    def gerador_cliente(entrada):
        df = pd.read_csv(entrada)
        clientes = []

        for _, linha in df.iterrows():

            cliente = Cliente(
                linha["id"],
                linha["tipo"],
                linha["chegada"],
                linha["duracao"]
            )

            clientes.append(cliente)
        
        return clientes
    
    @staticmethod
    def gerador_atendentes(quantidade_atendentes,tipo_atendimento):
        atendentes=[]
        for i in range(quantidade_atendentes):
            if tipo_atendimento == 'FIFO':
                atendente = Atendente((i+1),["Comum","Técnico"])
                atendentes.append(atendente)
            else:
                atendente = Atendente((i+1),["Comum","Técnico","Prioritário"])
                atendentes.append(atendente)

        return atendentes