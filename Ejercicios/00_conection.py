import mysql.connector

# Establece los detalles de conexión a la base de datos
config = {
    'user': 'mouredev_read',
    'password': 'mouredev_pass',
    'host': 'mysql-5707.dinaserver.com',
    'database': 'moure_test',
    'port': '3306'
}

try:
    # Crea una conexión a la base de datos MySQL
    connection = mysql.connector.connect(**config)

    # Realiza operaciones con la base de datos
    # Ejemplo: Ejecuta una consulta
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `challenges`")
    rows = cursor.fetchall()

    # Itera sobre los resultados
    for row in rows:
        print(row)

    # Cierra el cursor y la conexión
    cursor.close()
    connection.close()

except mysql.connector.Error as error:
    print("Error de conexión a la base de datos: {}".format(error))
