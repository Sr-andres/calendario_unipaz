from flask import Flask, render_template, request, redirect

app = Flask(__name__)

USER = "andres"
PASSWORD = "1234"


@app.route("/login", methods=["POST"])
def login():
    is_error = False
    if (
        request.method == "POST"
        and request.form.get("username") == USER
        and request.form.get("password") == PASSWORD
    ):
        return redirect("/")
    
    else:
        is_error = True

    return render_template("/auth/login.html", data={"is_error": is_error})



@app.route("/login", methods=["GET"])
def login1():
    return render_template("/auth/login.html", data={})

@app.route("/")
def index():
    print(request.args.get("data"))
    return render_template("home.html", data={})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
