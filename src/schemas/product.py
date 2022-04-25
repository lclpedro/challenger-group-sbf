from pydantic import Field

from src.schemas import CustomBaseModel


class PriceSchema(CustomBaseModel):
    price_of: float = Field(alias="priceOf")
    price_to: float = Field(alias="priceTo")
    percent_discount: int = Field(alias="percentDiscount")


class PricesSchema(CustomBaseModel):
    brl: PriceSchema
    usd: PriceSchema
    eur: PriceSchema
    inr: PriceSchema


class ProductSchema(CustomBaseModel):
    name: str = Field(alias="productName")
    image: str = Field(alias="productImage")
    prices: PricesSchema
