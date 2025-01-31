# PD Downloader

O **PD Downloader** é um programa em Python que permite baixar documentos disponibilizados como imagens escaneadas no site PasseiDireto e consolidá-los em um único arquivo PDF, sem a necessidade da assinatura.

> **Nota:** Este programa é compatível apenas com documentos que são imagens escaneadas, não é possivel baixar texto.

## Requisitos
Certifique-se de ter o **Python 3** instalado.

Instale essas dependências com o comando:
```bash
pip install -r requirements.txt
```

## Como Executar
1. Abra o terminal ou prompt de comando e execute o programa com:
    ```bash
    python nome_do_arquivo.py 
    ```

2. Quando solicitado, informe a URL base antes da barra final (`/`). Exemplo:
    ```bash
    https://files.passeidireto.com/3f71f1d4-715a-460b-86d4-848957ad124a
    ```

3. Insira a quantidade total de páginas do documento.

4. O arquivo final será salvo como **ImagensFinal.pdf**.

## Aviso Legal
Este programa foi criado para fins educativos e acadêmicos. O uso desta ferramenta deve respeitar os termos de serviço dos sites acessados. A responsabilidade pelo uso é exclusivamente do usuário.

