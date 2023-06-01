def path_generator():

    with open('config.txt') as f:
        print('Acessando o arquivo "config.txt"')
        contents = f.readlines()
        contents = [content.rstrip('\n').rsplit('=') for content in contents]
        origem_arquivo = contents[0][1].strip()
        destino_arquivo = contents[1][1].strip()
    print('OS PATH FORAM GERADOS ........ AGUARDE')
    print('ORIGEM: ',origem_arquivo)
    print('DESTINO: ',destino_arquivo)
    return origem_arquivo, destino_arquivo
