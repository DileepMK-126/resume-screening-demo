from flask import Flask, render_template, request

app = Flask(__name__)

jobs = {
    "Python Developer": ["python","flask","sql"],
    "Web Developer": ["html","css","javascript"],
    "Data Analyst": ["python","sql","excel"]
}

@app.route("/", methods=["GET","POST"])
def home():
    result = []
    if request.method == "POST":
        resume = request.form["resume"].lower()
        for job, skills in jobs.items():
            match = sum(1 for s in skills if s in resume)
            if match > 0:
                result.append((job, match))
    return render_template("index.html", result=result)

app.run()
