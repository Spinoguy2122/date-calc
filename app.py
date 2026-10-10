
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    difference = None
    date1 = ""
    date2 = ""

    if request.method == "POST":
        date1 = request.form["date1"]
        date2 = request.form["date2"]

        first_date = datetime.strptime(date1, "%Y-%m-%d").date()
        second_date = datetime.strptime(date2, "%Y-%m-%d").date()

        difference = abs((second_date - first_date).days)

    return render_template(
        "index.html",
        difference=difference,
        date1=date1,
        date2=date2
    )

if __name__ == "__main__":
    app.run(debug=True)
