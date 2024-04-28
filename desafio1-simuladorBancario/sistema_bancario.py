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
quantidade_saque = 1
SAQUE_DIARIO = 3

while True:
    opcao = int(input(menu))
    
    if opcao == 0:
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            valida_deposito = input(f"Confirma o deposito no valor de R$  {valor:.2f}" + " Digite s para confirmar / n caso contrário: ").upper()
            if valida_deposito == 'S':
                saldo += valor
                extrato.append(f"Deposito no valor de R$ {saldo:.2f}")
            else:
                
                opcao = int(input(menu))
        else:
            print("Operação inválida, favor informar um valor válido!")    
    elif opcao == 1:
        saque = float(input("Digite o valor a ser sacado: "))
        excedeu_valor_saque = saque > saldo
        excedeu_quantidade_saque_diario = SAQUE_DIARIO < quantidade_saque
        if excedeu_valor_saque:
            print("Saldo insuficiente")
        elif excedeu_quantidade_saque_diario:
            print("Você já realizou o limite de 3 saques diários, favor tentar amanhã.")
        else:
            saldo -= saque
            quantidade_saque += 1 
            print(f"Operação realizada com sucesso, seu novo saldo é: R$ {saldo:.2f}")
            extrato.append(f"Saque no valor de R$ {saque:.2f}")   
    elif opcao == 2:
        if extrato == "":
            print("Não houve movimentação no período solicitado")
        else:
            print(f"""
                  ########## DioBank --- EXTRATO DE MOVIMENTAÇÃO BANCÁRIA ##########
                  {extrato}
                  """)    
    elif opcao == 3:
        break
    else:
        print("Operação inválida, favor selecionar a operação desejada.")
        
print("Agradeçemos por utilizar DioBank!")