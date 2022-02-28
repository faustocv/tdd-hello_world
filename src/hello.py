def hello(name: str = None) -> str:
    """Return a greeting with and without name"""
    if not name:
        name = "World"
    return f"Hello, {name}!"
