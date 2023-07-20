from flask import Flask, render_template, jsonify

app = Flask(__name__)  # how a script is invoked

JOBS = [{
  "id": 1,
  "title": "Data Analyst",
  "Location": "Beirut,Lebanon",
  "Salary": "$ 1000.00"
}, {
  "id": 2,
  "Location": "Remote",
  "title": "Data Scientist",
  "Salary": "$ 1500.00"
}, {
  "id": 3,
  "Location": "Onsite",
  "title": "Back-end Engineer",
  "Salary": "$ 1300.00"
}, {
  "id": 4,
  "Location": "Hybrid",
  "title": "Front-end Engineer",
  "Salary": "$ 1300.00"
}]


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


@app.route("/")
def hello_world():
  return render_template("Home.html", jobs=JOBS, Company_Name="Careers4-all")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
