from armadura_3 import *



def aventura():
    print('''
                                 ________________________
                                |                        |
                                |      BEM-VINDO!!!      |
                                |________________________|

          ''')

    print('''Olá aventureiro, seja bem-vindo! É uma honra tê-lo conosco aqui na taverna.
Então quer dizer que você quer viver uma aventura é? ...Bom, veremos do que você é capaz hehehe''')

    print('''
Com qual raça você quer jogar?
(ANÃO / DRACONATO / ELFO / GNOMO / HALFLING / HUMANO / MEIO ELFO / MEIO ORC / TIEFLING)
(Para sair, digite exit)''')

    raça = input().upper()
    char.raça = raça

    if raça == 'ANÃO' or 'ANAO':
        raça = 'Anão'
        return final(anao(),raça)

    elif raça == 'ELFO':
        return final(elfo(),raça)

    elif raça == 'HUMANO':
        return final(humano(),raça)

    elif raça == 'GNOMO':
        return final(gnomo(),raça)

    elif raça == 'MEIO ELFO' or 'MEIOELFO' or 'MEIO-ELFO':
        return final(melf(),raça)

    elif raça == 'HALFLING' or 'HALF LING' or 'HALF-LING':
        return final(hobbit(),raça)

    elif raça == 'DRACONATO':
        return final(drake(),raça)

    elif raça == 'TIEFLING' or 'TIEF LING' or 'TIEF-LING':
        return final(tief(),raça)

    elif raça == 'MEIO ORC' or 'MEIO-ORC' or 'MEIOORC' or 'MEIORC':
        return final(morc(),raça)
    
    elif raça == "exit":
        return None

    else:
        print("Essa raça ainda não foi adicionada! Calma que logo logo ela tá por aqui, beleza?")
        aventura()
if __name__=='__main__':
	aventura()
# def FERREIRO():
 #   print('Certo '+char.nome+''' agora vamos escolher sua classe. Isso vai envolver determinar
# suas proficiências e sua vida inicial!
# Me diga, qual classe combina mais com você?''')
 #   classe = input()
  #  if classe == 'BARBARO':
   #     barbaro()
