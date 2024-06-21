def banco():
    LIMITESAQUE_DIARIO = 3
    AGENCIA = "0001"
    saldo = 0
    numero_conta = 1
    saque_limite = 500
    extrato = ""
    quantidade_saque = 0
    clientes = []
    contas = []
    
    while True:
        opcao = menu()
        if opcao == 0:
            valor = float(input("Digite o valor a ser depositado: "))
            saldo, extrato = realizar_deposito(saldo, valor, extrato)
        elif opcao == 1:
            valor = float(input("Digite o valor que deseja sacar:"))
            saldo, extrato = realizar_saque(
                saldo_saque=saldo, 
                valor_saque=valor, 
                extrato_saque=extrato, 
                valor_limite_saque=saque_limite, 
                quantidade_saque_realizado=quantidade_saque, 
                limite_saque_diario=LIMITESAQUE_DIARIO
            )
        elif opcao == 2:
            mostrar_extrato(saldo, extrato=extrato)
        elif opcao == 3:
            cadastrar_cliente(clientes)
        elif opcao == 4:
            conta = cadastrar_conta(
                agencia_conta=AGENCIA, 
                conta=numero_conta, 
                clientes_conta=clientes
            )
            contas.append(conta)
            numero_conta += 1
        elif opcao == 5:
            print("######## Obrigado por utilizar o DIOBANK, até a próxima! ########")
            break
        else:
            print("Opção invalida, informe a opção desejada.")
                


def menu():
    menu = """" 
    ################ Bem-vindo ao DIOBANK o banco digital que pensa em você! ################
    Para começar escolha uma opção:
    0 - Depositar 
    1 - Sacar 
    2 - Extrato
    3 - Cadastrar Cliente
    4 - Criar Conta 
    5 - Sair 
    ###### => """
    return int(input(menu))

def realizar_deposito(saldo, valor, extrato):
    if valor > 0:
        valida_deposito = input(f"Confirma o deposito no valor de R$  {valor:.2f}" + " Digite s para confirmar / n caso contrário: ").upper()
        if valida_deposito == 'S':
            saldo += valor
            extrato += f"Deposito\t\tR$ {valor:.2f}\n"
            return saldo, extrato
        else:
            return "Deposito não realizado."
    else:
        return "Operação inválida, favor informar um valor válido!"    

def realizar_saque(*, saldo_saque, valor_saque, extrato_saque, quantidade_saque_realizado, limite_saque_diario, valor_limite_saque):     
    saque_invalido = valor_saque > saldo_saque
    excedeu_saque_diario = limite_saque_diario < quantidade_saque_realizado
    excedeu_valor_limite = valor_saque > valor_limite_saque
    if saque_invalido:
        print("Saldo insuficiente")
    elif excedeu_saque_diario:
        print("Quantidade diária de saque excedida.")
    elif excedeu_valor_limite:
        print(f"O valor máximo permitido para saque é R$ {valor_limite_saque:.2f}")
    else:
        saldo_saque -= valor_saque
        print(f"==== Saque realizado com sucesso R$ {valor_saque:.2f} ====")
        extrato_saque += f"Saque\t\tR$ {valor_saque:.2f} \n"
        return saldo_saque, extrato_saque
        
def mostrar_extrato(saldo, /, *, extrato):
    print("########## DioBank --- EXTRATO DE MOVIMENTAÇÃO BANCÁRIA ##########")
    print("Não houve movimentação no período solicitado" if not extrato else extrato)
    print(f"Saldo\t\tR$ {saldo:.2f}")
    print("##################################################################")
    
def cadastrar_cliente(clientes):
    cpf = input("Digite seu cpf: ")
    if len(cpf) != 11:
        print("CPF inválido.")
        cpf = input("Digite seu cpf: ")
        
    validar_cpf = buscar_cliente(cpf, clientes)
    
    if validar_cpf != 'cpf_invalido':
        nome = input("Digite seu nome: ")
        nascimento = input("Digite sua data de nacimento(Formato: xx/xx/xxxx): ")
        cep = input("Digite seu CEP: ")
        logradouro = input("Digite o seu logradouro: ")
        numero = input("Digite o numero: ")
        bairro = input("Digite seu bairro: ")
        cidade = input("Digite sua cidade: ")
        estado = input("Digite a sigla do seu estado (Ex.: RJ / BA / ETC): ")
        endereco = f"Endereço:\t{logradouro}\t{numero}\t{bairro}\t{cidade} / {estado} - {cep}"
        cliente = {"cpf": cpf, "nome": nome, "data_nascimento": nascimento, "endereco": endereco}
        criar = input(f"Deseja criar\t{cliente['nome']} - {cliente['cpf']} - {cliente['data_nascimento']} - {cliente['endereco']} - Digite s (sim) / n (não): ").upper()
        if criar == 'S':
            print(f"######## Bem vindo\t{cliente['nome']}\tao DIOBANK! Desejamos uma excelente experiência! ########")
            clientes.append(cliente)
        else:
            return
    else:
        print("Cliente já cadastrado, favor utilizar outro CPF")
        continuar = input("Deseja continuar? Digite s (sim) / n (não): ").upper()
        if continuar == "S":
            cpf = input("Digite seu CPF: ")
        else:
            return

def buscar_cliente(cpf_cliente, lista_clientes):
    cliente_buscado = [cliente for cliente in lista_clientes if cliente["cpf"] == cpf_cliente]
    return cliente_buscado[0] if cliente_buscado else "cpf_invalido"

def cadastrar_conta(conta, agencia_conta, clientes_conta):
    print(" ######## DIOBANK Cadastro de Conta ########")
    cpf = input("Digite seu CPF: ")
    cliente = buscar_cliente(cpf, clientes_conta)
    if cliente != "cpf_invalido":
        print("Parabéns sua conta DIOBANK foi criada com sucesso!")
        return {'conta': conta, 'agencia': agencia_conta, 'cliente': cliente}
    
    print("###### Cliente não encontrado, aproveite e se cadastre em nosso menu de opções! DIOBANK sempre com você ######")

banco()