import pymysql



# Create a MySQL connection
cnx = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host="shanks-justatestsubject-c98a.h.aivencloud.com",
    password="AVNS_uxSiv4oYViwH83p8Lbe",
    read_timeout=timeout,
    port=26463,
    user="avnadmin",
    write_timeout=timeout,
)

cursor = conn.cursor()

# Create the users table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT,
        user_id INT,
        thumbnail BLOB,
        file_caption VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255),
        PRIMARY KEY (id)
    );
""")
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()
