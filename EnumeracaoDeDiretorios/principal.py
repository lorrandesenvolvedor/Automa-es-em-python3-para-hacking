""" o'que irei mostrar a vocês e a forma em python 3.11 que podemos desenvolver uma automação simples para listar possíveis diretórios e subdomínios em um site. para isso armazenamos no arquivo chamado (diretorios.txt) todos os caminhos que desejamos que ele verifique e depôs codamos a lógica."""

import httpx # biblioteca responsável pela requisição 

def Programa_dir(): # cria a função
    site = ("https://alvoAqui/") # URL 
    with open('diretorios.txt', 'r', encoding='utf-8') as diretorios: # caminho do arquivo (já deixei um criado)
        diretorio_lista = diretorios.read().splitlines()
    for diretorio in diretorio_lista:
        try: # espera por um erro 
            site_positivo = (f"{site}{diretorio}") # gera a URL que será imprimida para o usuário 
            requisicao = httpx.get(f"{site}{diretorio}") # gera a URL para a requisição 
            if requisicao.status_code == 200: # faz a requisição e verifica a resposta de cada tentativa (fiz um exemplo simples com alguns tipos de respostas)
                print (f"encontrado {site_positivo}")
            elif requisicao.status_code == 301:
                print (f" diretorio mudou de endereço {site_positivo}")
            elif requisicao.status_code == 202:
                print (f" a requisição não foi 100% concluída {site_positivo}")
            elif requisicao.status_code == 204:
                print (f"direito vazio {site_positivo}")
            elif requisicao.status_code == 403:
                print (f" requisição bloqueada {site_positivo}")
        except Exception as e: # exibe o erro 
            print (f"erro --> {e}")

Programa_dir() # fecha a função 

#_________________________________________________________________________________________________________
""" isto e apenas para uso educativo, não pretendo prejudicar ninguém compartilhando esse conhecimento, estou apenas mostrando como o python pode ser usado no hacking e compartilhando ideias de projetos com programadores iniciantes assim como eu."""
