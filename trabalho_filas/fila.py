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
    # Enfileira um novo elemento ao final da fila.
    # O tamanho da fila deve ser incrementado.
        novo_no = FilaNo(elemento)

        if self.vazia() == True:
            self._cabeca = novo_no
            self._cauda = novo_no
        else:
            self._cauda.set_prox(novo_no)
            self._cauda = novo_no

        self._tamanho += 1

    def desinfileira(self):
        # Desinfileira e retorna o dado contido no nó da cabeça. 
        # Se a fila estiver vazia, deve retornar None. O tamanho da fila deve ser decrementado.
        if self.vazia() : return None

        dado = self._cabeca.get_dado()
        self._cabeca = self._cabeca.get_prox()

        self._tamanho -= 1

        if self._cabeca is None : self._cauda = None # se a fila tinha apenas 1 elemento

        return dado

    def cabeca(self): 
        # Retorna o dado contido no nó da cabeça sem desinfileirar. 
        # Se a fila estiver vazia, deve retornar None.
        if self.vazia() == True : return None
        return self._cabeca.get_dado()

    def vazia(self):
        if self._cabeca == None : return True
        else : False

    def tamanho(self) : return self._tamanho
