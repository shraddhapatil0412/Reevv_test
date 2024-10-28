# Reevv_test

# URL Shortener API

## Table of Contents
1. [Setup and Execution Steps](#setup-and-execution-steps)
2. [Design Decisions and Trade-offs](#design-decisions-and-trade-offs)
3. [Deviations and Additional Features](#deviations-and-additional-features)
4. [Testing Instructions](#testing-instructions)

## Setup and Execution Steps

### Prerequisites
- Python 3.x
- Redis server
- `Flask` and `redis` Python packages

### Installation
1. **Clone the Repository**
   ```bash
   git clone <your-repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies**
   ```bash
   pip install flask redis flask-cors
   ```

3. **Start Redis Server**
   Ensure your Redis server is running. You can start it with:
   ```bash
   redis-server --service-start
   ```

4. **Run the Flask Application**
   ```bash
   python app.py
   ```
   The server will start on `http://127.0.0.1:8001`.

## Design Decisions and Trade-offs
- **Choice of Redis**: Redis was selected for its speed and efficiency in handling key-value data storage, which is ideal for URL shortening applications.
- **Random Short Code Generation**: Randomly generating short codes allows for a simple and quick implementation, but it does introduce a risk of collision, which is mitigated by checking for existing codes in Redis.
- **CORS Support**: Enabled to allow requests from different origins, facilitating cross-domain usage of the API.

## Deviations and Additional Features
- **CSRF Protection**: Initially planned to include CSRF protection for POST requests, but this was omitted due to the nature of the API not serving forms. 
- **Error Handling**: Implemented basic error handling for missing URLs and invalid short codes.

## Testing Instructions
You can test the endpoints using Postman or `curl`.

### Endpoints
1. **Shorten a URL**
   - **POST** `http://127.0.0.1:8001/url/shorten`
   - **Body** (JSON):
     ```json
     {
       "url": "https://www.example.com"
     }
     ```
   - **Response**:
     ```json
     {
       "short_url": "http://localhost:8000/r/<short_code>"
     }
     ```

2. **Redirect to Original URL**
   - **GET** `http://127.0.0.1:8000/r/<short_code>`
   - **Response**: Redirects to the original URL or returns a 404 error if not found.

### Postman Collection
You can also create a Postman collection to group these requests for easier testing. Make sure to include:
- The URL shortening request.
- The redirection request.

## Submission
Once you have created your repository and pushed your code, please send the link to josh@reevv.com.
