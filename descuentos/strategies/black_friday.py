from .base import IDiscountStrategy


class BlackFridayDiscount(IDiscountStrategy):
    def aplicarDescuento(self, importe: float) -> float:
        return importe * 0.7