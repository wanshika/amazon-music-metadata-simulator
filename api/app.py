from flask import Flask, jsonify
from routes import catalog_routes

app = Flask(__name__)
app.register_blueprint(catalog_routes)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'API is running 🚀'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5050)

