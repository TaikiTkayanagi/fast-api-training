from fastapi import APIRouter


router = APIRouter()

@router.get("/categories/")
def read_categories():
    return [{"category_id": "A"}, {"category_id": "B"}]