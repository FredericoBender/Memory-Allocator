#encoding=utf-8

#DEFINIÇÃO DO PADRÃO DE ESCRITA
    #COMENTÁRIOS
        #1º Modo de escrita dos comentários livre, ´~^-_+=, etc, permitidos
            #ex: meu nome é, variável de saída
    #FUNÇÕES
        #2º Nomes das funções SEM ´~^-_+=, etc. E pode usar "De"
        #3º Comentários no início das funções explicando o que fazem
        #4º Comentários no final das funções explicando o que retornam
            #ex: meuNomeE, variavelDeSaida
    #VARIÁVEIS
        #5º Variáveis iniciadas em mínuscula, SEM ´~^-_+= etc, SEM "De", se tiver mais de uma palavra, esta, deve ser iniciada em maíuscula
            #ex: meuNomeE, variavelSaida

import funcoes as f

#INICIALIZAÇÃO: Criação das estruturas necessárias
processos = f.interpreta("arq1.txt")
f.listaDeTamanhos(processos)
#tamanhos = lista de tamanho dos processos = [tamanho,...]
dicionarioDeEntrada = f.dicionarioDeEntrada(processos)
dicionarioDeSaida = f.dicionarioDeSaida(processos)
dicionarioDeProcessos = {}
clock = 0
del processos

"""print("\nDicionário de Entradas:\n")
print(dicionarioDeEntrada, end='\n\n')
print("Dicionário de Saídas:\n")
print(dicionarioDeSaida,end='\n\n')"""
##################################################
modo = "worst"
tamMemoria = 10000
#Início algoritmo: Cada loop é um ciclo
while (dicionarioDeSaida):
    #Remoção de processo
    if (clock in dicionarioDeEntrada):
        #print(str(clock) + ":" + str(dicionarioDeEntrada[clock]))
        while (dicionarioDeEntrada[clock]):
            ###print(str(clock) +":" +str(dicionarioDeEntrada))
            processo = dicionarioDeEntrada[clock].pop() #Remove e salva ultimo elemento da lista
            dicionarioDeProcessos = f.alocarMemoria(processo,tamMemoria,dicionarioDeProcessos,modo)
            print(str(clock) +":" +str(dicionarioDeProcessos),end="\n\n")
            ##print(dicionarioDeProcessos)
        #print("\n")
    if (clock in dicionarioDeSaida):
        #print("clock: " + str(clock))
        while (dicionarioDeSaida[clock]):
            processo = dicionarioDeSaida[clock].pop() #Remove e salva ultimo elemento da lista
            dicionarioDeProcessos = f.desalocaProcesso(processo,dicionarioDeProcessos)
        pass
    #Inserção de processo
    clock+=1