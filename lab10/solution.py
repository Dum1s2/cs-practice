import numpy as np

def make_table(rows: int, columns: int) -> list[list[int]]:
    arr = np.arange(rows*columns)
    table = arr.reshape(rows,columns)
    return table.tolist()

def rectangle(
    matrix: list[list[float]],
    row_start: int,
    row_stop: int,
    column_start: int,
    column_stop: int,
) -> list[list[float]]:
    arr = np.array(matrix)
    slice = arr[row_start:row_stop, column_start:column_stop]
    
    return slice.tolist()

def replace_rectangle(
    matrix: list[list[float]],
    row_start: int,
    row_stop: int,
    column_start: int,
    column_stop: int,
    value: float,
) -> list[list[float]]:
    arr = np.array(matrix).copy()
    arr[row_start:row_stop, column_start:column_stop] = value
        
    return arr.tolist()

def matrix_vector_product(matrix: list[list[float]], vector: list[float]) -> list[float]:
    a = np.array(matrix)
    b = np.array(vector)
    c = a @ b
    
    return c.tolist()

def matrix_multiply(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    a = np.array(left)
    b = np.array(right)
    c = a @ b
        
    return c.tolist()

def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    arr = np.array(matrix)
    trans_arr = arr.T
    return trans_arr.tolist()

def solve_system(matrix: list[list[float]], vector: list[float]) -> list[float]:
    a = np.array(matrix)
    b = np.array(vector)
    x = np.linalg.solve(a, b)
    
    return np.round(x, 6).tolist()

def tensor_channel_mean(tensor: list) -> list:
    ten = np.array(tensor)
    res = ten.mean(axis=-1)
    
    return res.tolist()

def point_distance(first: list[float], second: list[float]) -> float:
    a = np.array(first)
    b = np.array(second)
    res = np.linalg.norm(a - b)
    
    return float(round(res,6))