import socket


def run(runArgs):
    HOST, PORT = runArgs['host'], runArgs['port']

    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)
    print(f'Serving HTTP on port {PORT} ...')
    while True:
        client_connection, client_address = listen_socket.accept()
        request_data = client_connection.recv(1024)
        print(request_data.decode('utf-8'))

        http_response = b"""\
    HTTP/1.1 200 OK

    Hello, World, I just created a Web Server...!
    """
        client_connection.sendall(http_response)
        client_connection.close()