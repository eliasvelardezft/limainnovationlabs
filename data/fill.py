import json, sys
from psycopg2 import connect, Error
from random import randint

with open('./clients.json') as f:

    # use load() rather than loads() for JSON files
    clients = json.load(f)

with open('./credit_requests.json') as f2:

    # use load() rather than loads() for JSON files
    credit_requests = json.load(f2)


try:
    # declare a new PostgreSQL connection object
    conn = connect(
        dbname = "limadb",
        user = "limauser",
        host = "127.0.0.1",
        password = "limapassword",
        port = "5432",
        # attempt to connect for 3 seconds then raise exception
        connect_timeout = 5
    )

    cur = conn.cursor()
    print ("\ncreated cursor object:", cur)

except (Exception, Error) as err:
    print ("\npsycopg2 connect error:", err)
    conn = None
    cur = None


if cur != None:

    try:
        risks = ['Bueno', 'Regular', 'Malo']
        statuses = ['Pendiente', 'Cancelada', 'Aprobada']
        
        for c in clients:
            sql_string = f'INSERT INTO credits_client(first_name, last_name, sbs_debt, sentinel_risk_score) VALUES(\'{c["first_name"]}\', \'{c["last_name"]}\', {c["sbs_debt"]}, \'{risks[c["sentinel_risk_score"]]}\')'
            cur.execute( sql_string )
            conn.commit()

        for r in credit_requests:
            sql_string = f'INSERT INTO credits_creditrequest(date, amount, status, ai_score, cliente_id) VALUES(\'{r["date"]}\', {r["amount"]}, \'{statuses[r["status"]]}\', {r["ai_score"]}, {r["client"]})'
            cur.execute( sql_string )
            conn.commit()
        


        print ('\nfinished INSERT INTO execution')

    except (Exception, Error) as error:
        print("\nexecute_sql() error:", error)
        conn.rollback()

    # close the cursor and connection
    cur.close()
    conn.close()