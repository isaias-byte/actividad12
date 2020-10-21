import mysql.connector

bd = mysql.connector.connect(user='isaias123', password='S.is2001', database='nopalito')

cursor= bd.cursor()

while True:
    print('1.-Agregar Usuario')
    print('2.-Mostrar Usuarios')
    print('3.-Salir')
    op=input()

    if op=='1':
        nombre=input("Nombre: ")
        segundo_nombre=input("Segundo Nombre: ")
        apellido_paterno=input("Apellido Paterno: ")
        apellido_materno=input("Apellido Materno: ")
        correo=input("Correo: ")
        edad=input("Edad: ")

        consulta="INSERT INTO usuario (nombre, segundo_nombre, apellido_paterno, apellido_materno, correo, edad) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(consulta,(nombre, segundo_nombre, apellido_paterno, apellido_materno, correo, edad))
        bd.commit()
        if cursor.rowcount:
            print("Se agrego usuario")
        else:
            print("Error")

    elif op=='2':
        consulta= "SELECT * FROM usuario"

        cursor.execute(consulta)
        for row in cursor.fetchall():
            print("id: ", row[0])
            print("Nombre: ", row[1])
            print("Segundo Nombre: ", row[2])
            print("Apellido Paterno: ", row[3])
            print("Apellido Materno: ", row[4])
            print("Correo: ", row[5])
            print("Edad: ", row[6])
            print(".-.-.-.-.-.-.-..-.-.-.-.-.-")
    elif op=='3':
        break