import socket

class Client:

    def __init__(self):
        # 创建客户端套接字
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 与服务器建立链接
        self.client_socket.connect(("127.0.0.1", 9000))

    #向服务器端发生数据和接收数据
    def start_client(self):
        # 发生数据
        while True:
            data = input("发送:")
            if data != '*':
                self.client_socket.send(data.encode("utf-8"))
                # 接收服务器返回的数据
                recv_data = self.client_socket.recv(1024)
                print(recv_data.decode("utf-8"))
            else:
                # 关闭套接字
                self.client_socket.close()
                exit()

if __name__ == '__main__':
    Client().start_client()
