# Firebase Product Schema Documentation

## Estrutura do Produto

Cada produto salvo no Firebase deve seguir o seguinte formato:

```
products/{productId}:
  name: string                # Nome do produto
  description: string         # Descrição detalhada
  price: number               # Preço do produto (float)
  categories: [string]        # Lista de categorias
  brand: string               # Marca
  imageUrl: string            # URL da imagem principal
  sourceUrl: string           # URL da loja de origem
  createdAt: timestamp        # Data de criação
  updatedAt: timestamp        # Data da última atualização
  status: string              # 'pending', 'approved', 'rejected'
  approvedBy: string          # (opcional) ID do admin que aprovou
```

## Exemplo de Produto

```json
{
  "name": "Xbox Wireless Controller - Phantom Black Special Edition",
  "description": "Controle sem fio para Xbox, edição especial Phantom Black.",
  "price": 399.90,
  "categories": ["Games", "Acessórios"],
  "brand": "Microsoft",
  "imageUrl": "https://exemplo.com/xbox-controller.jpg",
  "sourceUrl": "https://loja.com/produto/123",
  "createdAt": 1719100000,
  "updatedAt": 1719100000,
  "status": "pending",
  "approvedBy": null
}
```

## Validação de Dados (Python)

```python
# Exemplo de validação antes de salvar
REQUIRED_FIELDS = ["name", "price", "categories", "brand", "imageUrl", "sourceUrl", "status"]

def validate_product(product):
    for field in REQUIRED_FIELDS:
        if field not in product or product[field] in [None, "", []]:
            raise ValueError(f"Campo obrigatório ausente: {field}")
    if not isinstance(product["price"], (int, float)):
        raise ValueError("O campo 'price' deve ser numérico.")
    if not isinstance(product["categories"], list):
        raise ValueError("O campo 'categories' deve ser uma lista.")
    # Adicione outras validações conforme necessário
    return True
```

## Exemplo de Escrita

```python
firebase_client.save_product(product_data)
```

## Exemplo de Leitura

```python
products = firebase_client.get_products(filters={"status": "approved"}, limit=10)
```

---
Adapte e expanda o schema conforme a evolução do projeto.
