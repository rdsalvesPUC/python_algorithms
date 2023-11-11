# +---------------------+
# |                     |
# |      A L P H A      |
# |                     |
# +---------------------+

import os
import time
import random
from ftplib import FTP

file_name = 'example.txt'                   # gerar um arquivo .txt

with open(file_name, 'w') as arquivo:
  arquivo.write('Código de 256 digitos')    # escrever conteudo dentro do arquivo


# Informações de conexão FTP
ftp_host = "ftp.example.com"  # Substitua pelo endereço do servidor FTP
ftp_user = "seu_usuario"      # Substitua pelo nome de usuário
ftp_passwd = "sua_senha"      # Substitua pela senha
remote_directory = "/diretorio/remoto/"  #

# salvar em uma pasta
# enviar o arquivo para um FTP