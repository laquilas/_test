import numpy as np

def sum_array(array):
    return np.sum([array])

def prod_array(array):
    return np.prod([array])



if __name__ == "__main__":
   
   array  = [10,20,30,40,50,60]
   print(sum_array(array))
   print(prod_array(array))
