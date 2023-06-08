import mariadb
import dbcreds

def run_procedure(sql, args):
    try:
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
        cursor.execute(sql, args) 
        results = cursor.fetchall()
        cursor.close()
        conn.close()  
        return results
    except:
        print('something went wrong!') 