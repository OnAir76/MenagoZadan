import time

def czas_wykonania(func):
    """Dekorator do mierzenia czasu wykonania funkcji."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Czas wykonania funkcji '{func.__name__}': {elapsed_time:.4f} sekund")
        return result
    return wrapper
