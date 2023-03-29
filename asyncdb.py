from datetime import datetime

import sqlite3
import asyncio


DB = 'simple.db'
SQL = 'create table if not exists names(first_name, last_name);'
SCRIPT = 'sql/script.sql'

clock = datetime.now


async def get_cursor():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    return cur

async def execute():
    cursor = await get_cursor()
    with open(SCRIPT, 'r') as file:
        text = file.read()
        for line in text.split('\n'):
            if line:
                cursor.execute(line)
        cursor.connection.commit()
        cursor.connection.close()

async def main():
    print("start: {}:{}:{}".format(clock().minute, clock().second, clock().microsecond))
    await execute()
    print("end: {}:{}:{}".format(clock().minute, clock().second, clock().microsecond))


if __name__ == '__main__':
    asyncio.run(main())
