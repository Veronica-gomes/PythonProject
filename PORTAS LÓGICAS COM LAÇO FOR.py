#Port Scan
#importando socket
import socket

print ("## INICIANDO PORT SCAN ##")

#Solicitando IP e porta a serem pesquisadas

saida=""
while saida!="EXIT":
    host = input("Qual o dominio ou ip do servidor? ")
    
    for i in range(1024):
        lista = list()
        port = i
        obj_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if obj_socket.connect_ex((host,port)):
            closed = (port," Está fechada.")
            lista.append(closed)
        else:
            opened = (port," Está aberta.")
            lista.append(opened)
    print("Scan Finalizado com sucesso!")
    saida=input("Digite <EXIT> para sair: ").upper()
