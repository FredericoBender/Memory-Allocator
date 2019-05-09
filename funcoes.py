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

#Extrai valores do txt para criar as estruturas 
def interpreta(arquivo):
    arq = open(arquivo,"r")
    processos = arq.readlines()
    for i in range(len(processos)):
        processos[i] = processos[i].strip()
        processos[i] = processos[i].split(" ")
    for i in range(len(processos)):
        for j in range(len(processos[i])):
            processos[i][j] = int(processos[i][j]) 
    #lista de processos = [[int tamanho, int tempo de execução,int tempo de chegada],...]
    return processos

#Extrai valores da lista de processos para criar uma lista com os tamanhos de cada processo
def listaDeTamanhos(processos):
    global tamanhos
    tamanhos = []
    for i in processos:
        tamanhos.append(i[0])
    #lista de tamanho dos processos = [tamanho,...]

#Extrai valores da lista de processos para criar um dicionário com os tempos de entrada de cada processo
def dicionarioDeEntrada(processos):
    temposEntrada ={}
    processoAtual=0
    for i in processos:
        if (i[2] in temposEntrada):#processos[2] é tempo de chegada
            temposEntrada[i[2]].append(processoAtual)
        else:
            temposEntrada[i[2]]= [processoAtual]
        processoAtual+=1
    #dicionário com os tempos de entrada dos processos = {ciclo de entrada:nº do processo,...}
    return temposEntrada

#Extrai valores da lista de processos para criar um dicionário com os tempos de saída de cada processo
def dicionarioDeSaida(processos):
    temposSaida ={}
    processoAtual=0
    for i in processos:
        if ((i[1]+i[2]) in temposSaida):
            temposSaida[i[1]+i[2]].append(processoAtual)
        else:
            temposSaida[i[1]+i[2]]= [processoAtual]
        processoAtual+=1
    #dicionário com os tempos de saída dos processos = {ciclo de Saida:nº do processo,...}
    return temposSaida

#Desaloca processo do dicionário de processos
def desalocaProcesso(processo,dicionarioDeProcessos):
    anterior = dicionarioDeProcessos[processo][2]
    posterior = dicionarioDeProcessos[processo][3]
    try:
        dicionarioDeProcessos[anterior][3]=posterior
    except:
        pass
    try:
        dicionarioDeProcessos[posterior][2]=anterior
    except:
        pass
    dicionarioDeProcessos[processo].pop()
    #Retorna dicionário atualizado
    return dicionarioDeProcessos

#Aloca processo no dicionário de processos
def alocarMemoria(processo,dicionarioDeProcessos,modo):
    def firstFit(processo,dicionarioDeProcessos):
        pass
    def bestFit(processo, dicionarioDeProcessos):
        pass
    def worstFit(processo, dicionarioDeProcessos):
        pass
    if(modo==0):
        firstFit(processo,dicionarioDeProcessos)
    if(modo==1):
        bestFit(processo,dicionarioDeProcessos)
    if(modo==2):
        worstFit(processo,dicionarioDeProcessos)