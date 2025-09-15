from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return """Hello from Flask App!"""

@app.route('/healthz')
def healthz():
    # Returning HTML content
    return """
    <html>
      <head>
        <title>Hello WORLD, This is from Flask App!</title>
      </head>
      <body>
        <h1>Status: Healthy</h1>
      </body>
    </html>
    """, 200
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
