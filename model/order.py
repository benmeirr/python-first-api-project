from typing import List
from pydantic import BaseModel


class Order(BaseModel):
    order_id: int
    customer_name: str
    order_items: List[str]
