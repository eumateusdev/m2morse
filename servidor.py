import socket

lista_caracteres = ['a','b','c','d','e','f','g','h','i','j','k',
                        'l','m','n','o','p','q','r','s','t','u','v',
                        'w','x','y','z',' ', '1','2','3','4','5','6',
                        '7','8','9','0','.',',','?','!','/','(',')',
                        ':',';','=','-','_']

lista_morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-',
                  '.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-',
                  '.--','-..-','-.--','--..','/','.----','..---','...--','....-','.....',
                  '-....','--...','---..','----.','-----','.-.-.-','--..--','..--..',
                  '-.-.--','-..-.','-.--.','-.--.-','---...','-.-.-.','-...-','-....-','..--.-']

# Cria o socket (TCP)
socket_servidor = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Obtem o nome da máquina
host = socket.gethostname()
porta = 1724
# Associa a porta
socket_servidor.bind((host, porta))
# Escutando...
socket_servidor.listen()
print("Servidor", host, "esperando conexão na porta", porta)
# Aceita alguma conexão
socket_cliente, addr = socket_servidor.accept()
print("Conectado a:", str(addr))

def codifica():
    
    frase = socket_cliente.recv(1024)
    frase =  frase.decode('utf-8')
    print('Frase recebida e decodificada!')

    frase = frase.lower()

    frase_lista = list(frase)

    j = len(lista_caracteres)
    k = len(frase_lista)

    frase_final = []

    for i in range(k):
        for l in range(j):
            if frase_lista[i] == lista_caracteres[l]:
                frase_final.append(lista_morse[l])
    
    print('Conversão em processo...')

    frase_final = ' '.join(map(str,frase_final))
    socket_cliente.sendall(bytes(frase_final, 'utf-8'))
    print('Frase enviada para o cliente! A frase gerada em morse foi:')
    print(frase_final)


def traduz():

    frase = socket_cliente.recv(1024)
    frase =  frase.decode('utf-8')
    print('Morse recebido e decodificada!')

    frase_lista = list(frase.split(' '))
    
    j = len(lista_morse)
    k = len(frase_lista)

    frase_final = []

    for i in range(k):
        for l in range(j):
            if frase_lista[i] == lista_morse[l]:
                frase_final.append(lista_caracteres[l])

    print('Tradução para português em processo...')
    frase_final = ''.join(map(str,frase_final))
    socket_cliente.sendall(bytes(frase_final, encoding='utf-8'))
    print('Frase enviada para o cliente! A frase traduzido para portugues foi:')
    print(frase_final)

while True:
    # Decodifica mensagem em UTF-8:
    try:
        escolha = socket_cliente.recv(1024)
        escolha =  escolha.decode('utf-8')
        print('Escolha recebida!')
        escolha = int(escolha)
    except Exception as err:
        break
    if(escolha == 0):
        print('Servidor desconectado!')
        socket_cliente.close()
        break
    else:
        if escolha == 1:
            codifica()
        if escolha == 2:
            traduz()