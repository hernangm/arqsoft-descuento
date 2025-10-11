from descuentos import aplicarDescuento
from impuestos import calcularImpuesto
# INPUT
# { "items": [
#   { "id": 1, "product_category": "category_a", "price": 10.0 },
#   { "id": 2, "product_category": "category_b", "price": 20.0 }
# ], "discount": "student" }

# OUTPUT
# {
#   "subtotal": 0.0,
#   "applied_discount": 0.0,
#   "item_taxes": [
#     { "id": 1, "tax": 0.0 },
#     { "id": 2, "tax": 0.0 }
#   ],
#   "total_taxes": 0.0,
#   "final_total": 0.0
# }

def facturar(ticket):
    item_taxes = []
    descs = []
    for i in ticket["items"]:
        descs.append(aplicarDescuento(ticket["discount"], i["price"]))
        tax = calcularImpuesto(i["product_category"], i["price"] - descs[-1])
        item_taxes.append({"id": i["id"], "tax": tax})

    return {
        "subtotal": 0.0,
        "applied_discount": sum(descs),
        "item_taxes": item_taxes,
        "total_taxes": sum([it["tax"] for it in item_taxes]),
        "final_total": sum([i["price"] for i in ticket["items"]]) - sum(descs) + sum([it["tax"] for it in item_taxes])
    }