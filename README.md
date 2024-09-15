# URL Shortener

A simple URL shortening service built with Flask and Redis.

## Features

- **Shorten long URLs to easily shareable short URLs**: Redis stores mappings between shortened identifiers and original URLs using key-value pairs, allowing for quick retrieval.
- **Redirect short URLs to the original long URLs**: Redis retrieves the original URL from the shortened identifier to facilitate immediate redirection.
- **Clear the shortened URL after use**: Redis deletes the specific key-value pair to remove the association between the shortened URL and the original URL, ensuring efficient use of storage.

## Prerequisites

- Python 3.6+
- Redis

## Installation

### Step 1: Install Redis

#### On macOS using Homebrew:

1. Install Redis:
   ```bash
   brew install redis
   
2. Start Redis as a background service:
   ```bash
   brew services start redis
   
3. Verify that Redis is running:
   ```bash
   redis-cli ping
  If Redis is running, it will respond with PONG.

### Step 2: Clone the Repository
1. Clone the repository and navigate to the directory::
   ```bash
   git clone https://github.com/yourusername/url-shortener.git
   cd url-shortener

### Step 3: Set Up Python Environment
- Set up a Python virtual environment and install dependencies:
   ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

### Step 4: Run the Application
- Run the Flask application by executing the script:
   ```bash
   Python app.py
This command starts the server, making the app accessible on your local network at http://localhost:5001.

### Step 4: Accessing the Application
Once the application is running, you can access it by navigating to http://localhost:5001 in your web browser. Here you can start shortening URLs immediately.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

### MIT License


