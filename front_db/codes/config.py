import oracledb
def connect_oracle_21(username,password,dsn):
    return oracledb.connect(username,password,dsn)