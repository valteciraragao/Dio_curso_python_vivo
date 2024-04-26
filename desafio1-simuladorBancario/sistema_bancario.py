menu = """" 
Bem-vindo ao DioBank o banco digital que pensa em você, digite uma opção para começar:

0 - Depositar
1 - Sacar
2 - Extrato
3 - Sair

=> """

saldo = 0
saque_limite = 500
extrato = []
quantidade_saque = 0
SAQUE_DIARIO = 3

while True:
    opcao = int(input(menu))
    
    if opcao == 0:
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            valida_deposito = input(f"Confirma o deposito no valor de R$ {valor:.2f}:").upper()
            if valida_deposito == 'S':
                saldo += valor
                extrato += f"Deposito no valor de R$ {saldo:.2f}"
            else:
                print("Agradeçemos por utilizar DioBank!")
                break    
        else:
            print("Operação inválida, favor informar um valor válido!")    
    elif opcao == 1:
        saque = float(input("Digite o valor a ser sacado: "))
        excedeu_valor_saque = saque > saldo
        excedeu_quantidade_saque_diario = quantidade_saque > SAQUE_DIARIO
            
    elif opcao == 2:
    elif opcao == 3:
        break
    else:
        print("Operação inválida, favor selecionar a operação desejada.")