from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notifications', methods=['POST'])
def notifications():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    return jsonify({"message": "Notification received", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)