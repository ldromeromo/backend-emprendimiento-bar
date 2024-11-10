import src.routes.index.index_crud as index_crud
from src.config.database import get_db_connection
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import pyodbc
from dotenv import load_dotenv

load_dotenv()

message_not_found = "No existe la data"
index_router = APIRouter()

# @index_router.post("/delete_evicted", status_code=status.HTTP_201_CREATED)
# def activacion_desa(index: schema.Namespace, conn: pyodbc.Connection = Depends(get_db_connection)):
#     # Ejecución bash
#     result = scripts.delete_pod(index.cluster, index.pod, index.app)
#     return {"status": result }

@index_router.get("/usuarios", status_code=status.HTTP_200_OK)
def get_user(conn: pyodbc.Connection = Depends(get_db_connection)):
    usuarios = index_crud.obtener_usuarios(conn)
    print("\nUsuarios:")
    for usuario in usuarios:
        print(usuario.json())
    return usuarios

@index_router.get("/productos", status_code=status.HTTP_200_OK)
def get_productos(conn: pyodbc.Connection = Depends(get_db_connection)):
    productos = index_crud.obtener_productos(conn)
    print("\nProductos:")
    for producto in productos:
        print(producto.json())
    return productos

@index_router.get("/precios", status_code=status.HTTP_200_OK)
def get_precios(conn: pyodbc.Connection = Depends(get_db_connection)):
    precios = index_crud.obtener_precios(conn)
    print("\nPrecios:")
    for precio in precios:
        print(precio.json())
    return precios

@index_router.get("/productos_vendidos", status_code=status.HTTP_200_OK)
def get_productos_vendidos(conn: pyodbc.Connection = Depends(get_db_connection)):
    productos_vendidos = index_crud.obtener_productos_vendidos(conn)
    print("\nProductos Vendidos:")
    for producto_vendido in productos_vendidos:
        print(producto_vendido.json())
    return productos_vendidos

@index_router.get("/ventas", status_code=status.HTTP_200_OK)
def get_ventas(conn: pyodbc.Connection = Depends(get_db_connection)):
    ventas = index_crud.obtener_ventas(conn)
    print("\nVentas:")
    for venta in ventas:
        print(venta.json())
    return ventas
