# Este arquivo demonstra as operações básicas em python.

#---------------------------
# 1. Operações Aritiméticas
#---------------------------
print("--- Operações Artiméticas ---")
a = 10
b = 3

soma = a + b                #Soma
subtracao = a - b           #Subtração
multiplicacao = a * b       #Multiplicação
divicao = a / b             #Divisão (Sempre retorna um numero com ponto flutuante, ex:2.0)
divicao_inteiro = a // b    #Divisão inteira (Discarta a parte decimal) 
resto = a % b               #Resto da divisão (Módolo)
pontencia = a ** b          #Potencia(ex:a elevado a b)


print(f"{a} + {b} = {soma}")
print(f"{a} - {b} = {subtracao}")
print(f"{a} * {b} = {multiplicacao}")
print(f"{a} / {b} = {divicao}")
print(f"{a} // {b} = {divicao_inteiro}")
print(f"{a} % {b} = {resto}")
print(f"{a} ** {b} = {pontencia}")
