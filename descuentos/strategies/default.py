from .base import IDiscountStrategy


class DefaultDiscount(IDiscountStrategy):
    def aplicarDescuento(self, importe: float) -> float:
        return importe