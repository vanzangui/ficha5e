from random import *
#from pip import *

class Personagem:
    def __init__(self,nome,raca,atributos,pv):
        self.nome = nome
        self.raca = raca
        self.atributos = atributos
        self.pv = pv


char = Personagem('nome','raça','atributos','pv')


def dfor():
    dFOR = [randint(1,6),randint(1,6),randint(1,6),randint(1,6)]
    list.sort(dFOR)
    list.reverse(dFOR)
    list.pop(dFOR)
    FOR = dFOR[0]+dFOR[1]+dFOR[2]
    return FOR


def ddes():
    dDES = [randint(1,6),randint(1,6),randint(1,6),randint(1,6)]
    list.sort(dDES)
    list.reverse(dDES)
    list.pop(dDES)
    DES = dDES[0]+dDES[1]+dDES[2]
    return DES


def dcon():
    dCON = [randint(1,6),randint(1,6),randint(1,6),randint(1,6)]
    list.sort(dCON)
    list.reverse(dCON)
    list.pop(dCON)
    CON = dCON[0]+dCON[1]+dCON[2]
    return CON


def dint():
    dINT = [randint(1,6),randint(1,6),randint(1,6),randint(1,6)]
    list.sort(dINT)
    list.reverse(dINT)
    list.pop(dINT)
    INT = dINT[0]+dINT[1]+dINT[2]
    return INT


def dsab():
    dSAB = [randint(1,6),randint(1,6),randint(1,6),randint(1,6)]
    list.sort(dSAB)
    list.reverse(dSAB)
    list.pop(dSAB)
    SAB = dSAB[0]+dSAB[1]+dSAB[2]
    return SAB


def dcar():
    dCAR = [randint(1,6),randint(1,6),randint(1,6),randint(1,6)]
    list.sort(dCAR)
    list.reverse(dCAR)
    list.pop(dCAR)
    CAR = dCAR[0]+dCAR[1]+dCAR[2]
    return CAR


def dadosDeAtributo():
    ATR = [dfor(),ddes(),dcon(),dint(),dsab(),dcar()]

    while ATR[0]+ATR[1]+ATR[2]+ATR[3]+ATR[4]+ATR[5] > 80:

        ATR = [dfor(),ddes(),dcon(),dint(),dsab(),dcar()]
        print(ATR)
        return ATR

    while ATR[0]+ATR[1]+ATR[2]+ATR[3]+ATR[4]+ATR[5] < 70:

        ATR = [dfor(),ddes(),dcon(),dint(),dsab(),dcar()]
        print(ATR)
        return ATR

    print(ATR)
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
        print('''
O último valor que sobrou, '+str(+ATR[0])+', será seu valor de carisma!''')
        ATRT.append(ATR[0])
        
        return ATRT

    elif modo == '2':
        ATRT = []
        ATR = dadosDeAtributo()
        print('''Você gostou dos dados?
(SIM/NÃO)''')
        reroll = input()
        while reroll == 'NÃO':
            ATR=dadosDeAtributo()
            print('''Você gostou dos dados?
(SIM/NÃO)''')
            reroll = input()
             
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
        print('O último valor que sobrou, '+str(+ATR[0])+', será seu valor de carisma!')
        ATRT.append(ATR[0])

        return ATRT


def final(ATRT):
    print('Qual será o nome do seu aventureiro(a)?')
    nome = input()
    char.nome = nome
    char.atributos = ATRT
    print('Ok, '+nome+', seus valores de atributo são:')
    print(str(ATRT[0])+' de Força')
    print(str(ATRT[1])+' de Destreza')
    print(str(ATRT[2])+' de Constituição')
    print(str(ATRT[3])+' de Inteligência')
    print(str(ATRT[4])+' de Sabedoria')
    print(str(ATRT[5])+' de Carisma')
    

def anao():
    char.raça = 'Anão'
    ATRT = escolha()
    ATRT.insert(0,(ATRT.pop(0)+2))   
    print('Você é um anão das montanhas ou das colinas?')
    print('(MONTANHAS/COLINAS)')
    subraça = input()

    if subraça == 'MONTANHAS':
        ATRT.insert(2,(ATRT.pop(2)+2))
        return ATRT

    elif subraça == 'COLINAS':
        ATRT.insert(4,(ATRT.pop(4)+1))
        return ATRT


def elfo():
    ATRT = escolha()
    ATRT.insert(1,(ATRT.pop(1)+2))
    print('você é um elfo(a) alto, das florestas ou negro?')
    print('(ALTO/FLORESTAS/NEGRO)')
    subraça = input()
    if subraça == 'ALTO':
        ATRT.insert(3,(ATRT.pop(3)+1))
        return ATRT

    elif subraça == 'FLORESTAS':
        ATRT.insert(4,(ATRT.pop(4)+1))
        return ATRT

    elif subraça == 'NEGRO':
        ATRT.insert(5,(ATRT.pop(5)+1))
        return ATRT


def humano():
    print('''você quer usar as regras de humano variante?
(SIM/NÃO)''')
    subraça = input()
    if subraça == 'NÃO':
        #+1 em todos os atr
        ATRT = escolha()
        ATRT.insert(0,(ATRT.pop(0)+1))
        ATRT.insert(1,(ATRT.pop(1)+1))
        ATRT.insert(2,(ATRT.pop(2)+1))
        ATRT.insert(3,(ATRT.pop(3)+1))
        ATRT.insert(4,(ATRT.pop(4)+1))
        ATRT.insert(5,(ATRT.pop(5)+1))
        return ATRT

    elif subraça == 'SIM':
        ATRT = escolha()
        ATRHV = ['FOR','DES','CON','INT','SAB','CAR']
        print(ATRT)
        print('Qual atributo você gostaria de aprimorar primeiro?')
        print(ATRHV)
        pa = input()
        if pa == 'FOR':
            ATRHV.remove('FOR')
            ATRT.insert(0,(ATRT.pop(0)+1))

        elif pa == 'DES':
            ATRHV.remove('DES')
            ATRT.insert(1,(ATRT.pop(1)+1))

        elif pa == 'CON':
            ATRHV.remove('CON')
            ATRT.insert(2,(ATRT.pop(2)+1))

        elif pa == 'INT':
            ATRHV.remove('INT')
            ATRT.insert(3,(ATRT.pop(3)+1))

        elif pa == 'SAB':
            ATRHV.remove('SAB')
            ATRT.insert(4,(ATRT.pop(4)+1))

        elif pa == 'CAR':
            ATRHV.remove('CAR')
            ATRT.insert(5,(ATRT.pop(5)+1))

        print('Agora escolha outro atributo')
        print(ATRT)
        print(ATRHV)
        ps = input()
        if ps == pa:
            print('''Você já escolheu esse atributo! escolha um diferente
( ¯\_(ツ)_/¯ regras do jogo)''')
            print(ATRHV)
            print(ATRT)
            pt = input()
            if pt == 'FOR':
                ATRHV.remove('FOR')
                ATRT.insert(0,(ATRT.pop(0)+1))
                return ATRT

            elif pt == 'DES':
                ATRHV.remove('DES')
                ATRT.insert(1,(ATRT.pop(1)+1))
                return ATRT

            elif pt == 'CON':
                ATRHV.remove('CON')
                ATRT.insert(2,(ATRT.pop(2)+1))
                return ATRT

            elif pt == 'INT':
                ATRHV.remove('INT')
                ATRT.insert(3,(ATRT.pop(3)+1))
                return ATRT

            elif pt == 'SAB':
                ATRHV.remove('SAB')
                ATRT.insert(4,(ATRT.pop(4)+1))
                return ATRT

            elif pt == 'CAR':
                ATRHV.remove('CAR')
                ATRT.insert(5,(ATRT.pop(5)+1))
                return ATRT

        elif pa == 'FOR':
            ATRHV.remove('FOR')
            ATRT.insert(0,(ATRT.pop(0)+1))
            return ATRT

        elif pa == 'DES':
            ATRHV.remove('DES')
            ATRT.insert(1,(ATRT.pop(1)+1))
            return ATRT

        elif pa == 'CON':
            ATRHV.remove('CON')
            ATRT.insert(2,(ATRT.pop(2)+1))
            return ATRT

        elif pa == 'INT':
            ATRHV.remove('INT')
            ATRT.insert(3,(ATRT.pop(3)+1))
            return ATRT

        elif pa == 'SAB':
            ATRHV.remove('SAB')
            ATRT.insert(4,(ATRT.pop(4)+1))
            return ATRT

        elif pa == 'CAR':
            ATRHV.remove('CAR')
            ATRT.insert(5,(ATRT.pop(5)+1))
            return ATRT

def gnomo():
    ATRT = escolha()
    ATRT.insert(3,ATRT.pop(3)+2)
    print('''Você é um Gnomo da floresta ou das rochas?
(FLORESTA/ROCHA)''')
    subraça=input()
    if subraça == 'FLORESTA':
        #ATRT = escolha()
        #ATRT.insert(3,ATRT.pop(3)+2)
        ATRT.insert(1,(ATRT.pop(1)+1))
        return ATRT
    elif subraça == 'ROCHA':
        #ATRT = escolha()
        #ATRT.insert(3,ATRT.pop(3)+2)
        ATRT.insert(2,(ATRT.pop(2)+1))
        return ATRT
    
def melf():
    ATRT = escolha()
    ATRT.insert(5,ATRT.pop(5)+2)
    ATRME = ['FOR','DES','CON','INT','SAB']
    print(ATRT)
    print('Qual atributo você gostaria de aprimorar primeiro?')
    print(ATRME)
    pa = input()
    if pa == 'FOR':
        ATRME.remove('FOR')
        ATRT.insert(0,(ATRT.pop(0)+1))

    elif pa == 'DES':
        ATRME.remove('DES')
        ATRT.insert(1,(ATRT.pop(1)+1))

    elif pa == 'CON':
        ATRME.remove('CON')
        ATRT.insert(2,(ATRT.pop(2)+1))

    elif pa == 'INT':
        ATRME.remove('INT')
        ATRT.insert(3,(ATRT.pop(3)+1))

    elif pa == 'SAB':
        ATRME.remove('SAB')
        ATRT.insert(4,(ATRT.pop(4)+1))

    print('Agora escolha outro atributo')
    print(ATRT)
    print(ATRME)
    ps = input()
    if ps == pa:
        print('''Você já escolheu esse atributo! escolha um diferente
( ¯\_(ツ)_/¯ regras do jogo)''')
        print(ATRME)
        print(ATRT)
        pt = input()
        if pt == 'FOR':
            ATRME.remove('FOR')
            ATRT.insert(0,(ATRT.pop(0)+1))
            return ATRT

        elif pt == 'DES':
            ATRME.remove('DES')
            ATRT.insert(1,(ATRT.pop(1)+1))
            return ATRT

        elif pt == 'CON':
            ATRME.remove('CON')
            ATRT.insert(2,(ATRT.pop(2)+1))
            return ATRT

        elif pt == 'INT':
            ATRME.remove('INT')
            ATRT.insert(3,(ATRT.pop(3)+1))
            return ATRT

        elif pt == 'SAB':
            ATRME.remove('SAB')
            ATRT.insert(4,(ATRT.pop(4)+1))
            return ATRT

    elif pa == 'FOR':
        ATRME.remove('FOR')
        ATRT.insert(0,(ATRT.pop(0)+1))
        return ATRT

    elif pa == 'DES':
        ATRME.remove('DES')
        ATRT.insert(1,(ATRT.pop(1)+1))
        return ATRT

    elif pa == 'CON':
        ATRME.remove('CON')
        ATRT.insert(2,(ATRT.pop(2)+1))
        return ATRT

    elif pa == 'INT':
        ATRME.remove('INT')
        ATRT.insert(3,(ATRT.pop(3)+1))
        return ATRT

    elif pa == 'SAB':
        ATRME.remove('SAB')
        ATRT.insert(4,(ATRT.pop(4)+1))
        return ATRT

def hobbit():
    ATRT = escolha()
    ATRT.insert(1,(ATRT.pop(1)+2))
    print('''Você é um halfling robusto ou tem pés ligeiros?
(ROBUSTO/PÉS LEVES)''')
    subraça=input()
    if subraça == 'ROBUSTO':
       ATRT.insert(2,(ATRT.pop(2)+1))
       return ATRT

    elif subraça == 'PÉS LEVES':
       ATRT.insert(5,(ATRT.pop(5)+1))
       return ATRT

def drake():
    ATRT = escolha()
    ATRT.insert(0,(ATRT.pop(0)+2))
    ATRT.insert(5,(ATRT.pop(5)+1))
    return ATRT

def tief():
    ATRT = escolha()
    ATRT.insert(3,(ATRT.pop(3)+1))
    ATRT.insert(5,(ATRT.pop(5)+2))
    return ATRT

def morc():
    ATRT = escolha()
    ATRT.insert(0,(ATRT.pop(0)+2))
    ATRT.insert(2,(ATRT.pop(2)+1))
    return ATRT

def barbaro():
    char.pv = (char.atributos[2]-10)/2
    return char.pv
