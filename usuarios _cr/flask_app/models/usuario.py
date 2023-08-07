from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['Nombre']
        self.apellido = data['Apellido']
        self.email = data['email']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion'] 

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    @classmethod
    def obtener_todos(cls):
        query = """
                SELECT *
                FROM usuario;
                """
        resultado = connectToMySQL("users_schema").query_db( query )
        
        usuarios = []
        for u in resultado:
            usuarios.append( Usuario( u ))
        print(usuarios)
        return usuarios
    
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO usuario (nombre, apellido, email) 
                VALUES (%(nombre)s, %(apellido)s, %(email)s);
                """

        resultado = connectToMySQL('users_schema').query_db( query, data )
        return resultado
    
    @classmethod
    def obtener_uno(cls, data):
        query = """
                SELECT * 
                FROM usuario   
                WHERE id = %(id)s;
                """
        resultado = connectToMySQL ('users_schema').query_db(query, data)
        return cls (resultado[0])
    
    
    @classmethod
    def update(cls, data):
        query = """
                UPDATE usuario
                SET nombre= %(nombre)s, apellido=%(apellido)s, email=%(email)s, updated_at=NOW() 
                WHERE id = %(id)s;
                """
        return connectToMySQL('users_schema').query_db( query, data )
    
    @classmethod
    def eliminar(cls, data):
        query  ="""
                DELETE 
                FROM usuario
                WHERE id = %(id)s;
                """
        return connectToMySQL('users_schema').query_db(query, data)
    

