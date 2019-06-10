import pymysql.cursors


def atualiza_grupo(user_id, grupo):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='filmes',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        sql = "UPDATE users SET grupo = %s WHERE id = %s"
        val = (int(grupo), int(user_id))

        with connection.cursor() as cursor:
            cursor.execute(sql, val)

        connection.commit()

    finally:
        connection.close()
