from website import create_app
import socket
app = create_app()

if __name__ == "__main__":
    app.run(host=socket.gethostbyname(socket.gethostname()), port=5554, debug=True)
