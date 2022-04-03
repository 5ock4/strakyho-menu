from typing import Optional

from fastapi import FastAPI
import db

app = FastAPI()


@app.get("/")
def read_root():
    dbms = db.UnitOfWork(db.SQLITE, dbname='mydb.sqlite')
    r = dbms.execute_query("SELECT * FROM users")
    print(r)
    return {"User": r}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}