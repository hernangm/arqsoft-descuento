# main.py
import json
from app import facturar

# Leer JSON desde archivo
with open("input.json", "r") as f:
    ticket = json.load(f)

resultado = facturar(ticket)

# Mostrar resultado formateado
print(json.dumps(resultado, indent=2))
