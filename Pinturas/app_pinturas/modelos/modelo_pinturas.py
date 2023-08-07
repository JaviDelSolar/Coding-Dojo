from app_pinturas.configuracion.mysqlconnection import connectToMySQL
from app_pinturas import BASE_DATOS
from app_pinturas.modelos.modelo_usuarios import Usuario
from flask import flash 

class Pintura:
    def __init__(self, data) :
        self.id = data['id']
        self.titulo = data['titulo']
        self.descripcion = data['descripcion']
        self.precio = data['precio']
        self.id_usuario = data['id_usuario']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion']
        self.usuario = None
    
    @classmethod
    def crear_uno(cls, data): #Acá es para crear una pintura
        query = """
                INSERT INTO pinturas (titulo, descripcion, precio, id_usuario)
                VALUES ( %(titulo)s, %(descripcion)s, %(precio)s, %(id_usuario)s)
                """
        id_pintura = connectToMySQL (BASE_DATOS).query_db (query, data)
        return id_pintura
    
    @staticmethod
    def validar_formulario_pinturas (data):
        es_valido = True
        if len(data ['titulo']) < 2:
            es_valido = False
            flash("Debes proporcionar el titulo de la pintura con al menos 2 caracteres.", "error_titulo")
        if len(data ['descripcion']) < 10:
            es_valido = False
            flash("Debes proporcionar la descripción de la pintura con al menos 10 caracteres.", "error_descripcion")
        if len(data ['precio']) < 1:
            es_valido = False
            flash("Debes proporcionar el precio de la pintura.", "error_precio")
        
        return es_valido
    
    @classmethod
    def obtener_todas_con_usuarios (cls,):
        query = """
                SELECT *
                FROM pinturas r JOIN usuarios u
                ON  r.id_usuario = u.id                
                """
        resultado = connectToMySQL (BASE_DATOS).query_db (query)
        print(resultado)
        lista_pinturas = []
        
        for renglon in resultado:
            pintura = Pintura (renglon)
            data_usuario = {
                "id" : renglon ['u.id'],
                "nombre" : renglon ['nombre'],
                "apellido" :renglon ['apellido'],
                "email" :renglon ['email'],
                "contraseña" :renglon ['contraseña'],
                "fecha_creacion" :renglon ['u.fecha_creacion'],
                "fecha_actualizacion" :renglon ['u.fecha_actualizacion'],
            }
            usuario = Usuario (data_usuario)
            pintura.usuario = usuario
            lista_pinturas.append(pintura)
    
        return lista_pinturas
    @classmethod
    def elimina_uno (cls, data):
        query = """
                DELETE FROM pinturas
                WHERE id = %(id)s ;              
                """
        return connectToMySQL(BASE_DATOS).query_db(query, data)
    
    @classmethod
    def obtener_uno_con_usuario (cls, data):
        query = """
                SELECT *
                FROM pinturas r JOIN usuarios u
                ON  r.id_usuario = u.id  
                WHERE r.id= %(id)s;             
                """
        resultado = connectToMySQL(BASE_DATOS).query_db (query, data)
        renglon = resultado [0]
        pintura = Pintura (renglon)
        data_usuario = {
                "id" : renglon ['u.id'],
                "nombre" : renglon ['nombre'],
                "apellido" :renglon ['apellido'],
                "email" :renglon ['email'],
                "contraseña" :renglon ['contraseña'],
                "fecha_creacion" :renglon ['u.fecha_creacion'],
                "fecha_actualizacion" :renglon ['u.fecha_actualizacion'],                    
            }
        pintura.usuario = Usuario (data_usuario)
        return pintura
    
    @classmethod
    def editar_uno (cls, data):
        query = """
                UPDATE pinturas
                SET titulo = %(titulo)s, descripcion = %(descripcion)s, precio = %(precio)s
                WHERE id= %(id)s;             
                """
        return connectToMySQL(BASE_DATOS).query_db( query, data)
    
    @classmethod
    def obtener_uno (cls, data):
        query = """
                SELECT *
                FROM pinturas 
                WHERE id= %(id)s;             
                """
        resultado = connectToMySQL(BASE_DATOS).query_db( query, data)
        pintura = Pintura (resultado [0])
        return pintura