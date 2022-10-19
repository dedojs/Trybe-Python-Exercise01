#Faça um programa que solicite o nome de uma pessoa usuária e imprimaó na vertical
'''
from venv import create


name = input('Digite seu nome:')
for letter in name:
    print(letter.upper())


# Exercício 2: Escreva um programa que receba vários números naturais e calcule a soma desses valores. Caso algum valor da entrada seja inválido (por exemplo uma letra), uma mensagem deve ser exibida na saída de erros no seguinte formato: “Erro ao somar valores, {valor} é um valor inválido”. Ao final, você deve imprimir a soma dos valores válidos.


nums = input("Digite números naturais:")
numsArr = nums.split(' ')

sum = 0
for n in numsArr:
    if (n.isdigit()):
        l = int(n)
        sum += l
    else:
        print(f"O elemento {n} não é um número!")

print(f"A soma total dos valores válidos é {sum}")
'''
#Exercício 3: Dado um arquivo contendo estudantes e suas respectivas notas, escreva um programa que:
'''
lê todas essas informações;
aplique um filtro, mantendo somente as pessoas que estão reprovadas;
escreva seus nomes em outro arquivo.
Considere que a nota miníma para aprovação é 6.
'''

def read_notes_students(source):
    with open(source, 'r') as file:
        content = file.read()
    new_content = content.split('\n')
    with open('reprovados.txt', 'w') as file:
        for aluno in new_content:
            notas = aluno.split(' ')
            if (int(notas[1]) < 6):
                reprovados = notas
                file.write(f"{reprovados[0]} \n") 
          


read_notes_students('exercicio3.txt')



