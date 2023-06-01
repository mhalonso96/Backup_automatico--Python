import os
import shutil
from time import sleep
from countdown import *
from path_generator import *
try:

    path = path_generator()
    caminho_arquivo = path[0]
    caminho_backup_arquivo = path[1]
    arquivos = os.listdir(caminho_arquivo)
    if len(arquivos) > 0:
    
        for arquivo in arquivos:
            caminho_origem = os.path.join(caminho_arquivo, arquivo)
            caminho_destino = os.path.join(caminho_backup_arquivo, arquivo)
            shutil.copy2(caminho_origem, caminho_destino)
            os.remove(caminho_origem)
            print('arquivo copiado', arquivo)
            sleep(1)
        print('Backup realizado com sucesso!!')
        print(countdown(5))
    else:
        print('Diretório esta vazio')
        print(countdown(5))
    
except Exception as error:
    print('Houve um erro, aplicativo sendo finalizado')
    print ('EXCEPTION:', error)
    print(countdown(5))


    