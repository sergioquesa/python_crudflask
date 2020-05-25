import pymysql

class Claseconnect():
    def __init__(self):
        #conectarme con la base de datos
        self.CrearConnect()
        #abrir la conexion
        self.AbrirConnect()
    def CrearConnect(self):
        self.db = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="",
            db="alumno"
        )
    
    def AbrirConnect(self):
        self.cursor = self.db.cursor()
    
    def EjecutarSql(self,sql):
        self.cursor.execute(sql)

    def DevolverDatos(self):
        return self.cursor.fetchall()

    def CerrarBasededatos(self):
        self.db.close()

    def RealizaCambios(self):
        self.db.commit()

    def DeshacerCambios(self):
        self.db.rollback()