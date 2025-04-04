from flask import Flask, jsonify
from routes import catalog_routes
import os

app = Flask(__name__)

# ✅ Root route
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the Amazon Music Metadata API!'}), 200

# ✅ Health check route
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'API is running 🚀'}), 200

# ✅ Register reconciliation blueprint
app.register_blueprint(catalog_routes)

# ✅ Run app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port)
