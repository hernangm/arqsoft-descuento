from .base import IDiscountStrategy


class StudentDiscount(IDiscountStrategy):
    def aplicarDescuento(self, importe: float) -> float:
        return importe * 0.9