from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "shubham_secret_key"

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    print(f"\n[CONTACT FORM]\nName: {name}\nEmail: {email}\nMessage: {message}\n")

    flash("Thank you! Your message has been sent.")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
