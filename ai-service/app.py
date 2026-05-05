from flask import Flask, jsonify
from routes.analyze_routes import analyze_bp

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import logging

# create app
app = Flask(__name__)

# logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# rate limiting
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

# register routes
app.register_blueprint(analyze_bp)

# health endpoint
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "ai-service"
    })

# home endpoint
@app.route("/", methods=["GET"])
def home():
    return "AI Service is running"

# security headers
@app.after_request
def add_security_headers(response):
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"

    if "Server" in response.headers:
        response.headers["Server"] = "SecureServer"

    return response

# run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)