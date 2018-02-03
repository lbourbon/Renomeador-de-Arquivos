# encoding: utf-8
from os import rename, listdir, getcwd, path

try:
    # MOSTRA INSTRUÇÕES

    print('''####################################################################################################################
####################################################################################################################
####################################################################################################################
###                                   ZZ Renomeador de Arquivos                                                  ###
####################################################################################################################
####################################################################################################################
####################################################################################################################
### FUNÇÃO:                                                                                                      ###
###  MUDAR RAPIDAMENTE O NOME DOS ARQUIVOS EM UMA PASTA, PRINCIPALMENTE PARA NUMERAR SÉRIES                      ###
####################################################################################################################
### INSTRUÇÕES:                                                                                                  ###
### -> A PASTA DE NOME "ZZ FILE NUMERATOR TABAJARA" DEVE ESTAR DENTRO DA PASTA COM OS ARQUIVOS CUJOS NOMES SERÃO ###
###    MODIFICADOS. ESSA PASTA NÃO DEVE CONTER MAIS NENHUM OUTROS ARQUIVO, POIS TODOS ELES SERÃO RENOMEADOS.     ###
### -> A PASTA DEVE ESTAR ALFABETICAMENTE POSICIONADA APÓS TODOS OS ARQUIVOS, POR ISSO O NOME COMEÇA COM "ZZ"    ###
####################################################################################################################
### PERGUNTAS:                                                                                                   ###
###  1) QUAL NOME COLOCAR NOS ARQUIVOS? -> DIGITE QUALQUER NOME, A NUMERAÇÃO SERÁ INCLUÍDA LOGO APÓS O NOME QUE  ###
###     VOCÊ ESCOLHER, POR ISSO LEMBRE DE ACRESCENTAR UM ESPAÇO EM BRANCO APÓS O NOME, SE JULGAR NECESSÁRIO      ###
###  2) COMEÇAR A NUMERAÇÃO A PARTIR DE QUE NÚMERO? -> ESCOLHE A NUMERAÇÃO A SER COLOCADA NO PRIMEIRO ARQUIVO,   ###
###     DEPOIS DELE, CADA ARQUIVO SERÁ NUMERADO EM ORDEM CRESCENTE.                                              ###
###  3) QUANTOS ZERO COLOCAR ANTES DE CADA DÍGITO? -> PARA EVITAR PROBLEMAS COM A ORDENAÇÃO ALFABÉTICA QUANTO    ###
###     TEMOS MUITOS ARQUIVOS, (EX. O ARQUIVO 'exemplo10' FICA ANTES DO ARQUIVO 'exemplo2'). PARA RESOLVER ESSE  ###
###     PROBLEMA COLOQUE PELO MENOS 1 ZERO ANTES DE CADA DÍGITO.                                                 ###
###  4) POSSUI LEGENDAS? -> CASO A PASTA CONTENHA AS LEGENDAS, O NOME DE CADA ARQUIVO SERÁ REPETIDO NO ARQUIVO   ###
###     SEGUINTE, PARA QUE VÍDEO E LEGENDA TENHAM O MESMO NOME. PARA ISSO, CADA LEGENDA DEVE ESTAR SITUADA       ###
###     ALFABETICAMENTE LOGO APÓS O RESPECTIVO VÍDEO.                                                            ###
####################################################################################################################
####################################################################################################################
####################################################################################################################\n\n''')

    # INPUT DE VARIÁVEIS PELO USUÁRIO

    nome = str(input(
        'QUAL NOME COLOCAR NOS ARQUIVOS? Ex: "Game Of Thrones S07E".\n'))
    start = int(input('COMEÇAR A NUMERAÇÃO A PARTIR DE QUE NÚMERO?\n'))
    zeros = int(input('QUANTOS ZERO COLOCAR ANTES DE CADA DÍGITO? Ex: 0, 1 ou 2. => Resultados: 1, 01 ou 001.\n'))
    leg = str(input(
        'POSSUI LEGENDAS? DIGITE "s" para SIM, "n" para NÃO. Obs: Cada legenda deve estar após o respectivo vídeo\n'))
    legendas = True if leg.lower() == 's' else False

    # PEGA O PATH DO SCRIPT  E CRIA UM ITERÁVEL COM OS ARQUIVOS DA PASTA

    my_path = (path.dirname(getcwd()) + '\\').replace('\\', '/')
    folder = iter(listdir(my_path)[:-1])

    # RENOMEAR OS ARQUIVOS

    for file in folder:
        rename(my_path + file, my_path + nome + str(start).zfill(1 + zeros) + file[-4:])
        if legendas:
            temp = str(next(folder))
            rename(my_path + temp, my_path + nome + str(start).zfill(1 + zeros) + temp[-4:])
        start += 1

    # ENCERRA

    wait = input("TAREFA CONCLUÍDA COM SUCESSO. PRESSIONE ENTER PARA ENCERRAR O PROGRAMA.")
    raise SystemExit


except Exception as e:

    print('Devido a sua incompetência em preencher um simples questionário, esse programa deu erro e será fechado!')
    print('ERRO: ', e)
    raise SystemExit
