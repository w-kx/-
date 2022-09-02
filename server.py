import socket, threading


# 服务器端程序
class Server:

    def __init__(self):
        # 创建服务器端套接字对象
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定端口和IP地址
        self.server_socket.bind(("127.0.0.1", 9000))
        # 设置监听
        self.server_socket.listen(128)

    # 向客户端发生数据和接收数据
    def start_server(self):
        print("等待客户端链接...")
        while True:
            # 接收客户端对象
            server_socket, ip_port = self.server_socket.accept()
            # 创建多线程
            t = threading.Thread(target=self.handle_client_request, args=(server_socket, ip_port))
            t.start()

    # 与客户端保持联系,并能传递数据
    def handle_client_request(self, server_client_socket, ip_port):
        while True:
            # 接收数据
            recv_data = server_client_socket.recv(1024)
            if recv_data:
                print( f"用户{ip_port}发送消息:",recv_data.decode("utf-8"))
                # 服务器返回数据
                back_data = "服务器接收:" + recv_data.decode("utf-8")
                server_client_socket.send(back_data.encode("utf-8"))
            else:
                print("客户端下线", ip_port)
                break
        # 关闭
        server_client_socket.close()


if __name__ == '__main__':
    Server().start_server()
