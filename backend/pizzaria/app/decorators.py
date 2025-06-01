import logging
from functools import wraps
from config import Config

logging.basicConfig(
    level=Config.LOG_LEVEL,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def log_event(level="INFO"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_func = getattr(logging, level.lower(), logging.info)
            log_func(f"Executando {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
