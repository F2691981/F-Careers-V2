from sqlalchemy import create_engine,text



db_connection_string = "mysql+pymysql://l6tbwccknb1jb6knd5wn:pscale_pw_Magv1J5sLaICLmVGL4cVWbvV2jcuPMnTSanKlozquVV@aws.connect.psdb.cloud/fcareers?charset=utf8mb4"


engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(
      text("select title, location, salary,currency from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs
