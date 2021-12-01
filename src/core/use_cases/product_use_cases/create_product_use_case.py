from src.core.validations import create_product_validation as validade


class CreateProduct:

    def __init__(self, item_repository):
        self.item_repository = item_repository

    def create(self, name: str,
               description: str,
               category: int,
               price: float,
               amount: int,
               promotion: bool):
        invalid_inputs = validade(
            name=name,
            description=description,
            category=category,
            price=float(price),
            amount=amount,
            promotion=promotion)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.item_repository.create_product(name=name, category=category, description=description, price=float(price), amount=amount,
                                                        promotion=promotion)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}
