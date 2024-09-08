from flask import Flask, render_template, request, redirect, url_for
import redis
import random
import string

app = Flask(__name__)

# Initialize Redis connection
r = redis.Redis()

# Base URL where the short URLs will be hosted
BASE_URL = "http://localhost:5001/"


def generate_short_url():
    """Generates a random short URL string."""
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(6))


def shorten_url(long_url):
    """Shortens a long URL and stores it in Redis."""
    existing_short_url = r.get(f"url:{long_url}")
    if existing_short_url:
        return f"{BASE_URL}{existing_short_url.decode('utf-8')}"

    while True:
        short_url = generate_short_url()
        if not r.exists(short_url):  # Ensure the short URL is unique
            r.set(short_url, long_url)
            r.set(f"url:{long_url}", short_url)
            break
    return f"{BASE_URL}{short_url}"


@app.route('/', methods=['GET', 'POST'])
def index():
    """Homepage where users can enter a long URL to shorten."""
    if request.method == 'POST' and 'long_url' in request.form:
        long_url = request.form['long_url']
        short_url = shorten_url(long_url)
        return render_template('index.html', short_url=short_url)

    return render_template('index.html')


@app.route('/clear', methods=['POST', 'GET'])
def clear():
    """Clear the shortened URL from the display."""
    return redirect(url_for('index'))


@app.route('/<short_url>')
def redirect_to_url(short_url):
    """Redirects the user to the original long URL based on the short URL."""
    long_url = r.get(short_url)
    if long_url:
        return redirect(long_url.decode('utf-8'))
    else:
        return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
