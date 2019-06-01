#encoding=utf-8
import math
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
    del dicionarioDeProcessos[processo]
    #Retorna dicionário atualizado
    return dicionarioDeProcessos

#Varre a memória de acordo com a eurística determinada, retornando qual será o processo anterior à nova inserção
def varreMemoria(dicionarioDeProcessos,tamanhoProcesso,modo):
    
   # print(tamanhoProcesso)
    if not (dicionarioDeProcessos):
        return "I","F"

    for i in dicionarioDeProcessos:
    
        if("I" in dicionarioDeProcessos[i]):
            processoAtual = i
            if(tamanhoProcesso <= dicionarioDeProcessos[i][0]):
                menorDistancia = dicionarioDeProcessos[i][0]
                maiorDistancia = dicionarioDeProcessos[i][0]
                if(modo == "first"):
                    return "I",processoAtual
            else:
                menorDistancia = float('inf')
                maiorDistancia = 0
                menorProcesso = "I"
                maiorProcesso = "I"
    processoSeguinte=dicionarioDeProcessos[processoAtual][3]

    while(processoSeguinte!="F"):
        distancia = dicionarioDeProcessos[processoSeguinte][0]-dicionarioDeProcessos[processoAtual][1]
        if ((modo == "first") and (tamanhoProcesso<=distancia)):
            return processoAtual,dicionarioDeProcessos[processoAtual][2]
        if ((distancia<menorDistancia) and (tamanhoProcesso<=distancia)):
            menorDistancia = distancia
            menorProcesso = processoAtual
        if ((distancia>maiorDistancia) and (tamanhoProcesso<=distancia)):
            maiorDistancia = distancia
            maiorProcesso = processoAtual
        processoAtual=processoSeguinte
        processoSeguinte= dicionarioDeProcessos[processoSeguinte][3] 
    if(modo=="worst"):
        try:
            return maiorProcesso,dicionarioDeProcessos[maiorProcesso][2]
        except:
            return maiorProcesso,"F"
    elif(modo=="best"):
            return menorProcesso,dicionarioDeProcessos[menorProcesso][2]

#Aloca processo no dicionário de processos
def alocarMemoria(processo,tamMemoria,dicionarioDeProcessos,modo):
    processoAnterior,processoPosterior = varreMemoria(dicionarioDeProcessos,tamanhos[processo],modo)
    print("Processo anterior: ")
    padrao = True
    if (processoPosterior != "F"):
        dicionarioDeProcessos[processoPosterior][2]=processo
    else:
        padrao=False
        try:
            posicao = dicionarioDeProcessos[processoAnterior][1]
        except:
            posicao = 0
    if (processoAnterior != "I"):
        dicionarioDeProcessos[processoAnterior][3]=processo
    else:
        padrao=False
        posicao = 0
    if(padrao==True):
        posicao = dicionarioDeProcessos[processoAnterior][1]

    dicionarioDeProcessos[processo]=[posicao,posicao+tamanhos[processo],processoAnterior,processoPosterior]
    
    
    
    return dicionarioDeProcessos