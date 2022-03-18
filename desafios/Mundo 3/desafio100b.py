# desafio100, mas melhorado e o usuário pode escolher quantos números e o alcance.
from random import randint
from time import sleep
numbers = list()
def sorteia():
	user_n = int(input('  Quantos números deseja sortear? '))
	while user_n < 1:
		print('   \033[31mErro!\033[m Não pode ser menor que 1.')
		user_n = int(input('  Quantos números deseja sortear? '))

	user_a = int(input('  Qual é o número mínimo? '))

	user_b = int(input('  Qual é o número máximo? '))
	while user_b <= user_a:
		print(f'   \033[31mErro!\033[m Não pode ser menor que {user_a}.')
		user_b = int(input('  Quantos números deseja sortear? '))

	print('-' * 20, f'\nSorteando {user_n} números de {user_a} a {user_b}...')
	for e in range(0,user_n):
		s = randint(user_a,user_b)
		numbers.append(s)

	for n in numbers:
		print(f'{n}', end=' ', flush=True)
		if len(numbers) <= 20:
			sleep(0.2)
		elif len(numbers) <= 80 and len(numbers) > 30:
			sleep(0.1)
		else:
			sleep(0.05)
	print()


def somaPar():
	sumeven = 0
	for p in numbers:
		if p % 2 == 0:
			sumeven += p
	print('-' * 20)
	print(f'A soma dos números pares é:', f'\n{sumeven}')
	sleep(1)
	print('~' * 40)
	numbers.clear()


print('~' * 40)
sorteia()
somaPar()
while True:
	user = str(input(' Deseja continuar?\033[40m[S/N]\033[m ')).strip().upper()
	while user != 'S' and user != 'N':
		print('   \033[31mErro!\033[m Tente novamente.')
		user = str(input(' Deseja continuar?\033[40m[S/N]\033[m ')).strip().upper()
	if user == 'N':
		break
	elif user == 'S':
		sorteia()
		somaPar()

print('Encerrando... ')
sleep(1)