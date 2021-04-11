from pycep_correios import get_address_from_cep, WebService


pergunta = input('Digite seu cep:\n')
#VERIIFAR DADOS FORNECIDOS PELO USUARIO
valida_dados = len(pergunta)

while(valida_dados != 8):
    print('Cep incorrreto\n')
    pergunta = input('Digite seu cep novamente\n')
    valida_dados = len(pergunta)

