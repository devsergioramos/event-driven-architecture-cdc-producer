import asyncpg
import asyncio
from faker import Faker
import argparse

fake = Faker()

db_params = {
    'database': 'erp_db',
    'user': 'erp_user',
    'password': 'erp_pass',
    'host': 'localhost',
    'port': '5432'
}

semaphore = asyncio.Semaphore(50)

async def insert_record():
    async with semaphore:
        conn = await asyncpg.connect(**db_params)
        actual_address = fake.address()
        next_address = fake.address()
        status = fake.random_element(elements=('in transit', 'delivered', 'pending', 'returned'))

        await conn.execute('''
            INSERT INTO package_status (actual_address, next_address, status)
            VALUES ($1, $2, $3)
        ''', actual_address, next_address, status)
        await conn.close()

async def insert_fake_data(num_records):
    tasks = []
    for _ in range(num_records):
        tasks.append(insert_record())
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Stream fake data CDC events to Kafka")
    parser.add_argument("-Q", "--quantity", type=int, help="quantity of stored data", default=10)
    args = parser.parse_args()

    asyncio.run(insert_fake_data(args.quantity))