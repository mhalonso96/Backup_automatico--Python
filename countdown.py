import time

def countdown(segundos):

    for i in range(segundos):
        segundos = segundos-1
        time.sleep(1)
        print('Aplicação sendo finalizada em ...', segundos + 1 ,' segundos')
    return print('Fechando ....')
     