from flask import Flask, request, render_template, jsonify

from handlers import get_info_by_ip

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_ip', methods=['POST'])
def process_ip():
    data = request.get_json()
    ip_address = data.get('ip')

    if not ip_address:
        return jsonify({"error": {"title": "Missing IP", "message": "Please provide an IP address"}, "status": 400})

    ip_info = get_info_by_ip(ip_address)
    return jsonify(ip_info)


if __name__ == '__main__':
    app.run(debug=True)
