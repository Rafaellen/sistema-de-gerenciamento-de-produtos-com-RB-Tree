import json
from typing import List
from src.product import Product

class Color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[31m'
    BLACK_BG = '\033[40m'
    RED_BG = '\033[41m'

def export_products(products: List[Product], filename: str = "data/inventory.json") -> bool:
    try:
        with open(filename, 'w') as f:
            json.dump([p.to_dict() for p in products], f, indent=2)
        return True
    except Exception as e:
        print(f"{Color.FAIL}Erro ao exportar: {e}{Color.END}")
        return False

def import_products(filename: str = "data/inventory.json") -> List[Product]:
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return [Product.from_dict(p) for p in data if Product.from_dict(p)]
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"{Color.WARNING}Aviso: {e}{Color.END}")
        return []

def input_color(prompt: str, color: str = Color.BLUE) -> str:
    return input(f"{color}{prompt}{Color.END}")

def print_color(text: str, color: str = Color.GREEN, end: str = "\n") -> None:
    print(f"{color}{text}{Color.END}", end=end)