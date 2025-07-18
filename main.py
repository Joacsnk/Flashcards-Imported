from os import system as sy
from time import sleep as sl
import pyperclip as pc
class main():
    
    def __init__(self):
        self.numero_interrupcao_str = self.flashcard_import = ""
        sy('cls')
        sl(1)
    
    def inicio(self, recomecar=int):
        if recomecar == 0:
            self.senha()
            self.verificacao_senha()
        else:
            self.flashcard_import = ""
        self.flashcards()
        self.importacao()
    
    def senha(self):
        print("Antes de iniciar, é necessário definir um número de interrupção do programa.")
        print("O número de interrupção é um número escolhido para interromper o funcionamento e receber o conjunto. \nEscolha entre 0 e 9")
        self.numero_interrupcao_int = int(input("Defina seu número de interrupção aqui: "))
    
    def verificacao_senha(self):
        sy('cls')
        sl(1)
        if self.numero_interrupcao_int < 10 and self.numero_interrupcao_int > -1:
            print("Número válido")
            self.numero_interrupcao_str += str(self.numero_interrupcao_int)
            sl(1)
            sy('cls')
        else:
            print("Número inválido. Tente novamente")
            sl(1)
            sy("cls")
            sl(1)
            self.inicio(0)
    
    def flashcards(self):
        i = int(1)
        while True:
            palavra = str(input(f"Digite a palavra do flashcard número {i}º:\n\n"))
            sy("cls")
            sl(0.5)
            explicacao = str(input(f"Digite a explicacao do flashcard número {i}º:\n\n"))
            sy("cls")
            sl(0.5)
            if palavra == self.numero_interrupcao_str and explicacao == self.numero_interrupcao_str:
                break
            else:
                i += 1
                self.flashcard_import += palavra
                self.flashcard_import += ','
                self.flashcard_import += explicacao
                self.flashcard_import += ';'

    def importacao(self):
        while True:
            sy('cls')
            sl(1)
            print(f"Conjunto criado com sucesso! Aqui está abaixo:\n\n{self.flashcard_import}\n\n")
            print("1 - Copiar conteúdo")
            print("2 - Criar um flashcard novamente")
            print("3 - Sair")
            match str(input("Escolha a opção acima: ")):
                case '1':
                    sy("cls")
                    sl(0.5)
                    pc.copy(self.flashcard_import)
                    print("Conteúdo copiado com sucesso")
                    sl(0.5)                
                case '2':
                    sy('cls')
                    self.inicio(1)
                case '3':
                    sy('cls')
                    exit()
                case _:
                    sy("cls")
                    sl(0.5)
                    print("Opção inválida")
                    sl(0.5)
                  
                
if __name__ == "__main__":
    main().inicio(0)
