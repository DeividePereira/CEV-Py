import requests
print('=-= Teste de abrir o site \"example.com\" =-=')

try:
    requests.get('https://example.com')

except Exception:
    print('\033[31mA operação falhou.\033[m')

else:
    print('\033[32mOperação realizada com sucesso.\033[m')

finally:
    print('Obrigado pela preferência!')
