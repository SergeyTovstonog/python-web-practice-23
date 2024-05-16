import socket

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

# Function to send data to the server
def send_data():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((HOST, PORT))

        while True:
            # Input data to send
            message = input("Enter message to send (or type 'quit' to exit): ")
            if message.lower() == 'quit':
                break

            # Send the data to the server
            client_socket.sendall(message.encode())

    finally:
        # Close the connection
        client_socket.close()

# Main function to run the client
def main():
    send_data()

if __name__ == "__main__":
    main()
