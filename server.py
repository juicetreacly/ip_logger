from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def log_ip():
    ip_address = request.remote_addr
    print(f'Received request from IP address: {ip_address}')
    # Log the IP address to a file
    with open('ip_log.txt', 'a') as f:
        f.write(f'{ip_address}\n')
    return '', 204  # Send a no content response

if __name__ == '__main__':
    app.run(host='https://juicetreacly.github.io/ip_logger/', port=5000)
