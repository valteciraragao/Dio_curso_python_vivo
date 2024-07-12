```markdown
# DIOBANK - Um projeto realizado pelo Bootcamp da @DIO. 🚀

## Visão Geral 🤖

Bem-vindo ao DIOBANK, um sistema de gerenciamento bancário completo desenvolvido em Python. Este projeto abrange conceitos essenciais de Programação Orientada a Objetos (POO), incluindo herança, encapsulamento e polimorfismo, além de técnicas avançadas como o uso de classes abstratas e propriedades.

## Funcionalidades

- **Cadastro de Clientes:** Suporta cadastro de pessoas físicas (PF) e jurídicas (PJ).
- **Criação de Contas:** Permite a criação de contas correntes e poupanças com controle de saldo e histórico de transações.
- **Operações Bancárias:** Inclui funcionalidades para depósito, saque e consulta de extrato.
- **Histórico de Transações:** Mantém um registro detalhado de todas as operações realizadas em cada conta.

## Estrutura do Projeto 🏗️

O projeto está organizado em classes que representam os principais componentes do sistema bancário:

### Clientes

- **Cliente:** Classe base para todos os clientes, armazenando o endereço.
- **PessoaFisica:** Herda de `Cliente`, adicionando atributos como nome, data de nascimento e CPF.
- **PessoaJuridica:** Herda de `Cliente`, adicionando atributos como nome da empresa, data de início de atividade e CNPJ.

### Contas

- **Conta:** Classe abstrata que define a estrutura básica de uma conta bancária.
- **ContaCorrente:** Herda de `Conta`, com funcionalidades específicas como limite de saque diário.
- **ContaPoupanca:** Herda de `Conta`, incluindo a capacidade de gerar rendimentos.

### Transações

- **Transacao:** Classe abstrata que define o comportamento básico de uma transação.
- **Saque:** Herda de `Transacao`, representando a operação de saque.
- **Deposito:** Herda de `Transacao`, representando a operação de depósito.

### Histórico

- **Historico:** Armazena todas as transações realizadas em uma conta, permitindo consultas detalhadas.

### Banco

- **banco_DIO:** Classe principal que gerencia os clientes, contas e todas as operações bancárias.

### Diagrama de Classes 📊

```plaintext
Cliente
├── PessoaFisica
└── PessoaJuridica
Conta (Abstract Base Class)
├── ContaCorrente
└── ContaPoupanca
Transacao (Abstract Base Class)
├── Saque
└── Deposito
Historico
BancoDIO
```

## Como Usar 🛠️

Para executar o DIOBANK, basta rodar o arquivo principal do projeto. Certifique-se de ter o Python instalado em sua máquina.

```bash
python banco_DIO.py
```

## Exemplo de Uso 🚀 

Ao iniciar o sistema, você será apresentado ao menu principal com as seguintes opções:

```
#################### Bem-vindo ao DIOBANK o banco que pensa em você! ####################
Escolha uma opção:
1  Novo Cliente
2  Nova Conta Corrente
3  Nova Conta Poupança
4  Realizar Depósito
5  Realizar Saque
6  Mostrar Extrato
0  Sair
```

### Cadastro de Cliente 💻

Informe se o cliente é Pessoa Física (PF) ou Jurídica (PJ) e preencha os dados solicitados:

```plaintext
Para continuar informe o tipo de cliente:
    Pessoa Física digite --> PF;
    Pessoa Juridica digite --> PJ;
==> PF

CPF: 12345678901
Nome Completo: João da Silva
Endereço: Rua Exemplo, 123 - Centro São Paulo / SP
Data Nascimento: 01/01/1980
Cliente João da Silva cadastrado com sucesso!
```

### Criação de Conta Corrente 💻

Crie uma conta corrente para um cliente existente:

```plaintext
Digite o CPF ou CNPJ do cliente: 12345678901
Conta Corrente criada com sucesso para o cliente João da Silva.
```

### Realizar Depósito 💻

Faça um depósito em uma conta existente:

```plaintext
Digite o CPF ou CNPJ do cliente: 12345678901
Digite o valor a ser depositado: 500
Depósito de R$ 500,00 realizado com sucesso!
```

### Realizar Saque 💻

Realize um saque de uma conta existente:

```plaintext
Digite o CPF ou CNPJ do cliente: 12345678901
Digite o valor que deseja sacar: 200
==== Saque realizado com sucesso R$ 200,00 ====
```

### Mostrar Extrato 💻

Consulte o extrato de uma conta:

```plaintext
Digite o CPF ou CNPJ do cliente: 12345678901
Conta encontrada:
C/C: 300
Titular: João da Silva
Agência: 003
Saldo: R$ 300,00
Histórico de transações:
Depósito R$ 500,00
Saque Conta Corrente R$ 200,00
```

## Conclusão

DIOBANK é um projeto robusto e flexível que demonstra a aplicação prática dos principais conceitos de POO em Python. Sinta-se à vontade para explorar, modificar e expandir o sistema conforme suas necessidades.

---

### Contribuições 🤝

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, por favor, abra uma issue ou envie um pull request.

---

### Licença 📜

Este projeto é licenciado sob os termos da MIT License.

---

## Contato 📧

- **Nome**: Valtecir Aragao
- **E-mail**: valteciraragao@poli.ufrj.br
- **LinkedIn**: [Seu Perfil](https://www.linkedin.com/in/valteciraragao)

---

Desenvolvido com 🚀🚀🚀 por [Valtecir Aragao](https://github.com/valteciraragao)
```


