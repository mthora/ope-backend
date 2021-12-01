def create_product_validation(
        name: str,
        description: str,
        category: str,
        price: float,
        amount: int,
        promotion: bool):
    message: list[str] = []
    if not isinstance(name, str) or name is None or len(name) > 40 or name == "":
        message.append("Nome inválido")
    if not isinstance(category, int) or category is None or category < 1 or category > 3:
        message.append("Categoria inválida")
    if not isinstance(description,str) or description is None or len(description) > 200 or description == "":
        message.append("Descrição inválida")
    if not isinstance(price, float) or price is None:
        message.append("Preço inválido")
    if not isinstance(amount, int) or amount is None:
        message.append("Quantidade inválida")
    if not isinstance(promotion, bool) or promotion is None:
        message.append("Informação inválida")
    return message