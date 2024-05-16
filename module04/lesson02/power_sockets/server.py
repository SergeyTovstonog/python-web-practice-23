import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

# Function to handle client connections
def handle_client(client_socket, address):
    print(f"Connection from {address} established.")
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    # Receive data from client
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received from {threading.current_thread().name} {address}: {data.decode()}")

    # Close the connection
    print(f"Connection from {address} closed.")
    client_socket.close()

# Main function to run the server
def main():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((HOST, PORT))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}")

    try:
        while True:
            # Accept a new connection
            client_socket, address = server_socket.accept()

            # Create a new thread to handle the connection
            client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
            client_thread.start()


    except KeyboardInterrupt:
        print("Server shutting down.")
        server_socket.close()

if __name__ == "__main__":
    main()
