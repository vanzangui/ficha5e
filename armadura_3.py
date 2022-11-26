from random import randint
from pdf import escriba


class Personagem:
    def __init__(self,nome,raca,atributos,pv):
        self.nome = nome
        self.raca = raca
        self.atributos = atributos
        self.pv = pv


char = Personagem('nome','raça','atributos','pv')

def dados():
    ATR = []
    dados = []
    while len(ATR) < 6:
        dados = [randint(1,6),randint(1,6),randint(1,6),randint(1,6)]
        list.sort(dados)
        list.reverse(dados)
        list.pop(dados)
        ATR.append(dados[0]+dados[1]+dados[2])
    return ATR

def dadosDeAtributo():
    ATR = dados()
    while ATR[0]+ATR[1]+ATR[2]+ATR[3]+ATR[4]+ATR[5] > 80 or ATR[0]+ATR[1]+ATR[2]+ATR[3]+ATR[4]+ATR[5] < 70:
        ATR = dados()
    return ATR


def escolha():
    print('''
Vamos lá, você quer usar os valores prontos (1) ou quer rolar seus valores de atributo (2)?''')
    modo = input()
    if modo == '1':
        ATRT = []
        ATR = [15,14,13,12,10,8]
        print(ATR)
        print('''
Esses serão os valores que você poderá alocar, ok?
Vamos alocar os atributos de acordo com a ordem da ficha
Sendo assim, vamos começar com Força. Qual valor você quer para esse atributo?''')
        forc = input()
        ATRT.append(int(forc))
        ATR.remove(int(forc))
        print('''
Ok, agora escolha um valor para Destreza''')
        print(ATR)
        des = input()
        ATRT.append(int(des))
        ATR.remove(int(des))
        print('''
Agora um para Constituição''')
        print(ATR)
        con = input()
        ATRT.append(int(con))
        ATR.remove(int(con))
        print('''
Escolha um para sua Inteligência''')
        print(ATR)
        inte = input()
        ATRT.append(int(inte))
        ATR.remove(int(inte))
        print('''
Falta pouco! Qual valor para Sabedoria você quer?''')
        print(ATR)
        sab = input()
        ATRT.append(int(sab))
        ATR.remove(int(sab))
        print('O último valor que sobrou, {}, será seu valor de carisma!'.format(ATR[0]))
        ATRT.append(ATR[0])
        
        return ATRT

    elif modo == '2':
        ATRT = []
        ATR = dadosDeAtributo()
        print(ATR)
        reroll = input('''Você gostou dos dados?
(S/N)''').upper()
        while reroll == 'N':
            ATR = dadosDeAtributo()
            print(ATR)
            reroll = input('''Você gostou dos dados?
(S/N)''').upper()
            if reroll == 'S':
                break
             
                
        print('''
Beleza, esses são seus dados:''')
        print(ATR)
        print('''Vamos alocar os atributos de acordo com a ordem da ficha, ok?
Sendo assim, vamos começar com Força. Qual valor você quer para esse atributo?''')
        forc = input()
        ATRT.append(int(forc))
        ATR.remove(int(forc))
        print('Ok, agora escolha um valor para Destreza')
        print(ATR)
        des = input()
        ATRT.append(int(des))
        ATR.remove(int(des))
        print('Agora um para Constituição')
        print(ATR)
        con = input()
        ATRT.append(int(con))
        ATR.remove(int(con))
        print('Escolha um para sua Inteligência')
        print(ATR)
        inte = input()
        ATRT.append(int(inte))
        ATR.remove(int(inte))
        print('Falta pouco! Qual valor para Sabedoria você quer?')
        print(ATR)
        sab = input()
        ATRT.append(int(sab))
        ATR.remove(int(sab))
        print('O último valor que sobrou, {}, será seu valor de carisma!'.format(ATR[0]))
        ATRT.append(ATR[0])

        return ATRT


def final(ATRT,raça):
    print('Qual será o nome do seu aventureiro(a)?')
    nome = input()
    char.nome = nome
    char.atributos = ATRT
    print('Ok, {}, seus valores de atributo são:'.format(nome[0].upper()+nome[1:]))
    print('{} de Força'.format(ATRT[0]))
    print('{} de Destreza'.format(ATRT[1]))
    print('{} de Constituição'.format(ATRT[2]))
    print('{} de Inteligência'.format(ATRT[3]))
    print('{} de Sabedoria'.format(ATRT[4]))
    print('{} de Carisma'.format(ATRT[5]))
    escriba(nome,ATRT,raça)

def anao():
    char.raça = 'Anão'
    ATRT = escolha()
    ATRT[2]=ATRT[2]+2   
    print('Você é um anão das montanhas (1) ou das colinas (2)?')
    print('(1/2)')
    subraça = input()

    if subraça == '1':
        ATRT[0]=ATRT[0]+2
        return ATRT

    elif subraça == '2':
        ATRT[4]=ATRT[4]+1
        return ATRT


def elfo():
    ATRT = escolha()
    ATRT[1]=ATRT[1]+2
    print('você é um elfo(a) alto(a) (1), das florestas (2) ou negr(a) (3)?')
    print('(1/2/3)')
    subraça = input()
    if subraça == '1':
        ATRT[3]=ATRT[3]+1
        return ATRT

    elif subraça == '2':
        ATRT[4]=ATRT[4]+1
        return ATRT

    elif subraça == '3':
        ATRT[5]=ATRT[5]+1
        return ATRT


def humano():
    print('''você quer usar as regras de humano variante?
    (S/N)''')
    subraça = input().upper()
    if subraça == 'N':
        #+1 em todos os atr
        ATRT = escolha()
        for n in range(0,6):
            ATRT[n] = ATRT[n]+1
        return ATRT

    elif subraça == 'S':
        ATRT = escolha()
        ATRHV = ['FOR','DES','CON','INT','SAB','CAR']
        print(ATRT)
        print(' ')
        print(ATRHV)
        decisao = input('''Escolha dois atributos para aprimorar:
(exemplo: For e Car)

''')
        AT1 = decisao[0:3].upper()
        AT2 = decisao[6:9].upper()
        if AT1 == AT2:
            return None
        else:
            while AT1 in ATRHV:
                ATRT[ATRHV.index(AT1)] = ATRT[ATRHV.index(AT1)]+1
                break
            while AT2 in ATRHV:
                ATRT[ATRHV.index(AT2)] = ATRT[ATRHV.index(AT2)]+1
                break
            return ATRT

def melf():
    ATRT = escolha()
    ATRT[5] = ATRT[5]+2
    ATRME = ['FOR','DES','CON','INT','SAB']
    print(ATRT)
    print('')
    print(ATRME)
    decisao = input('''Escolha dois atributos para aprimorar, lembrando que não pode ser carisma!
(exemplo: For e Sab)

''')          
    AT1 = decisao[0:3].upper()
    AT2 = decisao[6:9].upper()
    if AT1 == AT2:
        return None
    elif 'CAR' == AT1 or AT2:
        return None
    else:
        while AT1 in ATRME:
            ATRT[ATRME.index(AT1)] = ATRT[ATRME.index(AT1)]+1
            break
        while AT2 in ATRME:
            ATRT[ATRME.index(AT2)] = ATRT[ATRME.index(AT2)]+1
            break
        return ATRT
    
def gnomo():
    ATRT = escolha()
    ATRT.insert(3,ATRT.pop(3)+2)
    print('''Você é um Gnomo da floresta (1) ou das rochas (2)?
(1/2)''')
    subraça=input()
    if subraça == '1':
        ATRT[1]=ATRT[1]+1
        return ATRT
    elif subraça == '2':
        ATRT[2]=ATRT[2]+1
        return ATRT

def hobbit():
    ATRT = escolha()
    ATRT[1]=ATRT[1]+2
    print('''Você é um halfling robusto (1) ou dos pés ligeiros (2)?
(1/2)''')
    subraça=input()
    if subraça == '1':
       ATRT[2]=ATRT[2]+1
       return ATRT

    elif subraça == '2':
       ATRT[5]=ATRT[5]+1
       return ATRT

def drake():
    ATRT = escolha()
    ATRT[0]=ATRT[0]+2
    ATRT[5]=ATRT[5]+1
    return ATRT

def tief():
    ATRT = escolha()
    ATRT[3]=ATRT[3]+1
    ATRT[5]=ATRT[5]+2
    return ATRT

def morc():
    ATRT = escolha()
    ATRT[0]=ATRT[0]+2
    ATRT[2]=ATRT[2]+1
    return ATRT

def barbaro():
    char.pv = (char.atributos[2]-10)/2
    return char.pv
