# Escreva um script python que use compreensão de listas para criar as seguintes listas:
# Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
# Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
# Todos os números entre 1 e 100 que sejam divisíveis por 7
# Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento (ex: ['par', 'impar',… , 'impar']) 

# lista1=[]
# x=20
# while x <51:
#     lista1.append(x)
#     x+=2
# print (lista1)
# lista_quadrado=[]
# lista2=[]
# y=1
# while y<10:
#     lista2.append(y)
#     y+=1
# for i in lista2:
#     lista_quadrado.append(i**2)

pares_entre_20_e_50 = [x for x in range(20, 51, 2)]
print(pares_entre_20_e_50)

valores = [y for y in range(1, 10)]
quadrados = [y**2 for y in valores]
print(valores)
print(quadrados)

divisiveis_por_7 = [z for z in range(1, 101) if z % 7 == 0]
print(divisiveis_por_7)

par_ou_impar = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]
print(par_ou_impar)