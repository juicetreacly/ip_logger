from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Flask server is running."

@app.route('/store', methods=['GET'])
def store_location():
    lat = request.args.get('lat')
    lon = request.args.get('long')
    if lat and lon:
        with open('ip_log.txt', 'a') as f:
            f.write(f'Latitude: {lat}, Longitude: {lon}\n')
        return 'Coordinates received and logged.'
    else:
        return 'No coordinates received.', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
