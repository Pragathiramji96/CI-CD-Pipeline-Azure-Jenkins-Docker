from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🚀 DevOps Project Deployed Successfully</h1>
    <h2>Azure + Jenkins + Docker + GitHub</h2>
    <p>Built by Pragathi</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
