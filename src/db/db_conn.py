import psycopg2

class ConexionPostgreSQL:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def conectar(self):
        try:
            self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password,
                                          host=self.host, port=self.port)
            print("Conexión exitosa a la base de datos PostgreSQL")
        except Exception as e:
            print(f"No se pudo conectar a la base de datos. Error: {e}")
            self.conn = None
        return self.conn
