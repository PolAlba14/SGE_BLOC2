import connect 
    def read_red()
        connect.connection_bd()
        cursor = conn.cursor()

        sql_read = "SELECT * FROM clientes2"

        cursor.execute(sql_read)
        conn.commit()

        results = cursor.fetchall()

        return results