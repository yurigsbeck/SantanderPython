print("ola mundo!")

#OPERADORES
# variaveis
a = b = c = 10
print(a)

#aritméticos
a = 10
b = 3

soma = a + b   # 13
subtracao = a - b    # 7
multiplicacao = a * b    # 30
divisao = a / b   # 3.333333333
divisao_inteira = a // b   # 3
modulo = a % b   # 1 ( resto de uma divisão )
exponenciacao = a ** b   # 1000 ( potência )

#logicos
#AND (and): devolve True se ambas as condições são verdadeiras.
#OR (or): devolve True se ao menos uma das condições é verdadeira.
#NOT (not): inverte o valor de uma condição, devolve True se a condição é falsa e False se a condição é verdadeira.
a = 10
b = 3

resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False

#estruturas condicionais
#if-elif-else
nota = 85
if nota >= 90:
   print ("Excelente")

elif nota >= 80:
   print ("Muito bom")

elif nota >= 70:
   print ("Bom")

else:
   print ("Precisa melhorar")

#Neste exemplo, são avaliadas múltiplas condições em ordem. Se a variável nota for maior ou igual a 90, será impresso "Excelente". Se não se cumprir a primeira condição, mas nota for maior ou igual a 80, será impresso "Muito bom". Se não se cumprirem as condições anteriores, mas nota for maior ou igual a 70, será impresso "Bom". Se nenhuma das condições anteriores for verdadeira, será executado o bloco else e será impresso "Precisa melhorar".

#LOOPS
#for, adicionat valor d uma variavel em outra
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

for numero in range(5, 10):
   print(numero*3)
#nesse exemplo o range é usado como um repetidor seguindo as informaões dadas no parametro, que dará os numeros de 5 e para ao 10, esses numeros serão copiados pela variavel numero e serão multiplicados por 3

#while, um repetidor
contador = 0
while contador < 5:
    print(contador)
    contador += 1

#CONTROLE DE LOOP
#continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
#verifica-se se o número é divisível por 2. Se o número for divisível por 2 (ou seja, se for par), a instrução continue é executada, como resultado, apenas os números ímpares serão impressos.

#ESTRUTUTA DE DADOS
#lista
#append(elemento): adiciona um elemento ao final da lista.
#insert(indice, elemento): insere um elemento em uma posição específica da lista.
#remove(elemento): remove a primeira ocorrência de um elemento na lista.
#pop(indice): remove e retorna o elemento em uma posição específica da lista.
#sort(): ordena os elementos da lista em ordem ascendente.
#reverse(): inverte a ordem dos elementos na lista.
frutas = ["maçã", "banana", "laranja"]

frutas.append("pera")
print(frutas)  #  ["maçã", "banana", "laranja", "pera"]

frutas.insert(1, "uva")
print(frutas)  #  ["maçã", "uva", "banana", "laranja", "pera"]

frutas.remove("banana")
print(frutas)  #  ["maçã", "uva", "laranja", "pera"]

fruta_removida = frutas.pop(2)
print(frutas)  #  ["maçã", "uva", "pera"]
print(fruta_removida)  #  "laranja"

frutas.sort()
print(frutas)  #  ["maçã", "pera", "uva"]

frutas.reverse()
print(frutas)  #  ["uva", "pera", "maçã"]

#lista de compreensão
números = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in números if x % 2 == 0]
print(quadrados)  #  [4, 16], o x irá copiar a lista de numeros, os pares serão selecionaos e elevaddos a 2