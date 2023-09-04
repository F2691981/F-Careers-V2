from flask import Flask, render_template,jsonify
from database import load_jobs_from_db

app = Flask(__name__)  # how a script is invoked


JOBS = load_jobs_from_db(id)
jobs = JOBS


@app.route("/")
def hello_world():
  jobs = load_jobs_from_db(id)
  return render_template("Home.html",
                         jobs = jobs,
                         Company_Name="Careers4-all.org")
  
@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db(id)
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  

