from flask import Flask, render_template , request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    print(data)
    return jsonify({"message": "Data received successfully."})
@app.route('/home')
def home():
    return "Hello from Flask."

if __name__ == '__main__':
    app.run(debug=True)
    
