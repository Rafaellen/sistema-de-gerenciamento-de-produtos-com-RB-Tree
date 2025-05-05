# Sistema de Inventário com Árvore Rubro-Negra

Um sistema completo para gerenciamento de inventário utilizando Árvore Rubro-Negra para armazenamento eficiente.

## Funcionalidades Principais

- ✅ Cadastro de produtos com auto-balanceamento
- 🔍 Busca rápida por código do produto
- 📋 Listagem ordenada de produtos
- 💾 Persistência em arquivo JSON

## Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/Rafaellen/sistema-de-gerenciamento-de-produtos-com-RB-Tree.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o sistema:
```bash
python run.py
```

## Estrutura do Código

```plaintext
inventory_rb_tree/
├── src/
│   ├── rb_tree.py          # Implementação da árvore rubro-negra
│   ├── product.py          # Classe Produto
│   ├── inventory.py        # Sistema principal
│   └── utils.py            # Utilitários (cores, validações)
├── data/                   # Armazenamento persistente
└── run.py                  # Ponto de entrada
```

## Tecnologias Utilizadas

- Python 3.x
- Estrutura de dados Árvore Rubro-Negra
- Persistência JSON
- Terminal colorido
