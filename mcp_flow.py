from prefect import flow, task

# -----------------------------
# Tool Logic (same as before)
# -----------------------------
@task
def add_numbers(a: int, b: int) -> int:
    return a + b


# -----------------------------
# Prefect Flow (entrypoint)
# -----------------------------
@flow(name="mcp-add-tool-flow")
def run_add_tool(a: int = 1, b: int = 2):
    result = add_numbers(a, b)

    return {
        "tool": "add_numbers",
        "input": {"a": a, "b": b},
        "output": result,
        "status": "success"
    }


if __name__ == "__main__":
    print(run_add_tool(5, 7))