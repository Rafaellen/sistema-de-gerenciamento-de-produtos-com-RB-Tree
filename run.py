import sys
import os

# Configura o path corretamente
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.inventory import InventorySystem

if __name__ == "__main__":
    # Verifica se a pasta data existe
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Inicia o sistema
    print("\n=== INICIANDO SISTEMA DE INVENTÁRIO ===")
    system = InventorySystem()
    system.run()