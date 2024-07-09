# -*- coding: utf8 -*-
import socket
import subprocess
from threading import Thread
from static.py.db import BancoDados

class Server:
    def __init__(self, server, port, host, user, password, database):
        # Inicialização do servidor com as configurações especificadas
        self.SERVER_ADDRESS = server
        self.SERVER_PORT = port
        self.binario = ["jpeg", "bmp", "png", "jpg", "ico"]
        self.texto = ["js", "html", "css", "map"]
        self.executavel = ["py", "php"]
        self.socket_servidor = None
        self.db = BancoDados("db")

    def responde(self, headers_get, socket_cliente):
        # Método para responder ao cliente com o cabeçalho e conteúdo apropriados
        cabecalho_resposta = b'HTTP/1.1 200 OK\r\n\r\n'
        corpo_resposta = headers_get.encode('utf-8')
        resposta_final = cabecalho_resposta + corpo_resposta
        socket_cliente.sendall(resposta_final)
        print(resposta_final.decode())
        return True
    
    def thread_func(self, socket_cliente, cliente_addr):
        # Função executada em cada thread para lidar com uma conexão de cliente
        print(f'cliente conectado com sucesso.{cliente_addr[0]}:{cliente_addr[1]}')
        dado_recebido = socket_cliente.recv(4096)
        dado_recebido = dado_recebido.decode()
        headers = dado_recebido.split('\r\n')
        headers_get = headers[0]

        try:
            # Analisa o cabeçalho para obter o arquivo solicitado
            arquivo_solicitado = headers_get.split(' ')[1][1:]
            extencao = arquivo_solicitado.split('.')[-1]
            if extencao in self.executavel:
                ex = None
            elif extencao in self.binario:
                ex = True
            elif extencao in self.texto:
                ex = False
            else:
                print("Arquivo recebido: " + arquivo_solicitado)
                return self.responde(headers_get, socket_cliente)
        except IndexError:
            print("Arquivo recebido: " + headers_get)
            return self.responde(headers_get, socket_cliente)

        try:
            # Abre o arquivo solicitado ou executa um script, dependendo da extensão
            if ex == True:
                file = open("static/src/"+arquivo_solicitado,'rb')
            elif ex == False:
                if extencao == "html":
                    file = open("templates/"+ arquivo_solicitado,'r',encoding='utf-8')
                elif extencao == "map":
                    extencao = arquivo_solicitado.split('.')[-2]
                    file = open("static/" + extencao +"/"+ arquivo_solicitado,'r',encoding='utf-8')
                else:
                    file = open("static/" + extencao +"/"+ arquivo_solicitado,'r',encoding='utf-8')
            else:
                if extencao == "py":
                    processo = subprocess.Popen(['python',"static/py/"+arquivo_solicitado],stdout = subprocess.PIPE) 
                elif extencao == "php":
                    processo = subprocess.Popen(['php',"static/php/"+arquivo_solicitado],stdout = subprocess.PIPE)
                else:
                    print(f'Arquivo ({arquivo_solicitado}) não exite.')
                    socket_cliente.sendall(b'HTTP/1.1 404 File not found\r\n\r\nFound file not found')
                    socket_cliente.close()
                    return False 
                stdout = processo.stdout.read()
                socket_cliente.sendall(b'HTTP/1.1 200 OK\r\n\r\n' + stdout)
                return True
            conteudo_arquivo = file.read()
        except FileNotFoundError:
            print(f'Arquivo ({arquivo_solicitado}) não exite.')
            socket_cliente.sendall(b'HTTP/1.1 404 File not found\r\n\r\nFound file not found')
            socket_cliente.close()
            return False
        
        # Envia a resposta ao cliente
        if ex:
            cabecalho_resposta =  b'HTTP/1.1 200 OK\r\n\r\n'
            corpo_resposta = conteudo_arquivo
            resposta_final = cabecalho_resposta + corpo_resposta
            socket_cliente.sendall(resposta_final)
        else:
            cabecalho_resposta =  f'HTTP/1.1 200 OK\r\n\r\n'
            corpo_resposta = conteudo_arquivo
            resposta_final = cabecalho_resposta + corpo_resposta
            socket_cliente.sendall(resposta_final.encode('utf-8'))

        socket_cliente.close()

    def cria_socket(self):
        # Cria o socket do servidor e vincula à porta especificada
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.SERVER_ADDRESS, self.SERVER_PORT))
        self.socket_servidor.listen(10)
        
    def aguarda_conexao(self):
        # Loop para aguardar e lidar com conexões de clientes
        while True:
            print(f'Servidor ouvindo em {self.SERVER_ADDRESS}:{self.SERVER_PORT} pronto para receber conexão...')
            socket_cliente, cliente_addr = self.socket_servidor.accept()
            # Inicia uma nova thread para lidar com a conexão do cliente
            Thread(target=self.thread_func, args=(socket_cliente, cliente_addr)).start()
 
if __name__ == "__main__":
    SERVER_ADDRESS = '0.0.0.0'
    SERVER_PORT = 8080
    HOST= '192.168.0.108'
    USER='root'
    PASSWORD=''
    DATABASE='cocadaboa'
    
    server = Server(SERVER_ADDRESS, SERVER_PORT, HOST, USER, PASSWORD, DATABASE)
    server.cria_socket()
    server.aguarda_conexao()
