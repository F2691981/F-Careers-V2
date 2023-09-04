from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://l6tbwccknb1jb6knd5wn:pscale_pw_Magv1J5sLaICLmVGL4cVWbvV2jcuPMnTSanKlozquVV@aws.connect.psdb.cloud/fcareers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})
