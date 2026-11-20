import numpy as np 

def make_hours() -> list[int]:
    hours = np.arange(0,22,3)
    
    return hours.tolist()

def vector_report(values: list[float]) -> dict:
    arr = np.asarray(values, dtype=float)
    vector = {
        'third': arr[2],
        'last': arr[-1],
        'middle': arr[2:6].tolist(),
        'every_second': arr[::2].tolist(),
        'reversed': arr[::-1].tolist(),
        }
    
    return vector

