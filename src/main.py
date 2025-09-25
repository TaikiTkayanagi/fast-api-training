from fastapi import FastAPI
from router.memoRouter import router

app = FastAPI()
app.include_router(router)
