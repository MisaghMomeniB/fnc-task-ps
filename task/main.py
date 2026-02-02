from fastapi import FastAPI
from task.middlewares.rate_limiter import RateLimitMiddleware
from task.routes.ping import router as ping_router

app = FastAPI()

app.add_middleware(RateLimitMiddleware)

app.include_router(ping_router)
