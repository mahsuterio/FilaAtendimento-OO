class FilaNo:
    def __init__(self,dado,prox=None):
        self.set_dado(dado)
        self.set_prox(prox)

    def get_dado(self) : return self._dado

    def set_dado(self,dado):
        if dado == None:
            return 0
        self._dado = dado

    def get_prox(self) : return self._prox

    def set_prox(self,prox) : self._prox = prox

class Fila:
    def __init__(self):
        self._cabeca = None
        self._cauda = None
        self._tamanho = 0

    def enfileira(self, elemento):
    # enfileira um novo elemento ao final da fila.
    # o tamanho da fila deve ser incrementado.
        novo_no = FilaNo(elemento)

        if self.vazia() == True:
            self._cabeca = novo_no
            self._cauda = novo_no
        else:
            self._cauda.set_prox(novo_no)
            self._cauda = novo_no

        self._tamanho += 1

    def desinfileira(self):
        # desinfileira e retorna o dado contido no nó da cabeça. 
        # de a fila estiver vazia, deve retornar None. O tamanho da fila deve ser decrementado.
        if self.vazia() : return None

        dado = self._cabeca.get_dado()
        self._cabeca = self._cabeca.get_prox()

        self._tamanho -= 1

        if self._cabeca is None : self._cauda = None # se a fila tinha apenas 1 elemento

        return dado

    def cabeca(self): 
        # retorna o dado contido no nó da cabeça sem desinfileirar. 
        # se a fila estiver vazia, deve retornar None.
        if self.vazia() == True : return None
        return self._cabeca.get_dado()

    def vazia(self):
        if self._cabeca == None : return True
        else : False

    def tamanho(self) : return self._tamanho

class FilaPrioritaria(Fila):
    def __init__(self):
        super().__init__()

        self._fila_comum = Fila()
        self._fila_prioritaria = Fila()

        self._ultimo_tipo = None

    # ----------- MÉTODOS -------------

    def enfileira(self, cliente):
        tipo = cliente.get_tipo_cliente()

        if tipo == "comum" : self._fila_comum.enfileira(cliente)

        elif tipo == "prioritario" : self._fila_prioritaria.enfileira(cliente)

    def desinfileira(self):
        if self.vazia() : return None

        # tenta alternar depois de um comum
        if self._ultimo_tipo == "comum":
            if not self._fila_prioritaria.vazia():
                cliente = self._fila_prioritaria.desinfileira()
                self._ultimo_tipo = "prioritario"
                return cliente

        # tenta alternar depois de um prioritário
        elif self._ultimo_tipo == "prioritario":
            if not self._fila_comum.vazia():
                cliente = self._fila_comum.desinfileira()
                self._ultimo_tipo = "comum"
                return cliente

        # início ou quando não é possível alternar
        if not self._fila_prioritaria.vazia():
            cliente = self._fila_prioritaria.desinfileira()
            self._ultimo_tipo = "prioritario"
            return cliente

        if not self._fila_comum.vazia():
            cliente = self._fila_comum.desinfileira()
            self._ultimo_tipo = "comum"
            return cliente

    def vazia(self) : return (self._fila_comum.vazia() and self._fila_prioritaria.vazia())

    def tamanho(self) : return (self._fila_comum.tamanho() + self._fila_prioritaria.tamanho())

    def cabeca(self):
        if self.vazia() : return None

        if self._ultimo_tipo == "comum":
            if not self._fila_prioritaria.vazia() : return self._fila_prioritaria.cabeca()

        elif self._ultimo_tipo == "prioritario":
            if not self._fila_comum.vazia() : return self._fila_comum.cabeca()

        if not self._fila_prioritaria.vazia() : return self._fila_prioritaria.cabeca()
        return self._fila_comum.cabeca()