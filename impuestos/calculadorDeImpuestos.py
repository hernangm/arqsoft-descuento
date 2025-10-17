from abc import ABC

IVA = 20.0
IMPORTACION = 30.0

impuestos = {
    "food_item": [],
    "car": [IVA],
    "imported_car": [IVA, IMPORTACION],
    "cellphone":[IVA, IMPORTACION],
    "computer": [IVA, IMPORTACION]
}

class CalculadorImpuesto(ABC):
    def calcular_impuesto(self, product_category: str,importe: float) -> float:
        imp = impuestos.get(product_category, [])
        t = 0.0
        for i in imp:
            t += importe * (i / 100)
        return t