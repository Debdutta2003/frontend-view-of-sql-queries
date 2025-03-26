import config as c
def select_operation(username,password,dsn,sql):
    conn=c.connect_oracle_21(username,password,dsn,sql)
    cursor=conn.cursor()
    cursor.execute(sql)
    return cursor