# implementar mais verificações ? (raise value error etc)

class Cliente:
   def __init__(self, id_cliente, tipo_cliente, tempo_chegada):
      self.id_cliente = id_cliente
      self.tipo_cliente = tipo_cliente
      self.tempo_chegada = tempo_chegada

    # O preenchimento ocorre dinamicamente durante a simulação:
      self.tempo_inicio_atendimento = None
      self.tempo_fim_atendimento = None

    def get_tempo_espera(self):
      if self.tempo_inicio_atendimento is not None:
         return self.tempo_inicio_atendimento - self.tempo_chegada
      return 0.0 #retorna zero se ainda não iniciou o atendimento

   def get_tempo_total_sitema(self):
      if self.tempo_fim_atendimento is not None:
         return self.tempo_fim_atendimento - self.tempo_chegada
      return 0.0 #retorna zero se ainda não finalizou o atendimento