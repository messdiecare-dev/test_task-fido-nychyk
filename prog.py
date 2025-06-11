import random

def get_element(n):
    if not isinstance(n, int):
        return None
    
    if n > 1:
        return int(n*2/3) - 1
    
    return None

if __name__ == "__main__":
    n = random.randint(0, 100)
    list_ = list(range(n))

    index = get_element(n)

    print(f"Length of list: {n}")
    print(f"Index of element: {index}")
    print(f"Element by index: {list_[index]}")