
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple MCP Tool")

# -----------------------------
# Request Model
# -----------------------------
class AddRequest(BaseModel):
    a: int
    b: int


# -----------------------------
# Tool Function
# -----------------------------
def add_numbers(a: int, b: int) -> int:
    return a + b


# -----------------------------
# MCP-style Endpoint
# -----------------------------
@app.post("/tools/add")
def run_add_tool(request: AddRequest):
    result = add_numbers(request.a, request.b)

    return {
        "tool": "add_numbers",
        "input": request.dict(),
        "output": result,
        "status": "success"
    }


# -----------------------------
# Health Check
# -----------------------------
@app.get("/")
def root():
    return {"message": "MCP Tool Running"}