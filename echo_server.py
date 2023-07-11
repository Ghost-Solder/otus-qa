import socket
import urllib.parse
from http import HTTPStatus
from typing import Any


def parse_request(request: str) -> [str, str, dict, str]:
    req, *req_headers = request.split('\r\n')
    method, path, *_ = req.split()
    parsed_path = urllib.parse.urlparse(path)
    headers = '<br>\r\n'.join(sorted(req_headers[1:]))
    return method, parsed_path.path, urllib.parse.parse_qs(parsed_path.query), headers


def build_response(method: str, headers: dict, status: 'HTTPStatus', req_headers: str) -> str:
    response = f'Request Method: {method}<br>\n'
    response += f'Request Source: {headers["source"]}<br>\n'
    response += f'Response Status: {status.value} {status.phrase}<br>\n'
    response += req_headers
    status_line = f'HTTP/1.1 {status.value} {status.phrase}'
    body = f'<h3>{response}</h3>'
    headers = '\r\n'.join([
        status_line,
        'Content-Type: text/html',
        f'Content-Length: {len(body)}'
    ])
    result_response = '\r\n\r\n'.join([
        headers,
        body
    ])
    return result_response


def handle_client(client_socket: 'socket', client_address: Any) -> None:
    while True:
        recv_bytes = client_socket.recv(2048)
        request = recv_bytes.decode('utf-8')
        print(f'Message received\n"{recv_bytes}"')
        if request:
            print('sending data back to the client')
            method, path, params, req_headers = parse_request(request)
            headers = {
                'source': client_socket.getpeername(),
                **params
            }
            status = HTTPStatus.OK
            if 'status' in params:
                try:
                    status = HTTPStatus(int(params['status'][0]))
                except ValueError:
                    pass
            response = build_response(method, headers, status, req_headers)
            sent_bytes = client_socket.send(response.encode('utf-8'))
            print(f'{sent_bytes} bytes sent')
        else:
            print(f'no data from {client_address}')
            break
    client_socket.close()


def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)
    print('Server started')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Client connected: {client_address}')
        handle_client(client_socket, client_address)


if __name__ == '__main__':
    run_server()
