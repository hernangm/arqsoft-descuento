from .strategies.student import StudentDiscount
from .strategies.black_friday import BlackFridayDiscount
from .strategies.default import DefaultDiscount

strategies = {
    "student": StudentDiscount(),
    "black_friday": BlackFridayDiscount(),
}
default_strategy = DefaultDiscount()


def aplicarDescuento(discount_type: str, importe: float) -> float:
    strategy = strategies.get(discount_type, default_strategy)
    return strategy.aplicarDescuento(importe)