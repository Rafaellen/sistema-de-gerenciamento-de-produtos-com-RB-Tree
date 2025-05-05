from typing import Optional, List
from src.product import Product

class RBNode:
    RED = True
    BLACK = False
    
    def __init__(self, product: Product):
        self.product = product
        self.left: Optional['RBNode'] = None
        self.right: Optional['RBNode'] = None
        self.color = RBNode.RED  # novos nós = vermelho.
        self.parent: Optional['RBNode'] = None

class RBTree:
    def __init__(self):
        self.root: Optional[RBNode] = None
        self.size = 0
    
    def insert(self, product: Product) -> None:
        new_node = RBNode(product)
        if self.root is None:
            self.root = new_node
            self.root.color = RBNode.BLACK # raiz = preta
        else:
            self._insert_node(self.root, new_node)
        
        self._fix_insert(new_node)
        self.size += 1
    
    def _insert_node(self, node: RBNode, new_node: RBNode) -> None:
        if new_node.product.code < node.product.code:
            if node.left is None:
                node.left = new_node
                new_node.parent = node
            else:
                self._insert_node(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
                new_node.parent = node
            else:
                self._insert_node(node.right, new_node)
    
    def _fix_insert(self, node: RBNode) -> None:
        while node != self.root and node.parent.color == RBNode.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == RBNode.RED:
                    # Caso 1: Tio vermelho
                    node.parent.color = RBNode.BLACK
                    uncle.color = RBNode.BLACK
                    node.parent.parent.color = RBNode.RED
                    node = node.parent.parent
                else:
                    # Caso 2: Tio preto e nó eh filho direito
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    # Caso 3: Tio preto e nó eh filho esquerdo
                    node.parent.color = RBNode.BLACK
                    node.parent.parent.color = RBNode.RED
                    self._right_rotate(node.parent.parent)
            else:
                # Casos espelhados
                uncle = node.parent.parent.left
                if uncle and uncle.color == RBNode.RED:
                    node.parent.color = RBNode.BLACK
                    uncle.color = RBNode.BLACK
                    node.parent.parent.color = RBNode.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = RBNode.BLACK
                    node.parent.parent.color = RBNode.RED
                    self._left_rotate(node.parent.parent)
        
        self.root.color = RBNode.BLACK
    
    def _left_rotate(self, x: RBNode) -> None:
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    
    def _right_rotate(self, y: RBNode) -> None:
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
    
    def search(self, code: str) -> Optional[Product]:
        node = self._search_node(self.root, code)
        return node.product if node else None
    
    def _search_node(self, node: Optional[RBNode], code: str) -> Optional[RBNode]:
        if node is None or node.product.code == code:
            return node
        if code < node.product.code:
            return self._search_node(node.left, code)
        return self._search_node(node.right, code)
    
    def delete(self, code: str) -> bool:
        """Remove um produto pelo código e retorna True se bem-sucedido"""
        node = self._search_node(self.root, code)
        if node:
            self._delete_node(node)
            self.size -= 1
            return True
        return False

    def _delete_node(self, node: RBNode) -> None:
        """Implementação da remoção na árvore Rubro-Negra"""
        # Nó com dois filhos - encontre o sucessor in-order
        if node.left and node.right:
            successor = self._minimum(node.right)
            node.product = successor.product
            node = successor

        # Nó tem no máximo um filho
        child = node.left if node.left else node.right
        
        if node.color == RBNode.BLACK:
            if child and child.color == RBNode.RED:
                child.color = RBNode.BLACK
            else:
                self._fix_delete(node)
        
        self._replace_node(node, child)
        
        if node == self.root and child:
            self.root = child
            self.root.color = RBNode.BLACK

    def _fix_delete(self, node: RBNode) -> None:
        """Balanceamento após remoção"""
        while node != self.root and (node is None or node.color == RBNode.BLACK):
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == RBNode.RED:
                    sibling.color = RBNode.BLACK
                    node.parent.color = RBNode.RED
                    self._left_rotate(node.parent)
                    sibling = node.parent.right
                
                if (sibling.left is None or sibling.left.color == RBNode.BLACK) and \
                   (sibling.right is None or sibling.right.color == RBNode.BLACK):
                    sibling.color = RBNode.RED
                    node = node.parent
                else:
                    if sibling.right is None or sibling.right.color == RBNode.BLACK:
                        sibling.left.color = RBNode.BLACK
                        sibling.color = RBNode.RED
                        self._right_rotate(sibling)
                        sibling = node.parent.right
                    
                    sibling.color = node.parent.color
                    node.parent.color = RBNode.BLACK
                    sibling.right.color = RBNode.BLACK
                    self._left_rotate(node.parent)
                    node = self.root
            else:
                # Caso simétrico
                sibling = node.parent.left
                if sibling.color == RBNode.RED:
                    sibling.color = RBNode.BLACK
                    node.parent.color = RBNode.RED
                    self._right_rotate(node.parent)
                    sibling = node.parent.left
                
                if (sibling.right is None or sibling.right.color == RBNode.BLACK) and \
                   (sibling.left is None or sibling.left.color == RBNode.BLACK):
                    sibling.color = RBNode.RED
                    node = node.parent
                else:
                    if sibling.left is None or sibling.left.color == RBNode.BLACK:
                        sibling.right.color = RBNode.BLACK
                        sibling.color = RBNode.RED
                        self._left_rotate(sibling)
                        sibling = node.parent.left
                    
                    sibling.color = node.parent.color
                    node.parent.color = RBNode.BLACK
                    sibling.left.color = RBNode.BLACK
                    self._right_rotate(node.parent)
                    node = self.root
        
        if node:
            node.color = RBNode.BLACK

    def _replace_node(self, node: RBNode, child: Optional[RBNode]) -> None:
        """Substitui um nó por seu filho"""
        if node.parent is None:
            self.root = child
        elif node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child
        
        if child:
            child.parent = node.parent

    def _minimum(self, node: RBNode) -> RBNode:
        """Encontra o nó mínimo na subárvore"""
        while node.left:
            node = node.left
        return node
    
    def in_order_traversal(self) -> List[Product]:
        products = []
        self._in_order(self.root, products)
        return products
    
    def _in_order(self, node: Optional[RBNode], products: List[Product]) -> None:
        if node:
            self._in_order(node.left, products)
            products.append(node.product)
            self._in_order(node.right, products)
    
    def __len__(self) -> int:
        return self.size