from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def chat():
    if request.method=="POST":
        user_message=request.form['user_message']
        # Implement your logic to generate a philosophical response here
        response = "I ponder, therefore I am."
        return jsonify({"response": response})

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)