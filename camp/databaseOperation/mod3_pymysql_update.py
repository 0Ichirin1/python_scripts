import pymysql

db = pymysql.connect("localhost", "root", "", "testdb")

try:
    # %s 是占位符
    with db.cursor() as cursor:
        sql = """ update book set name = %s where id = %s """
        value = ("活着", 1002)
        cursor.execute(sql, value)
    db.commit()
except Exception as e:
    print(f"insert error {e}")
finally:
    # 关闭数据库连接
    db.close()
    print(cursor.rowcount)
