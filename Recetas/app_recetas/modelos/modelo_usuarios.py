from app_recetas.configuracion.mysqlconnection import connectToMySQL
from app_recetas import EMAIL_REGEX, BASE_DATOS
from flask import flash 

class Usuario: 
    def __init__(self, data) :
        self.id = data ['id']
        self.nombre = data ['nombre']
        self.apellido = data ['apellido']
        self.email = data ['email']
        self.contraseña = data ['contraseña']
        self.fecha_creacion = data ['fecha_creacion']
        self.fecha_actualizacion = data ['fecha_actualizacion']
        
    @classmethod
    def obtener_uno_con_email (cls, data):
        query = """
                SELECT *
                FROM usuarios
                WHERE email = %(email)s
                """
        resultado = connectToMySQL (BASE_DATOS).query_db ( query, data )
        if len(resultado) == 0:
            return None
        else:
            return Usuario(resultado [0])
        
    @classmethod
    def crear_uno (cls, data):
        query = """
                INSERT INTO usuarios ( nombre, apellido, email, contraseña)
                VALUES ( %(nombre)s,  %(apellido)s,  %(email)s,  %(contraseña)s)
                """
        id_usuario = connectToMySQL(BASE_DATOS).query_db(query, data)
        return id_usuario
        
    @staticmethod
    def validar_registro (data, usuario_existe):
        es_valido = True
        if len(data ['nombre']) < 2:
            es_valido = False
            flash ("Tu nombre debe tener al menos 2 caracteres.", "error_nombre") # "error_nombre", esto es para que aparezca el mensaje debajo de nombre

        if len(data ['apellido']) < 2:
            es_valido = False
            flash ("Tu apellido debe tener al menos 2 caracteres.", "error_apellido")

        if not EMAIL_REGEX.match (data ['email']) :
            es_valido = False
            flash ("Por favor proporciona un email valido", "error_email")

        if data ['contraseña']  != data['confirmacion_contraseña']:
            es_valido = False
            flash("Tus contraseñas no coinciden","error_contraseña")

        if usuario_existe != None:
            es_valido = False
            flash("Ya hay una cuenta asociada a este email, por favor ingresar otro","error_email")   
        return es_valido
            
        