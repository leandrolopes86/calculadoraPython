print('### CALCULADORA EM PYTHON ###')
print('Escolha a operação desejada (1/2/3/4/5)')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('5 - Sair do programa')
opcao = int(input('Digite a opção: '))

resultado = 0
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

def soma():
    resultado = num1 + num2
    print(num1, ' + ', num2, ' = ', resultado)

def subtracao():
    resultado = num1 - num2
    print(num1, ' - ', num2, ' = ', resultado)

def multiplicacao():
    resultado = num1 * num2
    print(num1, ' x ', num2, ' = ', resultado)

def divisao():
    resultado = num1 / num2
    print(num1, ' / ', num2, ' = ', resultado)

if opcao == 1:
    soma()
elif opcao == 2:
    subtracao()
elif opcao == 3:
    multiplicacao()
elif opcao == 4:
    divisao()
else:
    print('Opção Invalida.')

