import sqlite3
import os
from datetime import datetime

DB_PATH = "versa.db"

def init_db():
    """Inicializa la base de datos y crea la tabla si no existe."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS analisis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            nombre_archivo TEXT,
            analisis_completo TEXT
        )
    ''')
    conn.commit()
    conn.close()

def guardar_analisis(nombre_archivo: str, analisis_completo: str):
    """Guarda un nuevo análisis en la base de datos."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
        INSERT INTO analisis (fecha, nombre_archivo, analisis_completo)
        VALUES (?, ?, ?)
    ''', (fecha_actual, nombre_archivo, analisis_completo))
    
    conn.commit()
    conn.close()

def obtener_historial():
    """Obtiene todos los análisis ordenados por fecha descendente."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, fecha, nombre_archivo, analisis_completo 
        FROM analisis 
        ORDER BY fecha DESC
    ''')
    
    resultados = cursor.fetchall()
    conn.close()
    return resultados
