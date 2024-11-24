
import socket
import threading
import elliptic as ecc
import aes as aes

def main():
    time = [0,0,0]
    for i in range(0 , 5):
        a , b , c = ecc.showtime()
        time[0] += a
        time[1] += b
        time[2] += c
    time[0] /= 5
    time[1] /= 5
    time[2] /= 5
    print("computation time for A , B , shared key = " , time[0] , time[1] , time[2])
    host = '127.0.0.1'
    port = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")

    while True:
        input("press any key to start")
        p = ecc.genP()
        a, b = ecc.genAB(p)
        g = ecc.makeG(a, b, p)
        e = ecc.genE(p)
        ka = ecc.genK(e)
        kag = ecc.double_and_add(g[0], g[1], ka, a, b, p)
        iv = aes.iv_generator()
        message = (
            f"{p},{a},{b},{g[0]},{g[1]},{kag[0]},{kag[1]},{aes.list_to_str(iv)}"
        )
        client_socket.send(message.encode('utf-8'))
        try:
            # Receive and print messages from the server
            message = client_socket.recv(1024).decode('utf-8')
            slist = message.split(',')
            kbg = int(slist[0]), int(slist[1])
            kabg = ecc.double_and_add(kbg[0], kbg[1], ka, a, b, p)
            key = format(kabg[0], '032x')
            print("shared key = " , key)
            message = "okay"
            print("alice is conncted")
            client_socket.send(message.encode('utf-8'))
            message = client_socket.recv(1024).decode('utf-8')
            if message == "okay":
                print("bob is also connected")
                message = input("Enter Message to encrypt and send: ")
                print(message)
                res = ""
                res_list = aes.cbc_encrypt(key, message, iv)
                # print(res_list , type(res_list))
                for i in range(len(res_list)):
                    if i != 0:
                        res += ","
                    res += aes.list_to_str(res_list[i])
                message = res
                # print(message , type(message))
                client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            break

    # Close the connection when done
    client_socket.close()

if __name__ == "__main__":
    main()
