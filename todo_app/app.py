from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []   # store tasks in list

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form["task"]
        if task != "":
            tasks.append(task)
        return redirect("/")
    return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    tasks.pop(id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)