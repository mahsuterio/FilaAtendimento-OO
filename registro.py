class RegistroEventos:
    def __init__(self):
        self._eventos = []

    def registrar(self, tempo, mensagem):
        evento = f"[{tempo:03d}] {mensagem}"
        self._eventos.append(evento)
        print(evento)

    def get_eventos(self) : return self._eventos   