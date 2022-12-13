import numpy as np

def max_value(array):
    return np.max(array)

def min_value(array):
    # Test
    return np.min(array)
    
if __name__ == "__main__":
    array = [1,2,3,4,5,6]
    print(max_value(array))
    print(min_value(array))