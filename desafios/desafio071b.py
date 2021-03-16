from time import sleep
st = '==-==-==-==-==-==-==-==-==-=='
cc = '\033[36m'  #cyan
cn = '\033[m'    #normal
cr = '\033[31m'  #red
cb = '\033[34m'  #blue
print(f'{st}\n{cc}{"Cash Machine Ants Harpoon":^29}{cn}\n{st}')

m = str(input('How much do you want to withdraw? '))
while m.isalpha() or m.isspace():
    print(f'{cr}Invalid value! Try again!{cn}')
    m = str(input('How much do you want to withdraw? '))  #Test with 186

if int(m) // 100 >= 1:
    print(f'The number of bills of 100 dollars is: {int(m) // 100:.0f}')

if (int(m) % 100) // 50 >= 1:
    print(f'The number of bills of 50 dollars is: {(int(m) % 100) // 50:.0f}')

if ((int(m) % 100) % 50) // 20 >= 1:
    print(f'The number of bills of 20 dollars is: {((int(m) % 100) % 50) // 20:.0f}')

if (((int(m) % 100) % 50) % 20) // 10 >= 1:
    print(f'The number of bills of 10 dollars is: {(((int(m) % 100) % 50) % 20) // 10:.0f}')

if ((((int(m) % 100) % 50) % 20) % 10) // 5 >= 1:
    print(f'The number of bills of 5 dollars is: {((((int(m) % 100) % 50) % 20) % 10) // 5:.0f}')

if ((((int(m) % 100) % 50) % 20) % 10) % 5 >= 1:
    print(f'The number of bills of 1 dollar is: {((((int(m) % 100) % 50) % 20) % 10) % 5}')

sleep(0.5)
print(f'{cc}We appreciate your preference! {cb}Have a good day!{cn}')
sleep(0.5)
print(f'\033[37mFinalizando...{cn}')
sleep(1)
