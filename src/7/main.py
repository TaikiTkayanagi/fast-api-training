from fastapi import FastAPI
from Controller.CategoryController import router as category_router
from Controller.ItemController import router as item_router


app = FastAPI()

app.include_router(category_router)
app.include_router(item_router)