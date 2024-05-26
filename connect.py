"""
    o root_path faz com que o bd seja criado na pasta pai da pasta desta classe
    """
import sqlite3
# from pathlib import Path

# ROOT_Path = Path(__file__).parent
# conn = sqlite3.connect(ROOT_PATH / "clientes.db")

conn = sqlite3.connect("clientes.db")
