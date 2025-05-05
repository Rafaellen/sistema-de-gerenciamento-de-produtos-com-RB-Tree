from dataclasses import dataclass
from typing import Optional

@dataclass
class Product:
    code: str
    name: str
    quantity: int
    price: float
    
    def validate(self) -> bool:
        if not self.code or not isinstance(self.code, str):
            return False
        if not self.name or not isinstance(self.name, str):
            return False
        if not isinstance(self.quantity, int) or self.quantity < 0:
            return False
        if not isinstance(self.price, (int, float)) or self.price <= 0:
            return False
        return True
    
    def to_dict(self) -> dict:
        return {
            'code': self.code,
            'name': self.name,
            'quantity': self.quantity,
            'price': float(self.price)
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> Optional['Product']:
        try:
            return cls(
                code=data['code'],
                name=data['name'],
                quantity=int(data['quantity']),
                price=float(data['price'])
            )
        except (KeyError, ValueError):
            return None