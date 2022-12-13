import pytest
import sys
sys.path.append("\\".join(__file__[:__file__.find('_test_')-1].split("\\")))

from example02.function02 import prod_array



def test_foo_bar1():
   array = [1,2,3,4,5,6]
   assert prod_array(array) == 720

def test_foo_bar2():
   array = [1,7,3,4,5,6]
   assert prod_array(array) == 2520

def test_foo_bar3():
   array = [1,2,3,4,5,6]
   assert prod_array(array) != 22

def test_foo_bar4():
   array = [10,2,3,4,5,6]
   assert prod_array(array) != 1


if __name__ == "__main__":
    test_foo_bar1()