def delete_product_validation(product_id: int):
    message: list[str] = []
    if not isinstance(product_id, int) or product_id is None or product_id <= 0:
        message.append("Id inválido")
    return message