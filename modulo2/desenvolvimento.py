#FUNÇÕES
#funções anonimas ou lambda, são funções sem nome definidas em uma única linha. São comumente usadas para funções pequenas e concisas.

quadrado = lambda x: x ** 2
print(quadrado(5))  #  25

#funções comm numeros variaveis de argumentos

def soma_variavel(*numeros):
    total = 0 #começamos com total igual a zero para acumular a soma.
    for numero in numeros:
        total += numero #operador += é um operador de atribuição composta em Python. Ele é usado para somar um valor a uma variável e armazenar o resultado na própria variável.
    return total


print(soma_variavel(1, 2, 3))  #  6
print(soma_variavel(4, 5, 6, 7))  #  22

#MANEJO DE EXCEÇÕES, lidar com erros
# - try,Se ocorrer uma exceção dentro do bloco try, o fluxo de execução é transferido para o bloco except correspondente.
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")

# - expept, O bloco except especifica o tipo de exceção que se deseja capturar e lidar. Você pode ter múltiplos blocos except para lidar com diferentes tipos de exceções.
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")
 
 # - finally,é opcional e é executado sempre, independentemente de ter ocorrido uma exceção ou não. É comumente utilizado para realizar tarefas de limpeza ou liberação de recursos.

try:
    # Código que pode gerar uma exceção
    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção

"""
Imagine que você está cozinhando:
try: Você começa a cozinhar, mas não sabe se algo pode dar errado (como queimar a comida). Então, você coloca essa parte "incerta" no try. É como se fosse um "teste", onde você tenta fazer algo que pode dar errado.

except: Se algo der errado no que você tentou fazer (como queimar a comida), você tem um plano de emergência. O except é onde você define o que fazer caso algum erro aconteça enquanto você está tentando cozinhar. É como se fosse um "plano B" para lidar com o problema.

finally: Mesmo que tudo tenha dado certo ou errado, no final, você sempre vai fazer algo, como limpar a cozinha ou guardar os utensílios. O finally é a parte onde você garante que alguma coisa sempre vai acontecer, não importa o que.
"""
try:
    # Tentando fazer algo arriscado, como dividir um número por zero
    resultado = 10 / 0
except ZeroDivisionError:
    # Se houver um erro (como divisão por zero), tratamos aqui
    print("Erro: Não é possível dividir por zero!")
finally:
    # Independente do que aconteceu, eu vou sempre fazer isso
    print("Finalizando o processo.")

#try: Tenta fazer algo que pode dar erro.
#except: Se der erro, lida com ele.
#finally: Sempre faz algo no final, não importa se deu erro ou não.

#EXEÇÕES PERSONALIZADAS, Para criar uma exceção personalizada, você deve criar uma classe que herde da classe base Exception ou de uma de suas subclasses.
def funcao():
    # Código que pode gerar uma exceção personalizada
    if condicao:
        raise Exception("Descrição do erro") #Você pode criar um erro manualmente quando algo inesperado acontece no seu código. Para isso, usamos o comando raise para lançar o erro.
try:
    funcao()
except Exception as e: #as é usado para capturar a exceção e armazená-la em uma variável, para que você possa acessar as informações sobre o erro.
    print(f"Erro: {str(e)}")

"""
O que está acontecendo aqui:
A função funcao() pode gerar um erro.
O try tenta rodar a função. Se algo der errado, o Python vai "pegar" o erro e parar a execução.
O except pega o erro gerado e faz algo com ele, como mostrar uma mensagem, por exemplo.
Resumo:
raise: Você pode gerar um erro manualmente.
try-except: Você tenta rodar um código e, se der errado, pega o erro e faz algo com ele (como mostrar uma mensagem ou tentar outra coisa).
"""

#saida e entrada de dados, input e print
nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")
print("Olá, " + nome + "!")
print("Você tem " + idade + " anos.")
#A função input() sempre retorna uma cadeia de texto. Se você deseja trabalhar com outros tipos de dados, como números inteiros ou flutuantes, deve realizar uma conversão explícita utilizando funções como int() ou float().
idade = int(input("Insira sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#leitura e escrita de arquivos, Podemos abrir arquivos em diferentes modos, como leitura ("r"), escrita ("w") ou anexar ("a"), e realizar operações de leitura e escrita.

#leitura
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
#o arquivo "dados.txt" é aberto utilizando open(). Depois, o conteúdo é lido utilizando o método read() e armazenado na variável. Finalmente, o conteúdo é mostrado na tela e o arquivo é fechado utilizando o método close().

#escrita
arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()
#o arquivo "dados.txt" é aberto utilizando open(). Depois, a string "Olá, mundo!" é escrita utilizando o método write(). Finalmente, o arquivo é fechado utilizando o método close().
 
#importação e criação de modulos, um módulo é um arquivo que contém definições de funções, classes e variáveis que podem ser utilizadas em outros programas. A importação de módulos nos permite acessar a funcionalidade definida em outros arquivos e reutilizar código de maneira eficiente. Além disso, podemos criar nossos próprios módulos para organizar e modularizar nosso código.

#importar
import math
resultado = math.sqrt(25)
print(resultado)  #  5.0
#importar funções específicas de um módulo utilizando a sintaxe from módulo import função.
from math import sqrt
resultado = sqrt(25)
print(resultado)  #  5.0


""""
random - Oferece funções para gerar números aleatórios, como random() (número aleatório entre 0 e 1), randint() (número inteiro aleatório em um intervalo), entre outras.
datetime -Permite trabalhar com datas e horas, como datetime.now() (data e hora atual), datetime.date() (data), datetime.time() (hora), entre outras.
"""
import random
import datetime
numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  #  um número inteiro aleatório entre 1 e 10
data_atual = datetime.datetime.now()
print(data_atual)  #  a data e hora atual

#CRIAÇÃO DE MODULOS, simplesmente criamos um novo arquivo Python com o nome desejado e definimos as funções, classes e variáveis que queremos incluir no módulo. Por exemplo, criamos um arquivo (no mesmo diretório onde estamos executando Python) chamado meu_modulo.py com o seguinte conteúdo:
#meu_modulo.py
def saudar(nome):
    print(f"Olá, {nome}!")
def calcular_soma(a, b):
    return a + b
#Depois, podemos importar e utilizar as funções definidas em meu_modulo.py em outro arquivo Python.
import meu_modulo
meu_modulo.saudar("João")  #  "Olá, João!"
resultado = meu_modulo.calcular_soma(5, 3)
print(resultado)  #  8

#CRIAR E UTILIZAR PACOTES
#Um pacote é uma forma de organizar módulos relacionados em uma estrutura hierárquica de diretórios. Os pacotes nos permitem agrupar módulos relacionados e evitar conflitos de nomes entre módulos.

"""
Para criar um pacote, criamos um diretório com o nome desejado e adicionamos um arquivo especial chamado __init__.py dentro do diretório. Este arquivo pode estar vazio ou conter código de inicialização do pacote.

meu_pacote/
    __init__.py
    modulo1.py
    modulo2.py

Depois, podemos importar e utilizar os módulos do pacote em nosso programa.

from meu_pacote import modulo1, modulo2


modulo1.funcao1()
modulo2.funcao2(
"""
