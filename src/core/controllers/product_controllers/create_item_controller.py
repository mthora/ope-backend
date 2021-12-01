class CreateProductController:

    def __init__(self, create_product_use_case):
        self.create_product_use_case = create_product_use_case

    def route(self, body):
        print(body)
        if body is not None:
            print("controller", body)
            name = body["name"] if "name" in body else None
            description = body["description"] if "description" in body else None
            category = body["category"] if "category" in body else None
            price = body["price"] if "price" in body else None
            amount = body["amount"] if "amount" in body else None
            promotion = body["promotion"] if "promotion" in body else None
            response = self.create_product_use_case.create(
                name=name,
                description=description,
                category=category,
                price=price,
                amount=amount,
                promotion=promotion)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}
