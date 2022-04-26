contract_product = {
    "productName": {"type": "string", "required": True},
    "productImage": {"type": "string", "required": True},
    "prices": {
        "type": "dict",
        "required": True,
        "schema": {
            "brl": {
                "type": "dict",
                "required": True,
                "schema": {
                    "priceOf": {"type": "float", "required": True},
                    "priceTo": {"type": "float", "required": True},
                    "percentDiscount": {"type": "float", "required": True},
                },
            },
            "usd": {
                "type": "dict",
                "required": True,
                "schema": {
                    "priceOf": {"type": "float", "required": True},
                    "priceTo": {"type": "float", "required": True},
                    "percentDiscount": {"type": "float", "required": True},
                },
            },
            "eur": {
                "type": "dict",
                "required": True,
                "schema": {
                    "priceOf": {"type": "float", "required": True},
                    "priceTo": {"type": "float", "required": True},
                    "percentDiscount": {"type": "float", "required": True},
                },
            },
            "inr": {
                "type": "dict",
                "required": True,
                "schema": {
                    "priceOf": {"type": "float", "required": True},
                    "priceTo": {"type": "float", "required": True},
                    "percentDiscount": {"type": "float", "required": True},
                },
            },
        },
    },
}
