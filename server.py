import socket
import re
import live_predictions

lp = LivePredictions()


class Server():
    def __init__(self):
        self.host_ip = "localhost"
        self.host_port = 81
        self.s = socket.socket()
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.data_recv_size = 1024
        self.form = b"""<form enctype="multipart/form-data" action="" method="POST">
                <input type="hidden" name="MAX_FILE_SIZE" value="8000000" />
                <input name="uploadedfile" type="file" /><br />
                <input type="submit" value="Upload File" />
            </form>"""

    def get_data(self, conn):
        data = b""
        while True:
            chunk = conn.recv(self.data_recv_size)
            if len(chunk) < self.data_recv_size:
                return data + chunk
            else:
                data += chunk

    def save_file(self, packet):
        # print(packet)
        # name = re.compile(
        #     b'name="uploadedfile"; filename="(.+)"').search(packet).group(1)
        # print(data)
        # data = re.compile(
        #     b"WebKitFormBoundary((\n|.)*)Content-Type.+\n.+?\n((\n|.)*)([\-]+WebKitFormBoundary)?")
        print("Writing file...")
        with open("input.wav", "wb") as file:
            file.write(packet)
        live_prediction = LivePredictions(
            file=EXAMPLES_PATH + 'input.wav')
        live_prediction.make_predictions()
        print("done")

    def run(self):
        print(f"[+] Server: http://{self.host_ip}:{self.host_port}")
        self.s.bind((self.host_ip, self.host_port))
        self.s.listen()

        while True:
            conn, addr = self.s.accept()
            request = self.get_data(conn)

            # GET request
            if request[0:5] == b"GET /":
                conn.sendall(
                    b"HTTP/1.0 200 OK\nContent-Type: text/html\n\n"+self.form)
                print("[+] Responded to GET request!")

            # POST request
            elif request[0:4] == b"POST":
                packet = self.get_data(conn)
                self.save_file(packet)
                ok_reponse = b"Successfully upload %d bytes to the server!" % len(
                    packet)
                conn.sendall(
                    b"HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n"+ok_reponse)
                print(f"[+] {len(packet)} bytes received from POST!")


s = Server()
s.run()
