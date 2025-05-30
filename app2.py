from flask import Flask, render_template

app = Flask(__name__)

@app.route("/api/users")
def users():
    users = [{'id':'cs01','name':'sanaan'},{'id':'cs02','name':'prajwal'}]
    return render_template("index.html", res=users)

if __name__=='__main__':
    app.run(debug=True)