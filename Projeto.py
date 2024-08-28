"""
As seguintes funções procuram identificar e corrigir corrupções que ocorreram
numa base de dados (Buggy Data Base, BDB). Esta base de dados contém a
informação de autenticação de utilizadores, estando a recusar o acesso a
alguns utilizadores erradamente.
Assim, desenvolvi funções que corrigissem os documentos, que descubra
o PIN da base de dados, verifique a coerência de dados, desencripte o conteúdo
e depure as senhas.

Autor:Daniel Carvalho
Última atualização:22/10/2021

"""

#1.2.1-corrigir o surto de erros numa palavra
def corrigir_palavra(cdc): #recebe uma cadeia de caracteres
    """
    Esta funcao retira os pares de surto 
    da mesma letra (minuscula/maiscula ou
    vice-versa)
    
    Ao transformar a cadeia numa lista, tornou-se possível fazer a verificação 
    em elementos da lista consecutivos com as mesmas letras, apresentadas de
    forma minúscula/maíuscula ou vice/versa, retirando o mesmo par, 
    se acontecer,a partir da função imbutida del(), devolvendo no final 
    a cadeia de caracteres corrigida.
    
    Esta função recebe uma cadeia de carecteres com ou sem surto, 
    faz a sua verificação e remoção dos surtos
    se existir, procedendo a devolver uma cadeia de caracteres corrigida
    (corrigir palavra: cad. carateres → cad. carateres)
    """
    lista=list(cdc)
    count=len(lista)-1
    while count>=0:
        if abs(ord(lista[count])-ord(lista[count-1]))==32: 
        #verificação se ocorreu o surto da mesma letra
            del (lista[count])
            del(lista[count-1])
            count=len(lista) #renovação do comprimento da lista
        count-=1
    res=""
    for letra in lista: #cadeia de caracteres corrigida
        res+=letra
    return res

#1.2.2-verificação de anagramas

def eh_anagrama(cdc1,cdc2):
    """
    Esta funcao verifica se duas palavras são anagramas
    (diferentes de si próprio).
    
    A primeira cadeia recebida será a palavra "principal" 
    enquanto a segunda será o possível anagrama. 
    Esta função altera, primeiramente, todas as letras da cadeia em minúsculas, 
    procedendo a verificar se são iguais. Senão transformasse
    depois essas cadeias em listas, que são ordenadas de 
    acordo com a sua posição em UTF-8, sendo anagramas 
    se as duas listas ordenadas são iguais.
    
    Esta função recebe duas cadeias de caracteres, 
    uma "principal" e o possível anagrama,
    devolvendo um valor booleano se for ou não anagrama. 
    (eh_anagrama:carateres × cad. carateres → booleano)
    """    
    lista1=list(cdc1.lower())
    lista2=list(cdc2.lower())
    if lista1==lista2:#verificação se as palavras são iguais inicialmente
        return True
    lista1.sort()
    #ordena-se ambas as listas e verifica-se se são iguais
    lista2.sort()
    return lista1==lista2

#1.2.3-correção do documento

def corrigir_doc(cdc):
    """
    Esta função recebe uma cadeia de carateres que representa o texto 
    com erros da documentação da BDB e devolve 
    a cadeia de carateres filtrada com as palavras corrigidas e os
    anagramas retirados, ficando apenas a sua primeira ocorrência.
    
    Primeiro, é corrigido as palavras deste documento, seguido pela retiração
    da existência de anagramas,se ocorrerem, utilizando uma lista
    de forma a dividir uma frase em que as palavras se encontram separadas
    por um espaço.
    
    Esta função recebe uma cadeia de carecteres, devolvendo novamente
    uma cadeia de carcateres corrigida 
    
    (corrigir_doc:cad. carateres → cad. carateres)
    """
    res=""
    if type(cdc)!=str or cdc=="":
        raise ValueError("corrigir_doc: argumento invalido")
    lista=cdc.split(" ")#separação das palavras separadas por um espaço
    if " " in lista or lista==[]:
    #verificação se a cadeia de caracteres era vazia 
    #ou palavras estavam separadas por dois ou mais espaços
        raise ValueError("corrigir_doc: argumento invalido")
    for i in range(len(lista)-1,-1,-1):
        for caracteres in lista[i]: 
            #verificação de caracteres na lista para além de letras
            if ord(caracteres)<65 or ord(caracteres)>122 or\
               (ord(caracteres)>90 and ord(caracteres)<97):
                raise ValueError("corrigir_doc: argumento invalido")
        lista[i]=corrigir_palavra(lista[i])#filtração e correção das palavras
    alterado=True
    while alterado: #ciclo que ocorre desde que exista alteração
        comp1=len(lista)
        alterado=False
        for j in range(comp1-1):
            if alterado==True:
                break
            for k in range(j+1,comp1): 
            #verificacão se as palavras em posições seguintes 
            #a palavra de indice j são anagramas dessa
                if eh_anagrama(lista[j],lista[k])==True \
                   and lista[j].lower() !=lista[k].lower():
                    #verificação se são anagramas e não são iguais
                    del (lista[k])
                    alterado=True
                    break
    comp2=len(lista) #comprimento da lista sem anagramas e filtrada
    for el in range(comp2): #construção da string
        if el==comp2-1:
            res+=lista[el]
        else:
            res+=lista[el]+" "
    return res

#2.2.1-obtém-se a posição após um movimento
def obter_posicao(caracter,posicao):
    """
    Esta funçãao recebe uma cadeia de caracteres contendo 
    apenas um caráter que representa
    a direçãao de um único movimento (‘C’, ‘B’, ‘E’ ou ‘D’) e 
    um inteiro representando a
    posição atual (1, 2, 3, 4, 5, 6, 7, 8 ou 9); e 
    devolve o inteiro que corresponde à nova
    posição após do movimento.
    
    Esta função recebe uma letra  (‘C’, ‘B’, ‘E’ ou ‘D’), a posição atual
    e move-se de acordo com a letra correspondente, obtendo ou mantendo 
    uma posição (1, 2, 3, 4, 5, 6, 7, 8 ou 9).
    (obter_posicao:carateres × inteiro → inteiro)
    """
    if caracter=="C":
        if posicao==1 or posicao==2 or posicao==3:
        #não "desce" se estiver na última linha
            posicao=posicao
        else:
            posicao-=3
    elif caracter=="B":
        if posicao==7 or posicao==8 or posicao==9:
        #não "sobe" se estiver na primeira linha
            posicao=posicao
        else:
            posicao+=3
    elif caracter=="E":
        if posicao==1 or posicao==4 or posicao==7:
        #não se "move" para a esquerda se estiver na primeira coluna
            posicao=posicao  
        else:
            posicao-=1
    elif caracter=="D":
        if posicao==3 or posicao==6 or posicao==9:
        #não se "move" para a direita se estiver na última coluna
            posicao=posicao 
        else:
            posicao+=1
    return posicao

#2.2.2-obtém-se a posição após uma sequÊncia de movimentos
def obter_digito (cdc,posicao):
    """
    Esta função recebe uma cadeia de carateres contendo uma sequência de 
    um ou mais movimentos e um inteiro representando a posição inicial; 
    e devolve o inteiro que corresponde
    ao dígito a marcar após finalizar todos os movimentos.
    
    Percorre-se a cadeia de caracteres inteiramente e, utilizando a
    função obter_posicao, permite determinar a posição final após uma sequência 
    de 1 ou mais movimentos.
    (obter_digito:carateres × inteiro → inteiro)
    """
    for caracter in cdc: #percorre-se a lista de caracteres inteira
        posicao=obter_posicao(caracter,posicao)
    return posicao

#2.2.3-obtém-se um pin a partir de 4 a 10 sequencias
def obter_pin(tuplo):
    """
    Esta função recebe um tuplo contendo entre 4 e 10 
    sequências de movimentos e devolve
    o tuplo de inteiros que contêm o pin codificado 
    de acordo com o tuplo de movimentos.
    
    Esta função valida se um tuplo possui entre 4 a 10 elementos,
    sendo esses elementos compostos por "D","C","E" ou "B". O primeiro
    dígito a ser determinado tem como posição incial o 5, sendo as posições
    iniciais consecutivas as finais do digito anterior.
    
    (obter_pin:tuplo → tuplo)
    """
    
    if type(tuplo)!=tuple:
        raise ValueError ("obter_pin: argumento invalido")
    comp=len(tuplo)
    if comp<4 or comp>10:
        raise ValueError ("obter_pin: argumento invalido")    
    tuplo_res=()
    for el in range(comp):
        if type(tuplo[el])!=str or tuplo[el]=="":
            raise ValueError ("obter_pin: argumento invalido")   
        for ind in range(len(tuplo[el])):
            if tuplo[el][ind] not in "BCDE":
                raise ValueError ("obter_pin: argumento invalido")
        if tuplo[el]==tuplo[0]:#sequência do primeiro digito
            posicao=obter_digito(tuplo[el],5)
            tuplo_res+=(posicao,)#criação do tuplo correpondente ao PIN
        else:#dígitos restantes
            posicao=obter_digito(tuplo[el],posicao)
            tuplo_res+=(posicao,)#criação do tuplo correpondente ao PIN
    return tuplo_res

#3.2.1 e 4.2.1-verificação dos dados de entrada

def eh_entrada(entrada):
    """
    Esta função recebe um argumento de qualquer tipo e
    devolve True se e só se o seu 
    argumento corresponde a uma entrada da BDB 
    (potencialmente corrupta) conforme
    descrito, isto é, um tuplo com 3 campos: uma cifra, 
    uma sequência de controlo e uma sequência de segurança.
    
    Primeiro,se a entrada é correta, ou seja,
    um tuplo de comprimento 3 e verifica-se se os 
    caracteres pertencentes à cifra bem como a
    sequência de controlo são os corretos.
    
    (eh entrada: universal → booleano) 
    """
    verificacao_cifra="abcdefghijklmnopqrstuvwxyz-"
    verificacao_seq_con="[]abcdefghijklmnopqrstuvwxyz"
    if type(entrada)==tuple and len(entrada)==3:
        if isinstance(entrada[0],str) and isinstance(entrada[1],str)\
           and isinstance(entrada[2],tuple):
            lista_cifra=entrada[0].split("-")#separação das sequências em"-"
            for car1 in entrada[0]:
                if car1 not in verificacao_cifra:
                #verificação dos elementos na cifra
                    return False
            for car2 in lista_cifra: 
            #verificação de " " ou "-" em excesso na cifra
                if car2=="" or car2=="-":
                    return False
            if len(entrada[1])==7 and entrada[1].count("[")==1\
               and entrada[1].count("]")==1: 
                #verificação da existência de uma sequência de controlo de
                #comprimento igual a 7 e apenas com um parênteses reto de 
                #cada tipo
                for car3 in entrada[1]:
                    if car3 not in verificacao_seq_con:
                    #verificação dos elementos na sequência de controlo
                        return False
            else:
                return False
            comp=len(entrada[2]) #sequÊncia de segurança
            if comp<2:
                return False
            for el in entrada[2]:
                if type(el)!=int or el<=0:
                    return False
            return True
        return False
    return False

#3.2.2-coerência entre cifra e a sequência de controlo
def validar_cifra(cifra,seq_controlo):
    """
    Esta função recebe uma cadeia de carateres contendo uma cifra 
    e uma outra cadeia de carateres contendo uma sequência de controlo, 
    e devolve True se e só se a sequência de
    controlo é coerente com a cifra conforme descrito.
    
    Primeiro, para as letras da cifra, adiciona-se a uma lista um tuplo 
    com a letra,seguida por o seu número de aparições 
    na cadeia de caracteres, e uma lista para as letras e 
    outra para o número de aparições. Coloca-se em ordem alfabética a lista com,
    tuplos. Numa lista, com os caracteres e os seus número de
    aparições, indo buscar à lista com o húmero de aparições, os 5 cinco
    maiores número, adicionando a respetiva letra à resposta e retirando da
    lista com as sublistas essa letra e número de aparições correspondente.
    Finalmente, verifica-se se a sequência de controlo construída é igual
    à dada.
    
    (validar cifra: cad. carateres × cad. carateres → booleano)
    """
    lista_inicial=[]
    lista_count=[]
    lista_caracteres=[]
    lista_verificacao=[]
    num_seq_controlo="["
    for car in cifra:
        if ord(car)>96 and ord(car)<123: #aplica-se nas letras 
            if car not in lista_verificacao:
                lista_inicial.append((car,cifra.count(car)))
                #lista com tuplos da letra seguida por o nº de aparições
                lista_verificacao.append(car)
                #lista com as letras
                lista_count.append(cifra.count(car))
                #lista com o nº de aparições
    lista_inicial.sort()#ordem alfabética
    i=0
    for i in range(len(lista_inicial)): 
        #criação de uma lista nova em vez de tuplos
        lista_caracteres=lista_caracteres\
            +[lista_inicial[i][0],lista_inicial[i][1]]
    lista_count.sort() #de forma crescente
    lista_count.reverse()#de forma decrescente
    for num in lista_count[:5]:#seleciona os 5 maiores ou iguais números
        j=lista_caracteres.index(num)
        num_seq_controlo+=lista_caracteres[j-1]
        lista_caracteres=lista_caracteres[:j-1]+\
            lista_caracteres[j+1:]
        #permite escolher e remover a letra e o nº de aparições
        #se igual, escolhe por ordem alfabética
    return (num_seq_controlo + "]") ==seq_controlo

#3.2.3-validação das entradas não válidas
def filtrar_bdb(lista):
    """
    Esta função recebe uma lista contendo uma ou 
    mais entradas da BDB e devolve apenas
    a lista contendo as entradas em que o checksum não é 
    coerente com a cifra correspondente, na mesma ordem da lista original.
    
    Ao validar a cifra, se o resultado for "False", adicionaria-se a entrada
    ao resultado final.
    (filtrar bdb: lista → lista)
    """
    if type(lista)!=list or lista==[]:
        raise ValueError("filtrar_bdb: argumento invalido")    
    comp=len(lista)
    lista_res=[]
    for el in range(comp):
        if eh_entrada(lista[el])==False:
            raise ValueError("filtrar_bdb: argumento invalido")         
        elif eh_entrada(lista[el])==True \
             and validar_cifra(lista[el][0],lista[el][1])==False:
            #verificação de cifras não válidas
            lista_res=lista_res+[lista[el]]
    return lista_res

#4.2.2-cálculo do número de segurança
def obter_num_seguranca(tuplo):
    """
    Esta função recebe um tuplo de números inteiros positivos e 
    devolve o número de segurança conforme descrito, 
    isto é, a menor diferença positiva entre qualquer par de
    números.
    
    Cria-se uma lista com todas as subtrações possíveis com os números
    do tuplo, orden-se por ordem crescente e escreve-se o primeiro.
    (obter num seguranca: tuplo → inteiro)
    """
    comp=len(tuplo)
    lista=[]
    for i in range(comp-1):
        for j in range(i+1,comp):
            lista=lista+[abs(tuplo[i]-tuplo[j])] #todas as subtrações possíveis
    lista.sort()
    return lista[0]

#4.2.3-resolução da cifra
def decifrar_texto(cifra,num_seg):
    """
    Esta função recebe uma cadeia de carateres contendo uma 
    cifra e um número de segurança, 
    e devolve o texto decifrado conforme descrito.
    
    Visto que, dependendo do indíce da letra, o deslocamento difere,
    cria-se duas possibilidades de decifrar as letras. 
    (decifrar texto: cad. carateres × inteiro → cad. carateres)
    """
    comp=len(cifra)
    desloc_par=num_seg+1
    desloc_impar=num_seg-1
    res=""
    for car in range(comp):
        if cifra[car]=="-":
            res=res+" "
        elif car%2==0:
            res=res+chr(ord("a")+(ord(cifra[car])-ord("a")+desloc_par)%26)
        else:
            res=res+chr(ord("a")+(ord(cifra[car])-ord("a")+desloc_impar)%26)
    return res

#4.2.4-decifrar o documento
def decifrar_bdb(lista):
    """
    Esta função recebe uma lista contendo uma 
    ou mais entradas da BDB e devolve uma
    lista de igual tamanho, contendo o 
    texto das entradas decifradas na mesma ordem.
    
    A partir da função decifrar_texto, irá decifrar-se todos os elementos
    válidos, criando uma nova lista com o contúdo decifrado.
    (decifrar bdb: lista → lista)
    """
    if type(lista)!=list:
        raise ValueError("decifrar_bdb: argumento invalido")
    res=[]
    for el in lista:
        if eh_entrada(el)==False:
            raise ValueError("decifrar_bdb: argumento invalido")
        res=res+[decifrar_texto(el[0],obter_num_seguranca(el[2]))]
    return res

#5.2.1-verificação da informação relevante do utilizador
def eh_utilizador(entrada):
    """
    Esta função recebe um argumento de qualquer tipo e 
    devolve True se e só se o seu argumento corresponde a 
    um dicionário contendo a informação  de utilizador relevante
    da BDB conforme descrito, isto é, nome, senha e regra individual. 
    Considere para este efeito que nomes e senhas devem 
    ter tamanho mínimo 1 e podem conter qualquer caráter.
    
    (eh utilizador: universal → booleano)
    """
    if type(entrada)!=dict or len(entrada)!=3:
        return False
    lista_chaves=entrada.keys() #chaves: nome, senha e regra
    lista_chaves_regra=entrada["rule"].keys()#chaves das regras individuais
    if "name" not in lista_chaves or "pass" not in lista_chaves \
       or "rule" not in lista_chaves:
        return False
    if "vals" not in lista_chaves_regra or "char" not in lista_chaves_regra:
        return False
    if type(entrada["name"])!=str or len(entrada["name"])<1 or\
       type(entrada["pass"])!=str or len(entrada["pass"])<1 or\
       type(entrada["rule"]["vals"])!=tuple or\
       len(entrada["rule"]["vals"])<2 or type(entrada["rule"]["char"])!=str or\
       len(entrada["rule"]["char"])!=1:
    #verificação de tipos e comprimentos dos elementos do argumento de entrada
        return False
    if entrada["rule"]["vals"][0]>entrada["rule"]["vals"][1] or\
       entrada["rule"]["vals"][0]<=0 or entrada["rule"]["vals"][1]<=0:
    #verificação de argumentos das regras individuais
        return False
    else:
        return True

#5.2.2-validação das senhas
def eh_senha_valida(senha,regras):
    """
    Esta função recebe uma cadeia de carateres 
    correspondente a uma senha e um dicionário
    contendo a regra individual de criação da senha,
    e devolve True se e só se a senha cumpre
    com todas as regras de definição (gerais e individual) conforme descrito.
    
    Após verificar a validade dos argumkentos, verifica-se o número de vogais,
    bem como, o número de vezes em que letras se encontram seguidas
    (eh senha valida: cad. carateres × dicionário → booleano)
    """
    if type(senha)!=str or senha=="" or type(regras)!=dict or\
       len(regras)<2:
        return False
    if senha.count(regras["char"])<regras["vals"][0] or\
       senha.count(regras["char"])>regras["vals"][1]:
        #verifica se o nº de aparições desse carater está fora dos limites
        return False
    vogais=0
    for el in senha:
        if el in "aeiou": 
            vogais+=1
    if vogais<3: #verificação do número total de vogais
        return False
    comp=len(senha)-1
    consecutivas=0
    for i in range(comp):
        if senha[i]==senha[i+1]:#verificação de letras consecutivas
            consecutivas+=1
    if consecutivas<1:
        return False
    else:
        return True

#5.2.3-filtrar informações de utilizadores com senhas erradas
def filtrar_senhas(lista):
    """
    Esta função recebe uma lista contendo um ou mais dicionários 
    correspondentes às entradas da BDB como descritas anteriormente, 
    e devolve a lista ordenada alfabeticamente
    com os nomes dos utilizadores com senhas erradas.
    
    
    (filtrar senhas: lista → lista)
    """
    if type(lista)!=list or lista==[]:
        raise ValueError("filtrar_senhas: argumento invalido")
    lista_nomes=[]
    for el in lista:
        if eh_utilizador(el)==False:
            raise ValueError("filtrar_senhas: argumento invalido")
        if eh_senha_valida(el["pass"],el["rule"])==False:
            lista_nomes=lista_nomes+[el["name"]] 
            #utilizadores com senha errada
    lista_nomes.sort() #ordenação alfabética dos nomes
    return lista_nomes
                        
        
            
        
       
        

        
            
            
        
        
        
        
             
                        
        
                        
                
        
        
        
        
            

            
            
            
                
    
    
    
                
        
        
        
        
                
    
            
            
    
    
        

    
                
            
                


        
    
        




        
            
            
        


            
        
            
            
            
            
        
            
        
    
        
            
        
        