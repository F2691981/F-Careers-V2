from flask import Flask, render_template,jsonify
from sqlalchemy import text
from database import create_engine,engine

app = Flask(__name__)  # how a script is invok
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs=[]
    for rows in result.all():
      jobs.append(rows)
    return jobs

JOBS = load_jobs_from_db()
jobs = JOBS


@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template("Home.html",
                         jobs = JOBS,
                         Company_Name="Careers4-all.org")
  
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  

