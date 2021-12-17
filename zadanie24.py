from functools import wraps

def italic(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper

print(italic("text"))
















