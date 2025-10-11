from abc import ABC, abstractmethod


class IDiscountStrategy(ABC):
    @abstractmethod
    def aplicarDescuento(self, importe: float) -> float:
        pass