from pydantic import BaseModel
from typing import Optional

class Usuarios(BaseModel):
    id: int
    usuario: str
    rol: str
    nombre: Optional[str] = None
    contrasena: str

class Productos(BaseModel):
    id_producto: int
    nombre_producto: str
    referencia: Optional[str] = None
    cantidad_actual: int

class Precios(BaseModel):
    id_precio: int
    id_producto: int  # Foránea a Productos
    precioxunidad: Optional[float] = None

class ProductosVendidos(BaseModel): 
    id_productos_vendidos: int
    id_producto: int  # Foránea a Productos
    unidades_vendidas: Optional[int] = None
    id_venta: int # Foránea a ventas

class Ventas(BaseModel):
    id_venta: int
    cliente: Optional[str] = None
    fecha: Optional[str] = None
    id: int  # Foránea a Usuarios

