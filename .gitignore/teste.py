from model import *

empresa = Empresa()
endereco1 = Endereco("Geraldo da Costa Cirne", "Dinarte Mariz", "Parelhas", "RN")
endereco2 = Endereco("José Valera", "Campim Macio", "Natal", "RN")
endereco3 = Endereco("Rua Maneiro", "Petrópolis", "Natal", "RN")
endereco4 = Endereco("Rua das Malvinas", "JUJU", "Rio de Janeiro", "RJ")
endereco5 = Endereco("Rua dos chatos", "resmundos", "João Pessoa", "PB")

funcionario1 = Funcionario("Sabrina", "20201214010012", endereco1, 800, "Feminino", "112-111", "Não", 17)
funcionario2 = Funcionario("Gabi", "2020", endereco2, 61600, "Feminino", "111-111", "Não", 24)
funcionario3 = Funcionario("rafa", "1012", endereco3, 801, "Masculino", "113-111", "Não", 25)
funcionario5 = Funcionario("Ciza", "105512", endereco5, 1400, "Masculino", "177-111", "Não", 64)
funcionario4 = Funcionario("Neide", "74128962", endereco4, 1500, "Feminino", "123-111", "Não", 56)

# empresa.addFuncionario(funcionario1)
empresa.addFuncionario(funcionario2)
empresa.addFuncionario(funcionario3)
empresa.addFuncionario(funcionario1)
empresa.addFuncionario(funcionario4)
empresa.addFuncionario(funcionario5)

# retorno = empresa.showFuncionarios()
# for i in retorno:
#     print(i)
# retorno = empresa.showFuncionarios(21)
# print(retorno)
# # if len(retorno) == 0:
# #     print("Não tem cadeirantes cadastrado")
# # else:
# #     for funcionario in retorno:
# #         print(funcionario)
# if retorno == False:
#     print("Sem essa opção")
# palavra = "Sabis"
# retorno = len(palavra)
# print(retorno)
# retorno = palavra.find("a")
# print(retorno)

# palavra = Palavra("maneiro")
# jogador = Jogador("Sabrina")
# moderador = Moderador(palavra, jogador)
# # retorno = moderador.verificarAcerto("n")
# # if retorno == False:
# #     print("sem tentativas")
# # elif jogador.tentativas < 4 and retorno == False:
# #     print("Você errou")
# palavra.ocultarPalavra()
# retorno = moderador.verificarAcerto("i")
# print(retorno)
jogador = Jogador("Sabrina")
moderador = Moderador(jogador)
palavra = moderador.sortearPalavra()
print(palavra)
palavraOcultada = moderador.ocultarPalavra(palavra)
print(palavraOcultada)
# if verelacao == False:
#     print("Errei")
# else:
#     print(verelacao)
letra = "l"
ultimaVerificacao = None;

verificacao = moderador.verificarAcerto(palavra, palavraOcultada, "L")

if verificacao == False:
    print("vix")
    verificacao = ultimaVerificacao
else:
    print(verificacao)
verificacao = moderador.verificarAcerto(palavra, verificacao, "a")
ultimaVerificacao = verificacao
if verificacao == False:
    print("vix")
    verificacao = ultimaVerificacao
else:
    print(verificacao)

verificacao = moderador.verificarAcerto(palavra, verificacao, "P")
if verificacao == False:
    print("vix")
    verificacao = ultimaVerificacao
else:
    print(verificacao)

verificacao = moderador.verificarAcerto(palavra, verificacao, "R")
if verificacao == False:
    print("vix")
    verificacao = ultimaVerificacao
else:
    print(verificacao)
