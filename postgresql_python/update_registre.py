import connect

def update_reg(): 
    conn = connect.connection_bd()
    cursor = conn.cursor()

    sql_update = '''
    UPDATE clientes
    SET telefono_cliente=000000000
    WHERE id_cliente = 1
    '''

    cursor.execute(sql_update)
    conn.commit()

    cursor.close()
    conn.close()

    return {"Update succesfully"}