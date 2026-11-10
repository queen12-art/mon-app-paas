from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Bonjour ! C'est mon application PaaS déployée avec succès."

if __name__ == '__main__':
    # Heroku et les serveurs cloud imposent un port dynamique
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)