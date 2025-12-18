from fastapi import FastAPI
from .routers import auth, users, accounting, audit


app = FastAPI(title="RADIUS Admin Backend")


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(accounting.router)
app.include_router(audit.router)