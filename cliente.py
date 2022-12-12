import socket
import os
import time

host = socket.gethostname()
porta = 1724

# Cria o socket
s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
try:
# Tenta se conectar ao servidor
    s.connect((host, porta))
except Exception as erro:
    print(str(erro))

print('Conexão efetuada com',host)

def tempo():  
    segundos = 10   
    while segundos:
        timer = '{:02d}'.format(segundos)
        print("Voltando para o menu em: ", timer, end="\r") 
        time.sleep(1)
        segundos -= 1

def menu():
    os.system('cls')
    print('888b     d888  .d8888b.  888b     d888  .d88888b.  8888888b.   .d8888b.  8888888888')
    print('8888b   d8888 d88P  Y88b 8888b   d8888 d88P" "Y88b 888   Y88b d88P  Y88b 888       ')
    print('88888b.d88888        888 88888b.d88888 888     888 888    888 Y88b.      888       ')
    print('888Y88888P888      .d88P 888Y88888P888 888     888 888   d88P  "Y888b.   8888888   ')
    print('888 Y888P 888  .od888P"  888 Y888P 888 888     888 8888888P"      "Y88b. 888       ')
    print('888  Y8P  888 d88P"      888  Y8P  888 888     888 888 T88b         "888 888       ')
    print('888   "   888 888"       888   "   888 Y88b. .d88P 888  T88b  Y88b  d88P 888       ')
    print('888       888 888888888  888       888  "Y88888P"  888   T88b  "Y8888P"  8888888888')
    print('')
    print('Escolha uma função:')
    print('')
    print('1 - TRADUTOR DE PORTUGÛES PARA MORSE')
    print('2 - TRADUTOR DE MORSE PARA PORTUGUES')
    print('0 - SAIR E FECHAR CONEXÃO')
    print('')

while True:
    menu()
    #Aguarda usuario digitar opção escolhida

    escolha = int(input('Digite o número da sua escolha: '))
    if escolha == 1:
        #Aguarda usuario digitar a sentença
        escolha = bytes(str(escolha), 'utf-8')
        s.sendall(escolha)
        frase = bytes(input('Digite a frase que deseja transformar em morse: '), 'utf-8')
        s.sendall(frase) #Envia frase pelo usuario
        info = s.recv(1024)
        print('A frase codificada em morse: ', info.decode('utf-8'))
        tempo()

    if escolha == 2:
        escolha = bytes(str(escolha), 'utf-8')
        s.sendall(escolha)
        frase = bytes(input('Digite o código morse que deseja transformar em português: '), 'utf-8')
        s.sendall(frase) #Envia morse pelo usuario
        info = s.recv(1024)
        print('A frase codificada em portugûes: ', info.decode('utf-8'))
        tempo()
    
    if escolha == 0:
        escolha = bytes(str(escolha), 'utf-8')
        s.sendall(escolha) #Envia opção escolhida pelo usuario
        break