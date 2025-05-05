from typing import List
from src.rb_tree import RBTree
from src.product import Product
from src.utils import Color, export_products, import_products, input_color, print_color


class InventorySystem:
    def __init__(self):
        self.tree = RBTree()
        self._load_data()
    
    def _load_data(self) -> None:
        products = import_products()
        for product in products:
            if product:
                self.tree.insert(product)
        print_color(f"Dados carregados: {len(products)} produtos", Color.CYAN)
    
    def _save_data(self) -> None:
        products = self.tree.in_order_traversal()
        if export_products(products):
            print_color("Dados salvos com sucesso!", Color.GREEN)
        else:
            print_color("Falha ao salvar dados!", Color.FAIL)
    
    def add_product(self) -> None:
        print_color("\n=== ADICIONAR PRODUTO ===", Color.HEADER)
        
        code = input_color("Código do produto: ")
        if self.tree.search(code):
            print_color("Já existe um produto com este código!", Color.WARNING)
            return
        
        name = input_color("Nome do produto: ")
        
        try:
            quantity = int(input_color("Quantidade em estoque: "))
            price = float(input_color("Preço unitário: "))
        except ValueError:
            print_color("Valor inválido para quantidade ou preço!", Color.FAIL)
            return
        
        product = Product(code=code, name=name, quantity=quantity, price=price)
        if not product.validate():
            print_color("Dados do produto inválidos!", Color.FAIL)
            return
        
        self.tree.insert(product)
        print_color(f"\nProduto '{name}' adicionado com sucesso!", Color.GREEN)
        print_color(f"Código: {code} | Quantidade: {quantity} | Preço: R${price:.2f}")
    
    def remove_product(self) -> None:
        print_color("\n=== REMOVER PRODUTO ===", Color.HEADER)
        
        if len(self.tree) == 0:
            print_color("O inventário está vazio!", Color.WARNING)
            return
        
        code = input_color("Código do produto a remover: ")
        product = self.tree.search(code)
        
        if product:
            if self.tree.delete(code):
                print_color(f"Produto '{product.name}' removido com sucesso!", Color.GREEN)
                self._save_data()
            else:
                print_color("Falha ao remover o produto!", Color.FAIL)
        else:
            print_color("Produto não encontrado!", Color.FAIL)
    
    def search_product(self) -> None:
        print_color("\n=== BUSCAR PRODUTO ===", Color.HEADER)
        
        code = input_color("Código do produto: ")
        product = self.tree.search(code)
        
        if product:
            print_color("\nPRODUTO ENCONTRADO:", Color.GREEN)
            self._print_product_details(product)
        else:
            print_color("Produto não encontrado!", Color.FAIL)
    
    def list_products(self) -> None:
        print_color("\n=== LISTA DE PRODUTOS ===", Color.HEADER)
        
        if len(self.tree) == 0:
            print_color("O inventário está vazio!", Color.WARNING)
            return
        
        products = self.tree.in_order_traversal()
        for i, product in enumerate(products, 1):
            print_color(f"\nProduto #{i}", Color.CYAN)
            self._print_product_details(product)
    
    def _print_product_details(self, product: Product) -> None:
        print(f"Código: {product.code}")
        print(f"Nome: {product.name}")
        print(f"Quantidade: {product.quantity}")
        print(f"Preço: R${product.price:.2f}")
        print(f"Valor total: R${product.quantity * product.price:.2f}")
    
    def show_menu(self) -> None:
        print_color("\n=== SISTEMA DE INVENTÁRIO ===", Color.HEADER + Color.BOLD)
        print_color("1. Adicionar Produto", Color.BLUE)
        print_color("2. Remover Produto", Color.BLUE)
        print_color("3. Buscar Produto", Color.BLUE)
        print_color("4. Listar Produtos", Color.BLUE)
        print_color("5. Salvar e Sair", Color.BLUE)
        print_color("0. Sair sem salvar", Color.RED)
    
    def run(self) -> None:
        while True:
            self.show_menu()
            choice = input_color("\nEscolha uma opção: ", Color.GREEN)
            
            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.remove_product()
            elif choice == "3":
                self.search_product()
            elif choice == "4":
                self.list_products()
            elif choice == "5":
                self._save_data()
                print_color("Sistema encerrado. Dados salvos.", Color.GREEN)
                break
            elif choice == "0":
                print_color("Sistema encerrado sem salvar.", Color.WARNING)
                break
            else:
                print_color("Opção inválida!", Color.FAIL)
            
            input_color("\nPressione Enter para continuar...", Color.CYAN)

if __name__ == "__main__":
    system = InventorySystem()
    system.run()