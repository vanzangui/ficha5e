from PyPDF2 import PdfReader, PdfWriter

def escriba(nome,ATRT,raça):
    reader = PdfReader('D&D5E - Ficha editável.pdf')
    writer = PdfWriter()

    page = reader.pages[0]
    fields = reader.getFields()

    writer.add_page(page)

    #atribuindo nome, raça e valores de atributo
    writer.update_page_form_field_values(
        writer.pages[0], {"Campo de Texto0":"{}".format(nome[0].upper()+nome[1:]),"Campo de Texto13":"{}".format(raça[0].upper()+raça[1:]),"Campo de Texto27": "{}".format(ATRT[0]),
        "Campo de Texto30": "{}".format(ATRT[1]),"Campo de Texto32": "{}".format(ATRT[2]),"Campo de Texto35": "{}".format(ATRT[3]),
        "Campo de Texto36": "{}".format(ATRT[4]),"Campo de Texto38": "{}".format(ATRT[5])})
    
    #modificadores de atributo
    #writer.update_page_form_field_values(
    #    writer.pages[0], {
    
    with open("ficha pronta2.pdf", "wb") as output_stream:
        writer.write(output_stream)