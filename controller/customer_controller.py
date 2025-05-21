from typing import List, Optional
from fastapi import APIRouter, HTTPException
from model.customer import Customer
from service import customer_service

router = APIRouter(
    prefix="/customer",
    tags=["customer"]
)


@router.post("/")
async def create_customer(customer: Customer):
    try:
        await customer_service.create_customer(customer)
    except Exception:
        raise HTTPException(status_code=400, detail="Can't create new VIP customer - out of limit")

@router.put("/update/{customer_id}")
async def update_customer(customer_id: int, updated_customer: Customer):
    existing_customer = await customer_service.get_by_id(customer_id)
    if not existing_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    await customer_service.update_customer(customer_id, updated_customer)


@router.delete("delete/{customer_id}")
async def delete_customer(customer_id: int):
    existing_customer = await customer_service.get_by_id(customer_id)
    if not existing_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    await customer_service.delete_by_id(customer_id)


@router.get("customer_id/{customer_id}", response_model=Optional[Customer])
async def get_customer_by_id(customer_id: int):
    return await customer_service.get_by_id(customer_id)


@router.get("/all", response_model=List[Customer])
async def get_all_customers():
    return await customer_service.get_all()
