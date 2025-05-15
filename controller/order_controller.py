from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query
from model.order import Order

router = APIRouter(
    prefix="/order",
    tags=["order"]
)

orders = {}


@router.get("/customer/", response_model=List[Order])
def get_order_by_customer(customer_name: Optional[str] = Query(None)) -> List[Order]:
    order_results = []
    for order in orders.values():
        if order.customer_name == customer_name:
            order_results.append(order)
    return order_results


@router.get("/{order_id}/", response_model=Order)
def get_order(order_id: int):
    order = orders.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order




@router.post("/", response_model=Order)
def create_order(order: Order):
    if order.order_id in orders:
        raise HTTPException(status_code=400, detail=f"Order ID {order.order_id} already exists")
    orders[order.order_id] = order
    return order


@router.put("/{order_id}/", response_model=Order)
def update_order(order_id: int, updated_order: Order):
    if order_id not in orders:
        raise HTTPException(status_code=404, detail="Order not found")
    orders[order_id] = updated_order
    return updated_order


@router.delete("/{order_id}")
def delete_order(order_id: int):
    order = orders.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    del orders[order_id]
