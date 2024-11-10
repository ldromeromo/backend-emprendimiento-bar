from typing import List
from pydantic import ValidationError
import src.model.schema as models


def fetch_data_from_table(conn, query: str, model):
    """Ejecuta una consulta SQL y devuelve los datos validados en una lista del modelo especificado."""
    data = []
    
    if not conn:
        return data
    
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            
            # Obtener nombres de columna
            column_names = [column[0] for column in cursor.description]
            
            rows = cursor.fetchall()
            for row in rows:
                try:
                    # Convertir fila a diccionario
                    row_dict = dict(zip(column_names, row))
                    instance = model(**row_dict)
                    data.append(instance)
                except ValidationError as e:
                    print(f"Error de validación en la fila {row}: {e}")
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
    
    return data

def obtener_usuarios(conn) -> List[models.Usuarios]:
    query = "SELECT id, usuario, rol, nombre, contrasena FROM usuarios"
    return fetch_data_from_table(conn, query, models.Usuarios)

def obtener_productos(conn) -> List[models.Productos]:
    query = "SELECT id_producto, nombre_producto, referencia, cantidad_actual FROM productos"
    return fetch_data_from_table(conn, query, models.Productos)

def obtener_precios(conn) -> List[models.Precios]:
    query = "SELECT id_precio, id_producto, precioxunidad FROM precios"
    return fetch_data_from_table(conn, query, models.Precios)

def obtener_productos_vendidos(conn) -> List[models.ProductosVendidos]:
    query = "SELECT id_productos_vendidos, id_producto, unidades_vendidas,id_venta FROM productos_vendidos"
    return fetch_data_from_table(conn, query, models.ProductosVendidos)

def obtener_ventas(conn) -> List[models.Ventas]:
    query = "SELECT id_venta, cliente, fecha, id FROM ventas"
    return fetch_data_from_table(conn, query, models.Ventas)
