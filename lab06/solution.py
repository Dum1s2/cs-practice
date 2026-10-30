def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    
    for path in paths:
        filename = path.split('/')[-1]
        if '.' in filename and not filename.startswith('.'):
            extension = filename.split('.')[-1].lower()
        else:
            extension = ''
        
        if extension not in result:
            result[extension] = 1
        else:
            result[extension] += 1
    
    return result


def deepest_path(paths: list[str]) -> str:
    deepest = ""
    max_depth = -1

    for path in paths:
        depth = path.count('/')
        
        if depth > max_depth:
            max_depth = depth
            deepest = path
        elif max_depth == depth:
            if path < deepest:
                deepest = path
            
    return deepest

def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    unit_index = 0
    
    while n_bytes >= 1024 and unit_index < len(units) - 1:
        n_bytes /= 1024
        unit_index += 1
    
    if unit_index == 0 :
        return f'{n_bytes} Б'
    else:
        return f'{n_bytes:.1f} {units[unit_index]}' 
