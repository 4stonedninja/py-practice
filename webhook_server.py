from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON received"}), 400
    
    event = data.get("event")
    user = data.get("user", {}).get("name")
    amount = data.get("amount")
    status_code = data.get("status_code")

    if status_code == 200:
        return jsonify({
            "message": "payment successful",
            "user": user,
            "amount": amount
        }), 200
    
    elif status_code == 400:
        return jsonify({
            "message": "Bad request",
        }), 400
    
    else:
        return jsonify({
            "message": "Unhandled status",
        }), 500
    
if __name__ == "__main__":
    app.run(debug=True)