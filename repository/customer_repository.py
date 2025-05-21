from typing import Optional, List

from model.customer import Customer
from model.customer_status import CustomerStatus
from repository.database import database

TABLE_NAME = "customer"


async def get_by_id(customer_id: int) -> Optional[Customer]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id=:customer_id"
    return await database.fetch_one(query, values={"customer_id": customer_id})


async def get_all() -> List[Customer]:
    query = f"SELECT * FROM {TABLE_NAME}"
    return await database.fetch_all(query)


async def get_by_status(customer_status: CustomerStatus) -> List[Customer]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE status=:customer_status"
    return await database.fetch_all(query, values={"customer_status": customer_status.name})


async def create_customer(customer: Customer) -> int:
    query = f"""
        INSERT INTO {TABLE_NAME} (first_name, last_name, email, status)
        VALUES (:first_name, :last_name, :email, :status)
    """
    values = {"first_name": customer.first_name, "last_name": customer.last_name, "email": customer.email,
              "status": customer.status.name}
    await database.execute(query, values=values)
    last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")
    return last_record_id[0]


async def update_customer(customer_id: int, customer: Customer):
    query = f"""
        UPDATE {TABLE_NAME}
        SET first_name = :first_name,
        last_name = :last_name,
        email = :email,
        status = :status
        WHERE id = :customer_id
    """

    values = {"first_name": customer.first_name, "last_name": customer.last_name, "email": customer.email,
              "status": customer.status.name, "customer_id": customer_id}
    await database.execute(query, values=values)


async def delete_by_id(customer_id):
    query = f"DELETE FROM {TABLE_NAME} WHERE id=:customer_id"
    await database.execute(query, values={"customer_id": customer_id})
