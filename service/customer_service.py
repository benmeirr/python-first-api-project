from typing import Optional, List

from model.customer import Customer
from model.customer_status import CustomerStatus
from repository import customer_repository


async def get_by_id(customer_id: int) -> Optional[Customer]:
    return await customer_repository.get_by_id(customer_id)


async def get_all() -> List[Customer]:
    return await customer_repository.get_all()


async def create_customer(customer: Customer) -> int:
    if customer.status == CustomerStatus.VIP:
        vip_customers = await customer_repository.get_by_status(CustomerStatus.VIP)
        if len(vip_customers) < 2:
            return await customer_repository.create_customer(customer)
        else:
            raise Exception("Can't create new VIP customer - out of limit")
    else:
        return await customer_repository.create_customer(customer)


async def update_customer(customer_id: int, customer: Customer):
    await customer_repository.update_customer(customer_id, customer)


async def delete_by_id(customer_id):
    await customer_repository.delete_by_id(customer_id)
