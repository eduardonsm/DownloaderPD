import requests
print("--- Downloader PD ---\nValido apenas para arquivos escaneados ou que são imagens")
print("Exemplo: https://files.passeidireto.com/c7da1998-cecd-4b2f-b443-3854f2b67058/bg6b.png")
url_base = input("Informe o URL BASE (antes da /): ")
paginas = int(input("Informe a quantidade de paginas do seu documento: "))

for pagina in range(1,paginas+1):
    url = f"{url_base}/bg{format(pagina, 'x')}.png"
    print(url)
    if(requests.get(url) == "<Response [200]>"){

    }else{
        print("ERRO! Não é possivel conectar ao link gerado\n"+requests.get(url))
        break;
    }

# url = 'https://files.passeidireto.com/c7da1998-cecd-4b2f-b443-3854f2b67058/bg6b.png'
# response = requests.get(url)

# # Salvando o arquivo baixado
# with open('downloaded_image.png', 'wb') as file:
#     file.write(response.content)

# print("Download completo: downloaded_image.png")
