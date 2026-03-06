import uvicorn
from fastapi import FastAPI
from API.CRUD_routes.post_route import post_router
from API.CRUD_routes.get_route import get_router

app = FastAPI()
app.include_router(post_router)
app.include_router(get_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080)
