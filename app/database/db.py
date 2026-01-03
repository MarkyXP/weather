import asyncio
from contextlib import asynccontextmanager
from typing import Optional

import aiofiles
import onlymaps.asyncio as onlymaps
from fastapi import FastAPI


@asynccontextmanager
async def get_db(
    app: Optional[FastAPI] = None, connection_string: Optional[str] = None
):
    if not connection_string:
        connection_string = "sqlite:///:memory"
    async with onlymaps.connect(connection_string) as db:
        await _create_tables(db)
        if app:
            app.db = db
        yield db


async def _create_table(db: onlymaps.AsyncDatabase, table_name: str):
    filename = f"app/database/create_{table_name.lower()}.sql"
    async with aiofiles.open(filename, mode="r") as f:
        query = await f.read()  # Await the read operation
        await db.exec(query)


async def _create_tables(db: onlymaps.AsyncDatabase):
    await asyncio.gather(
        *(
            _create_table(db, table_name)
            for table_name in ("location_metadata", "location_alias", "graphics")
        )
    )

