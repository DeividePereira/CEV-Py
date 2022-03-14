# Crie a função escreva(), que receba um texto qualquer como parâmetro
# mostre uma mensagem com tamanho adaptável, como "------".
def escreva(txt):
    print(f'-' * (len(txt) + 4))
    print(f'  {txt}')
    print('-' * (len(txt) + 4))


escreva('Caraminguado')
escreva('Pneumoultramicroscopicossilicovulcanoconiótico')
escreva('Latinar')
escreva('O motorista estava ébrio.')