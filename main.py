from model import *


menu = """
================== Oxente Sistemas ============
1 ......................... Cadastrar Novo Funcionário
2 ......................... Excluir Funcionário
3 ......................... Alterar Funcionário
4 ......................... Pesquisar Funcionário
6 ......................... Listar todos os Funcionários
7 ......................... Listar todos os Funcionários (Da cidade X)
8 ......................... Listar todos os Funcionários (Do Estado X)
9 ......................... Listar todos os Funcionários (Que ganham mais de R$ 5000,00)
10 ....................... Listar todos os Funcionários (Que ganham menos de R$ 1000,00)
11........................ Listar todos os Funcionários (Que são homens)
12 ....................... Listar todos os Funcionários (Que são homens e ganham mais de 800)
13 ....................... Listar os Funcionários que ganham entre 1000 e 2000 e são da PB
14 ....................... Listar todos os Funcionários (Que começam com X)
15 ....................... Mostrar o Funcionário que ganha o maior salário
16 ....................... Mostrar a Funcionária que ganha o menor salário
17 ....................... Mostrar o Funcionário mais velho (O homem mais velho)
18 ....................... Mostrar o Funcionário mais novo (O homem mais novo)
19 ....................... Listar todos os Funcionário cadeirantes
20 ....................... Listar todos os Funcionários que irá se aposentar nos próximos anos
21........................ Forca
0.......................... Sair
"""
acao = None
CADASTRAR_NOVO_FUNCIONARIO, EXCLUIR_FUNCIONARIO, ALTERAR_FUNCIONARIO, PESQUISAR_FUNCIONARIO, LISTAR_TODOS_OS_FUNCIONARIOS, LISTAR_FUNCIONARIOS_POR_CIDADE, LISTAR_FUNCIONARIOS_POR_ESTADO,SALARIO_MAIS_5000, SALARIO_MENOS_1000, HOMENS, HOMEM_SALARIO_MAIS_800, FUNCIONARIOS_SALARIO_1000_2000_PB, FUNCIONARIO_PRIMEIRA_LETRA, MAIOR_SALARIO, MENOR_SALARIO, HOMEM_MAIS_VELHO, HOMEM_MAIS_NOVO, CADEIRANTES, APOSENTARAO, FORCA, SAIR = 1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,0
empresa = Empresa()
while(acao != 0):
    print(menu)
    acao = int(input("\nDigite sua ação: "))

    if acao == CADASTRAR_NOVO_FUNCIONARIO:
        print("\n========== CADASTRAMENTO ==========\n")
        nome = input("Digite o nome do funcionário: ")
        matricula = input("Digite a matrícula do funcionario: ")
        rua = input("Digite a rua do funcionário: ")
        bairro = input("Digite o bairro: ")
        cidade = input("Digite a cidade: ")
        estado = input("Digite o Estado: ")
        cpf = input("Digite o CPF: ")
        salario = input("Digite o salário: R$")
        sexo = input("Qual o sexo do funcionário. Digite (FEMININO) para funcionária e (MASCULINO) para funcionário. Informe:")
        cadeirante = input("O funcionário é cadeirante? (SIM) para sim e (NÃO) para não. Informe: ")
        idade = input("Idade do funcionário: ")

        endereco = Endereco(rua, bairro, cidade, estado)
        funcionario = Funcionario(nome, matricula, endereco, salario,sexo, cpf, cadeirante, idade)
        
        retorno = empresa.addFuncionario(funcionario)
        if retorno == True:
            print("Adicionado com sucesso!")
        else:
            print("Erro, cpf ou matrícula já existente")

    elif acao == EXCLUIR_FUNCIONARIO:
        dado = input("\nDigite a matrícula ou CPF do funcionário a ser excluído: ")
        retorno = empresa.dellFuncionario(dado)
        if retorno == True:
            print("Funcionário excluído com sucesso!")
        else:
            print("Erro. Funcionário não encontrado")
    elif acao == ALTERAR_FUNCIONARIO:
        matricula = input("Digite a matrícula do funcionário: ")
        menuAlteracao ="""
        -> O que deseja alterar?
        1........................Nome
        2...................Matricula
        3....................Endereço
        4.....................Salário
        5........................Sexo
        6.........................CPF
        7..................Cadeirante
        """
        print(menuAlteracao)
        NOME, MATRICULA, ENDERECO, SALARIO, SEXO, CPF, CADEIRANTE = 1,2,3,4,5,6,7
        alteracao = int(input("Digite sua acao: "))
        if alteracao == NOME:
            novoNome = input("Digite o novo nome: ")
            retorno = empresa.alterarFuncionario(matricula, alteracao, novoNome)
            if retorno == True:
                print("Nome alterado com sucesso!")
            else:
                print("Erro")
        elif alteracao == MATRICULA:
            novaMatricula = input("Digite a nova matrícula:")
            retorno = empresa.alterarFuncionario(matricula, alteracao, novaMatricula)
            if retorno == True:
                print("Matrícula alterada com sucesso!")
            else:
                print("Erro")
        elif alteracao == ENDERECO:
            RUA, BAIRRO, CIDADE =1,2,3
            menuAlteracaoEndereco = """
            1........................Rua
            2.....................Bairro
            3.....................Cidade
            """
            print(menuAlteracaoEndereco)
            acao = int(input("O que deseja alterar?: "))
            if acao == RUA:
                novaRua = input("Digite a nova rua: ")
                retorno = empresa.alterarFuncionario(matricula,ENDERECO, novaRua, RUA)
                if retorno == True:
                    print("Rua alterada com sucesso!")
                else:
                    print("Erro! Funcionário não encontrado") 
            elif acao == BAIRRO:
                novoBairro = input("Digite o novo bairro: ")
                retorno = empresa.alterarFuncionario(matricula, ENDERECO, novoBairro, BAIRRO)
                if retorno == True:
                    print("Bairro alterado com sucesso!")
                else:
                    print("Erro! Funcionário não encontrado")
            elif acao == CIDADE:
                novaCidade = input("Informe a nova cidade: ")
                retorno = empresa.alterarFuncionario(matricula, ENDERECO, novaCidade, CIDADE)
                if retorno == True:
                    print("Cidade alterado com sucesso!")
                else:
                    print("Erro! Funcionário não encontrado")
        elif alteracao == SALARIO:
            novoSalario = int(input("Informe o novo salário: R$ "))
            retorno = empresa.alterarFuncionario(matricula, SALARIO, novoSalario)
            if retorno == True:
                print("Salário alterado com sucesso!")
            else:
                print("Erro! Funcionário não encontrado")
        elif alteracao == SEXO:
            novoSexo = input("Informe o novo sexo: ")
            retorno = empresa.alterarFuncionario(matricula, SEXO, novoSexo)
            if retorno == True:
                print("Sexo alterado com sucesso!")
            else:
                print("Erro! Funcionário não encontrado")
        elif alteracao == CPF:
            novoCPF = input("Digite o novo CPF: ")
            retorno = empresa.alterarFuncionario(matricula, CPF, novoCPF)
            if retorno == True:
                print("CPF alterado com sucesso!")
            else:
                print("Erro! Funcionário não encontrado")
        elif alteracao == CADEIRANTE:
            novaInformacao = input("O funcionário é cadeirante ainda? (SIM) para sim e (NÃO) para não\nInforme: ")
            retorno = empresa.alterarFuncionario(matricula, CADEIRANTE, novaInformacao)
            if retorno == True:
                print("Status de deficiência do funcionário alterado com sucesso!")
            else:
                print("Erro! Funcionário não encontrado")
    elif acao == PESQUISAR_FUNCIONARIO:
        informacao = input("Informe a matrícula ou CPF do funcionário: ")
        retorno = empresa.getFuncionario(informacao)
        if retorno != False:
            print(retorno)
        else:
            print("Funcionário não encontrado")
    elif acao == LISTAR_TODOS_OS_FUNCIONARIOS:
        retorno = empresa.showFuncionarios()
        for funcionario in retorno:
            print(funcionario)
    elif acao == LISTAR_FUNCIONARIOS_POR_CIDADE:
        cidade = input("Informe a cidade para filtrar os funcionários: ")
        retorno = empresa.showFuncionarios(LISTAR_FUNCIONARIOS_POR_CIDADE, cidade)
        if retorno == False:
            print("Erro")
        else:
            for funcionario in retorno:
                print(funcionario)
    elif acao == LISTAR_FUNCIONARIOS_POR_ESTADO:
        estado = input("Informe o estado para filtrar os funcionários: ")
        retorno = empresa.showFuncionarios(LISTAR_FUNCIONARIOS_POR_ESTADO, estado)
        if retorno == False:
            print("Erro")
        else:
            for funcionario in retorno:
                print(funcionario)
    elif acao == SALARIO_MAIS_5000:
        retorno = empresa.showFuncionarios(SALARIO_MAIS_5000)
        if retorno == False:
            print("Erro")
        else:
            for funcionario in retorno:
                print(funcionario)
    elif acao == SALARIO_MENOS_1000:
        retorno = empresa.showFuncionarios(SALARIO_MENOS_1000)
        if retorno == False:
            print("Erro")
        else:
            for funcionario in retorno:
                print(funcionario)
    elif acao == HOMENS:
        retorno = empresa.showFuncionarios(HOMENS)
        if retorno == False:
            print("Erro")
        else:
            for homem in retorno:
                print(homem)
    elif acao == HOMEM_SALARIO_MAIS_800:
        retorno = empresa.showFuncionarios(HOMEM_SALARIO_MAIS_800)
        if retorno == False:
            print("Erro")
        else:
            for homem in retorno:
                print(homem)
    elif acao == FUNCIONARIOS_SALARIO_1000_2000_PB:
        retorno = empresa.showFuncionarios(FUNCIONARIOS_SALARIO_1000_2000_PB)
        if retorno == False:
            print("Erro")
        else:
            for funcionario in retorno:
                print(funcionario)
    elif acao == FUNCIONARIO_PRIMEIRA_LETRA:
        letra = input("Digite a 1° letra do nome dos funcionários que deseja filtrar: ")
        retorno = empresa.showFuncionarios(FUNCIONARIO_PRIMEIRA_LETRA, letra)
        if retorno == False:
            print("Erro, nenhum funcionário tem o nome que comece com essa letra")
        else:
            for funcionario in retorno:
                print(funcionario)
    elif acao == MAIOR_SALARIO:
        retorno = empresa.showFuncionarios(MAIOR_SALARIO)
        if retorno == False:
            print("Erro")
        else:
            print(f"O funcionário que ganha o maior salário é:")
            print(retorno)
    elif acao == MENOR_SALARIO:
        retorno = empresa.showFuncionarios(MENOR_SALARIO)
        if retorno == False:
            print("Erro")
        else:
            print(f"O funcionário que ganha o menor salário é:")
            print(retorno)
    elif acao == HOMEM_MAIS_VELHO:
        retorno = empresa.showFuncionarios(HOMEM_MAIS_VELHO)
        if retorno == False:
            print("Erro")
        else:
            print("O homem mais velho é:")
            print(retorno)
    elif acao == HOMEM_MAIS_NOVO:
        retorno = empresa.showFuncionarios(HOMEM_MAIS_NOVO)
        if retorno == False:
            print("Erro")
        else:
            print("O homem mais novo é:")
            print(retorno)
    elif acao == CADEIRANTES:
        retorno = empresa.showFuncionarios(CADEIRANTES)
        if len(retorno) == 0:
            print("Não tem registro de funcionários cadeirantes no sistema")
        else:
            for cadeirante in retorno:
                print(cadeirante)
    elif acao == APOSENTARAO:
        retorno = empresa.showFuncionarios(APOSENTARAO)
        if len(retorno) > 0:
            for funcionario in retorno:
                print(funcionario)
        else:
            print("ninguém se aposentará nos próximos 10 anos")
    else:
        if acao == 0:
            break
        else:
            print("Opção digitada não existe!")
print("Programa encerrado")