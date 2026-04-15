from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Arithmetic Web Service is Running! Use /add or /divide endpoints."

# Endpoint 1: Addition
@app.route('/add', methods=['GET'])
def add_numbers():
    try:
       
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = a + b
        
     
        return jsonify({"operation": "addition", "a": a, "b": b, "result": result})
    
    except (TypeError, ValueError):
        return jsonify({"error": "Please provide valid numbers for 'a' and 'b'."}), 400

# Endpoint 2: Division
@app.route('/divide', methods=['GET'])
def divide_numbers():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        
        
        if b == 0:
            return jsonify({"error": "Division by zero is not allowed."}), 400
            
        result = a / b
        return jsonify({"operation": "division", "a": a, "b": b, "result": result})
        
    except (TypeError, ValueError):
        return jsonify({"error": "Please provide valid numbers for 'a' and 'b'."}), 400

if __name__ == '__main__':
   
    app.run(host='127.0.0.1', port=8080, debug=True)
