#GRUPO: Sabrina, Yanka, Jamilly, Ana Paula e Lucas Cauan
#===================== CRUD =====================
class Empresa:
    def __init__(self):
        self.nome = "OxenteSistemas"
        self.funcionarios = []
        
    def addFuncionario(self, funcionario):
        retorno = None
        for funcionarioCadastrado in self.funcionarios:#procurar se o funcionario já existe no sistema
            if funcionario.matricula == funcionarioCadastrado.matricula or funcionario.cpf == funcionarioCadastrado.cpf:
                retorno = False#existe
        if retorno == None:#o teste do funcionarioCadastrado não encontrou esse funcionario, então o valor de RETORNO não mudou 
            self.funcionarios.append(funcionario)
            retorno = True
        return retorno

    def dellFuncionario(self, identificador):
        for funcionario in self.funcionarios:
            if funcionario.matricula == identificador or funcionario.cpf == identificador:
                self.funcionarios.remove(funcionario)
                return True
        return False
    
    def alterarFuncionario(self, matricula, alteracao, novoDado, alteracaoEndereco = None):
        NOME, MATRICULA, ENDERECO, SALARIO, SEXO, CPF, CADEIRANTE = 1,2,3,4,5,6,7
        if len(self.funcionarios) > 0:
            for funcionario in self.funcionarios:
                if funcionario.matricula == matricula:#achar funcionario
                    if alteracao == NOME:
                        funcionario.nome = novoDado
                        return True
                    elif alteracao == MATRICULA:
                        funcionario.matricula = novoDado
                        return True

                    elif alteracao == ENDERECO:
                        RUA, BAIRRO, CIDADE = 1,2,3
                        if alteracaoEndereco == RUA:
                            funcionario.endereco.rua = novoDado
                            return True
                        elif alteracaoEndereco == BAIRRO:
                            funcionario.endereco.bairro = novoDado
                            return True
                        elif alteracaoEndereco == CIDADE:
                            funcionario.endereco.cidade = novoDado
                            return True
                
                    elif alteracao == SALARIO:
                        funcionario.salario = float(novoDado)
                        return True
                    elif alteracao == SEXO:
                        funcionario.sexo = novoDado.upper()
                        return True
                    elif alteracao == CPF:
                        funcionario.cpf = novoDado
                        return True
                    elif alteracao == CADEIRANTE:
                        funcionario.cadeirante = novoDado.upper()
                        return True
        else:
            return False#lista vazia ou não achou o funcionario

    def getFuncionario(self, informacao):#encontrar funcionario pelo CPF ou MATRICULA
        for funcionario in self.funcionarios:
            if funcionario.matricula == informacao or funcionario.cpf == informacao:
                return funcionario
        return False#o funcionario não foi encontrado no FOR

    def showFuncionarios(self, opcao = None, procura = None):#lista todos os funcionários ou lista funcionários com algum filtro
        CIDADE, ESTADO, SALARIO_MAIS_5000, SALARIO_MENOS_1000, HOMENS, HOMEM_SALARIO_MAIS_800, FUNCIONARIOS_SALARIO_1000_2000_PB, FUNCIONARIO_PRIMEIRA_LETRA, MAIOR_SALARIO, MENOR_SALARIO, HOMEM_MAIS_VELHO, HOMEM_MAIS_NOVO, CADEIRANTES, APOSENTARAO = 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
        lista_funcionarios = []
        if procura != None or opcao != None:# verificação do listamento com filtro
            if opcao == CIDADE:
                for funcionario in self.funcionarios:
                    if funcionario.endereco.cidade == procura.upper():
                        lista_funcionarios.append(funcionario)
                return lista_funcionarios
            elif opcao == ESTADO:
                for funcionario in self.funcionarios:
                    if funcionario.endereco.estado == procura.upper():
                        lista_funcionarios.append(funcionario)
                return lista_funcionarios
            elif opcao == SALARIO_MAIS_5000:
                for funcionario in self.funcionarios:
                    if funcionario.salario > 5000:
                        lista_funcionarios.append(funcionario)
                return lista_funcionarios
            elif opcao == SALARIO_MENOS_1000:
                for funcionario in self.funcionarios:
                    if funcionario.salario < 1000:
                        lista_funcionarios.append(funcionario)
                return lista_funcionarios
            elif opcao == HOMENS:
                for funcionario in self.funcionarios:
                    if funcionario.sexo == "MASCULINO":
                        lista_funcionarios.append(funcionario)
                return lista_funcionarios
            elif opcao == HOMEM_SALARIO_MAIS_800:
                lista_homens = self.showFuncionarios(11)
                for funcionario in lista_homens:
                    if funcionario.salario > 800:
                        lista_funcionarios.append(funcionario)
                return lista_funcionarios
            elif opcao == FUNCIONARIOS_SALARIO_1000_2000_PB:
                for funcionario in self.funcionarios:
                    if funcionario.salario > 1000 and funcionario.salario < 2000 and funcionario.endereco.estado == "PB":
                        lista_funcionarios.append(funcionario)
                return lista_funcionarios
            elif opcao == FUNCIONARIO_PRIMEIRA_LETRA:
                for funcionario in self.funcionarios:
                    if funcionario.nome[0] == procura.upper():
                        lista_funcionarios.append(funcionario)
                return lista_funcionarios
            elif opcao == MAIOR_SALARIO:
                donoMaiorSalario = 0
                for funcionario in self.funcionarios:
                    if donoMaiorSalario == 0:
                        donoMaiorSalario = funcionario
                    elif funcionario.salario > donoMaiorSalario.salario:
                        donoMaiorSalario = funcionario
                return donoMaiorSalario
            elif opcao == MENOR_SALARIO:
                donoMenorSalario = 0
                for funcionario in self.funcionarios:
                    if donoMenorSalario == 0:
                        donoMenorSalario = funcionario
                    elif funcionario.salario < donoMenorSalario.salario:
                        donoMenorSalario = funcionario
                return donoMenorSalario
            elif opcao == HOMEM_MAIS_VELHO:
                lista_homens = self.showFuncionarios(HOMENS)
                maisVelho = 0
                for homem in lista_homens:
                    if maisVelho == 0:
                        maisVelho = homem
                    elif homem.idade > maisVelho.idade:
                        maisVelho = homem
                return maisVelho
            elif opcao ==  HOMEM_MAIS_NOVO:
                lista_homens = self.showFuncionarios(HOMENS)
                maisNovo = 0
                for homem in lista_homens:
                    if maisNovo == 0:
                        maisNovo = homem
                    elif homem.idade < maisNovo.idade:
                        maisNovo = homem
                return maisNovo
            elif opcao == CADEIRANTES:#retorna uma lista com os funcionários cadeirantes ou uma lista vazia
                lista_funcionarios_cadeirantes = []
                for funcionario in self.funcionarios:
                    if funcionario.cadeirante == "SIM":
                        lista_funcionarios_cadeirantes.append(funcionario)
                return lista_funcionarios_cadeirantes
            elif opcao == APOSENTARAO:# irão se aposentar nos prócimos 10 anos *nos próximos anos todo mundo vai né Thadeu kkkkkkk*
                #mulher: 61 anos
                #homem: 65 anos
                lista_irao_aposentar = []#retorna a lista com os funcionários que irão aposentar OU uma lista vazia
                for funcionario in self.funcionarios:
                    if funcionario.sexo == "FEMININO":
                        idade = funcionario.idade + 10
                        if idade >= 61:
                            lista_irao_aposentar.append(funcionario)
                    elif funcionario.sexo == "MASCULINO":
                        idade = funcionario.idade + 10
                        if idade >= 65:
                            lista_irao_aposentar.append(funcionario)
                return lista_irao_aposentar
            else:#a OPÇÃO digitada não existe
                return False
        else:#listamento de todos os funcionários
            return self.funcionarios

class Endereco:
    def __init__(self, rua, bairro, cidade, estado):
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade.upper()
        self.estado = estado.upper()
    def __str__(self):
        return f"====== ENDEREÇO ======\nRua: {self.rua}\nBairro: {self.bairro}\nCidade: {self.cidade}\nEstado: {self.estado}\n----------------------\n"
class Funcionario:
    def __init__(self, nome, matricula, endereco, salario, sexo,cpf, cadeirante, idade):
        self.nome = nome.upper()
        self.matricula = matricula
        self.endereco = endereco
        self.salario = float(salario)
        self.sexo = sexo.upper()
        self.cpf =cpf
        self.cadeirante = cadeirante.upper()
        self.idade = int(idade)
    def __str__(self):
        return f"========= DADOS =========\nNome: {self.nome}\nMatrícula: {self.matricula}\n{self.endereco}Salário: R${self.salario}\nSexo: {self.sexo}\nCPF: {self.cpf}\nCadeirante: {self.cadeirante}\n===================\n"
#======================== FORCA ========================

#tentamos fazer mas não conseguimos deixar 100%
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.tentativas = 4

class Moderador:
    def __init__(self, jogador):
        self.jogador = jogador
        self.palavra = ["FONE", "BOLA", "NAVIO", "VASO", "PORTA", "ESCOLA", "PERNA"]

    def sortearPalavra(self):
        import random
        num = random.randint(1,6)
        return self.palavra[num]

    def ocultarPalavra(self, palavra):
        palavraOculta = []
        for letra in range(len(palavra)):
            palavraOculta.append("_")
        return palavraOculta

    def verificarAcerto(self, palavra, palavraOculta, letra):
        letra = letra.upper()
        palavra = palavra.upper()
        listaLetras = list(palavra)
        palavraOculta = list(palavraOculta)
        retorno = False;
        if "_" in palavraOculta:
            for caracter in listaLetras:
                if caracter == letra:
                    index = palavra.find(letra)
                    palavraOculta[index] = letra
                    retorno = palavraOculta
            return retorno
        else:
            return True

    def diminuirTentativas(self):
        self.jogador.tentativas -= 1
            

        