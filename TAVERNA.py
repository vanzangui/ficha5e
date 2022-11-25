from armadura import *
print('''
                                 ________________________
                                |                        |
                                |      BEM-VINDO!!!      |
                                |________________________|

          ''')


def TAVERNA():
    print('''Olá aventureiro, seja bem-vindo! É uma honra tê-lo conosco aqui na taverna.
Então quer dizer que você quer viver uma aventura é? ...Bom, veremos do que você é capaz hehehe''')

    print('''
Com qual raça você quer jogar?
(ANÃO / DRACONATO / ELFO / GNOMO / HALFLING / HUMANO / MEIO ELFO / MEIO ORC / TIEFLING)''')

    raça = input()


#except EOFError:
    char.raça = raça

    if raça == 'ANÃO':
        return final(anao())

    elif raça == 'ELFO':
        return final(elfo())

    elif raça == 'HUMANO':
        return final(humano())

    elif raça == 'GNOMO':
        return final(gnomo())

    elif raça == 'MEIO ELFO':
        return final(melf())

    elif raça == 'HALFLING':
        return final(hobbit())

    elif raça == 'DRACONATO':
        return final(drake())

    elif raça == 'TIEFLING':
        return final(tief())

    elif raça == 'MEIO ORC':
        return final(morc())
    else:
        TAVERNA()
# def FERREIRO():
 #   print('Certo '+char.nome+''' agora vamos escolher sua classe. Isso vai envolver determinar
# suas proficiências e sua vida inicial!
# Me diga, qual classe combina mais com você?''')
 #   classe = input()
  #  if classe == 'BARBARO':
   #     barbaro()
TAVERNA()