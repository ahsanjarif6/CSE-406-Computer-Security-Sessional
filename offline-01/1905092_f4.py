import socket
import threading
import aes  
import elliptic as ecc 

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            datalist = data.split(',')
            
            if len(datalist) < 8:
                print("Invalid data format received.")
                continue
            
            # print("datalist = " , datalist)
            p, a, b, g0, g1, kag0, kag1 = map(int, datalist[:7])
            iv = aes.str_to_list(datalist[7])
            # print("bob er iv : " , iv)

            e = ecc.genE(p)
            kb = ecc.genK(e)
            kbg = ecc.double_and_add(g0, g1, kb, a, b, p)
            kabg = ecc.double_and_add(kag0, kag1, kb, a, b, p)
            key = format(kabg[0], '032x')  
            print("shared key = " , key)
            message = f"{kbg[0]},{kbg[1]}"
            client_socket.send(message.encode('utf-8'))

            message = client_socket.recv(1024).decode('utf-8')
            if message == "okay":
                print("alice sends confirmation and I(bob) am also connceted")
                client_socket.send(message.encode('utf-8'))
                message = client_socket.recv(1024).decode('utf-8')
                #print(message)
                messagelist = message.split(',')
                messagelist = aes.cbc_decrypt(key, messagelist, iv)
                decrypted_message = ''.join(messagelist)
                print(decrypted_message)

        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()

def main():
    host = '127.0.0.1'
    port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")


    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")
    handle_client(client_socket=client_socket)

if __name__ == "__main__":
    main()
