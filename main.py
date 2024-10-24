import requests
print("\n--- Downloader PD ---\nValido apenas para arquivos escaneados ou que são imagens")
# print("Exemplo: https://files.passeidireto.com/c7da1998-cecd-4b2f-b443-3854f2b67058/bg6b.png")
print("Exemplo: https://files.passeidireto.com/3f71f1d4-715a-460b-86d4-848957ad124a/bg4.png\n")
url_base = input("Informe o URL BASE (antes da /): ")
paginas = int(input("Informe a quantidade de paginas do seu documento: "))

for pagina in range(1,paginas+1):
    url = f"{url_base}/bg{format(pagina, 'x')}.png"
    print(url)
    response = requests.get(url)
    if str(response) == "<Response [200]>":
        with open(f'downloaded{pagina}.png', 'wb') as file:
            file.write(response.content)
    else:
        print("ERRO! Não é possivel conectar ao link gerado: "+str(response))
        break
    

print("PDF GERADO!")
