class Usuario:
    def __init__(self, nome, cpf, data_nasc, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc
        self.endereco = endereco

    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"CPF: {self.cpf}\n"
                f"Data de Nascimento: {self.data_nasc}\n"
                f"Endereço: {self.endereco}")


class Conta:
    def __init__(self, usuario, numero_conta, agencia="0001", saldo=0.0, lim_saque=500, max_saques_diario=3):
        self.usuario = usuario
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.saldo = saldo
        self.lim_saque = lim_saque
        self.saques_realizados = 0
        self.max_saques_diario = max_saques_diario

    def depositar(self, valor):
        if valor <= 0:
            print("Erro: O valor do depósito deve ser maior que zero.")
        else:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def saque(self, *, valor):
        if self.saldo <= 0:
            print("Erro: Saldo insuficiente.")
            return

        if valor > self.lim_saque:
            print("Erro: Saque acima do limite permitido de R$500,00.")
            return

        if self.saques_realizados >= self.max_saques_diario:
            print("Erro: Limite de saques diários atingido.")
            return

        self.saldo -= valor
        self.saques_realizados += 1
        print(f"Saque de R${valor:.2f} efetuado com sucesso.")

    def extrato(self):
        print("========= Extrato ==========")
        print(f"Saldo: R${self.saldo:.2f}")
        print(f"Saques realizados hoje: {self.saques_realizados}")


def criar_usuario(lista_usuarios):
    nome = input("Nome: ")
    cpf = input("CPF: ")
    data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
    endereco = input("Endereço (Rua, Número, Bairro, Cidade/UF): ")

    for usuario in lista_usuarios:
        if usuario.cpf == cpf:
            print("Erro: CPF já cadastrado.")
            return None

    novo_usuario = Usuario(nome, cpf, data_nascimento, endereco)
    lista_usuarios.append(novo_usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")
    return novo_usuario


def criar_conta(lista_contas, lista_usuarios):
    cpf = input("Digite o CPF do usuário: ")

    usuario_encontrado = None
    for usuario in lista_usuarios:
        if usuario.cpf == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        print("Erro: Usuário não encontrado. Cadastre o usuário primeiro.")
        return None

    numero_conta = len(lista_contas) + 1
    nova_conta = Conta(usuario_encontrado, numero_conta)

    lista_contas.append(nova_conta)
    print(f"Conta {numero_conta} criada com sucesso para {usuario_encontrado.nome}.")
    return nova_conta


def selecionar_conta(lista_contas):
    """Seleciona uma conta bancária a partir do CPF."""
    cpf = input("Digite o CPF do titular da conta: ")

    contas_encontradas = [conta for conta in lista_contas if conta.usuario.cpf == cpf]

    if not contas_encontradas:
        print("Erro: Nenhuma conta encontrada para esse CPF.")
        return None

    print("\nContas disponíveis:")
    for conta in contas_encontradas:
        print(f"Número da Conta: {conta.numero_conta} | Agência: {conta.agencia}")

    num_conta = int(input("Digite o número da conta desejada: "))

    for conta in contas_encontradas:
        if conta.numero_conta == num_conta:
            return conta

    print("Erro: Conta não encontrada.")
    return None


# ========== Menu de Operações ==========
usuarios = []
contas = []

while True:
    print("\n========== MENU ==========")
    print("[u] Criar usuário")
    print("[c] Criar conta")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[l] Listar usuários")
    print("[t] Listar contas")
    print("[q] Sair")

    opcao = input("Escolha uma opção: ").lower()

    if opcao == "u":
        criar_usuario(usuarios)

    elif opcao == "c":
        criar_conta(contas, usuarios)

    elif opcao == "d":
        conta = selecionar_conta(contas)
        if conta:
            valor = float(input("Digite o valor do depósito: "))
            conta.depositar(valor)

    elif opcao == "s":
        conta = selecionar_conta(contas)
        if conta:
            valor = float(input("Digite o valor do saque: "))
            conta.saque(valor=valor)

    elif opcao == "e":
        conta = selecionar_conta(contas)
        if conta:
            conta.extrato()

    elif opcao == "l":
        print("\n======= Usuários Cadastrados =======")
        for usuario in usuarios:
            print(usuario)
            print("-" * 30)

    elif opcao == "t":
        print("\n======= Contas Bancárias =======")
        for conta in contas:
            print(f"Agência: {conta.agencia} | Número da Conta: {conta.numero_conta} | Titular: {conta.usuario.nome}")
            print("-" * 30)

    elif opcao == "q":
        print("Saindo do programa. Obrigado!")
        break

    else:
        print("Opção inválida. Tente novamente.")