from flask import Flask, jsonify
from routes import catalog_routes
import os

app = Flask(__name__)
app.register_blueprint(catalog_routes)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'API is running 🚀'}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
