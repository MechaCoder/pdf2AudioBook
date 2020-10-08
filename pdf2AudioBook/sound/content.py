
def normalise(content:str) -> list:
    c = content.split('.')
    return_obj = []
    for e in c:
        temp = ' '.join(e.split())
        return_obj.append(temp)
    return ''.join(return_obj)
