import requests
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

def generate_pdf(images):
    c = canvas.Canvas("ImagensFinal.pdf", pagesize=letter)
    width, height = letter
    for imagem_data in images:        
        c.drawImage(imagem_data, 0, 0,  width=width, height=height)
        c.showPage()
    c.save()

print("\n--- Downloader PD ---\nValido apenas para arquivos escaneados ou que são imagens")
# print("Exemplo: https://files.passeidireto.com/c7da1998-cecd-4b2f-b443-3854f2b67058/bg6b.png")
print("Exemplo: https://files.passeidireto.com/3f71f1d4-715a-460b-86d4-848957ad124a/bg4.png\n")
url_base = input("Informe o URL BASE (antes da /): ")
paginas = int(input("Informe a quantidade de paginas do seu documento: "))
imagens=[]

for pagina in range(1,paginas+1):
    url = f"{url_base}/bg{format(pagina, 'x')}.png"
    print(url)
    response = requests.get(url)
    if str(response) == "<Response [200]>":
        with open(f'downloaded{pagina}.png', 'wb') as file:
            file.write(response.content)
        imagens.append(f'downloaded{pagina}.png')

    else:
        print("ERRO! Não é possivel conectar ao link gerado: "+str(response))
        break
    
generate_pdf(imagens)

for image in imagens:
    os.remove(image)

print("PDF GERADO!")
