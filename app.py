import string
import random
import redis
from flask import Flask, request, jsonify, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Base URL for shortened links
BASE_URL = "http://localhost:8001/r/"

# Length of short code
SHORT_CODE_LENGTH = 6

# Generate a random short code for the URL
def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=SHORT_CODE_LENGTH))

# POST /url/shorten
@app.route('/url/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')
    
    # Check if URL is provided
    if not original_url:
        return jsonify({"error": "URL is required"}), 400
    
    # Generate unique short code
    short_code = generate_short_code()
    
    # Avoid collisions by regenerating if the code already exists
    while r.exists(short_code):
        short_code = generate_short_code()
    
    # Store the URL in Redis
    r.set(short_code, original_url)
    
    # Return the shortened URL
    short_url = BASE_URL + short_code
    return jsonify({"short_url": short_url}), 201

# GET /r/<short_code>
@app.route('/r/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    # Retrieve the original URL from Redis
    original_url = r.get(short_code)
    
    # Redirect if URL exists, else return 404
    if original_url:
        return redirect(original_url, code=302)
    else:
        return jsonify({"error": "Short URL not found"}), 404

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8001, debug=True)
