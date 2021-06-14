from pycep_correios import get_address_from_cep, WebService, exceptions
from os import system

# {'bairro': '', 'cep': '46165-000', 'cidade': 'Dom Basílio',
# 'logradouro': '', 'uf': 'BA', 'complemento': ''}

print("######################")
print("#Consulta CEP correio#")
print("######################")

# pegar input do usuario
cep_consultar = input("\nDigite um cep para ser consultado: ")

print("\nResultado: \n")  # mostrar o resultado abaixo

# tentar extrair o cep
try:
    lista_definicoes = ("bairro", "cep", "cidade", "logradouro", "uf",
                        "complemento")

    endereco_consultado = get_address_from_cep(
        cep=cep_consultar, webservice=WebService.APICEP
    )

    # printar o resultado da pesquisa
    for items in lista_definicoes:
        nome = "{}: {}".format(items.capitalize(),
                               endereco_consultado[items].strip())
        print(nome)


# erro cep invalido
except exceptions.InvalidCEP as eic:
    system("clear")
    print("Ocorreu um error: {}".format(eic))

# erro cep nao achado
except exceptions.CEPNotFound as ecnf:
    system("clear")
    print("Ocorreu um error: {}".format(ecnf))

# erro de conexão
except exceptions.ConnectionError as errc:
    system("clear")
    print("Ocorreu um error: {}".format(errc))

# erro de tempo de espera muito longo
except exceptions.Timeout as errt:
    system("clear")
    print("Ocorreu um error: {}".format(errt))


# erro http
except exceptions.HTTPError as errh:
    system("clear")
    print("Ocorreu um error: {}".format(errh))

# erro base
except exceptions.BaseException as e:
    system("clear")
    print("Ocorreu um error: {}".format(e))
