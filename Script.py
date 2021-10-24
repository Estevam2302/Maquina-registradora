print('Maquina registradora')
print('Para encerrar o programa digite "0"')
print('Digite o código do produto conforme a tabela abaixo')
print('Produto 1 = 1')
print('Produto 2 = 2')
print('Produto 3 = 3')
print('Produto 4 = 4')
print('Produto 5 = 5')
total = 0
while True:
    produto = int(input('Insira o código do produto: '))
    if produto == 1:
        valor = float(0.50)
    elif produto == 2:
        valor = float(1.00)
    elif produto == 3:
        valor = float (4.00)
    elif produto == 4:
        valor = float (7.00)
    elif produto == 5:
        valor = float (8.00)
    if produto == 0:
        print('Programa encerrado!')
        break
    quantidade = int(input('Insira a quantidade comprada: '))
    if quantidade == 0:
        print('Programa encerrado!')
        break
    total = float(valor*quantidade+total)
    print('Total a pagar: R$ %.2f' %total)
