class Processo:
    esta_bloqueado = False
    tempo_bloqueio = 0
    def __init__(self, tamanho, nome,instrucoes):
        self.tamanho = tamanho 
        self.nome = nome
        self.instrucoes = instrucoes

    def _print_processo(self,):
        print("Nome: " + self.nome)

        print("Tamanho:" + self.tamanho) 
        
        print("Instrucoes: ")
        print(self.instrucoes)
