from flask import Flask, jsonify
from routes.analyze_routes import analyze_bp

# Rate limiting
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Logging
import logging

# Initialize app
app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Setup limiter (30 requests per minute)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

# Register routes
app.register_blueprint(analyze_bp)

# Health check endpoint
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "ai-service"
    })

@app.route("/", methods=["GET"])
def home():
    return "AI Service is running"

@app.after_request
def add_security_headers(response):
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    
    if "Server" in response.headers:
        response.headers["Server"] = "SecureServer"
    
    return response

# Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)