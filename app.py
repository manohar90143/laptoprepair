from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        issue = request.form['issue']
        phone = request.form['phone']
        print(f"Repair Request: {name} | {phone} | {issue}")
        return render_template("contact.html", success=True)
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
