from typing import List, Optional
from pydantic import BaseModel, Field


class Order(BaseModel):
    order_id: int
    customer_name: str = Field(alias="customer")
    order_items: List[str]
