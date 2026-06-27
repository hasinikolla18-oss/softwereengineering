from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask CI/CD!"

@app.route('/health')
def health():
    return "App is healthy!"

if __name__ == '__main__':
    app.run(debug=True)