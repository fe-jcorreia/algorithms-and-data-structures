import sys

class Heap():
  def __init__(self):
    self.heap_list = []
    self.length = 0
  
  def get_min(self):
    return self.heap_list[0]
  
  def get_size(self):
    return self.length
  
  def is_empty_heap(self):
    if(self.length):
      return False
    else:
      return True
    
  def sift_up(self, index: int):
    if index <= 0 or index >= self.length:
      return
    
    if self.heap_list[index] < self.heap_list[(index - 1) // 2]:
      aux = self.heap_list[(index - 1) // 2]
      self.heap_list[(index - 1) // 2] = self.heap_list[index]
      self.heap_list[index] = aux
      self.sift_up((index - 1) // 2)
  
  def insert_on_heap(self, value: int):
    self.heap_list.append(value)
    self.length += 1
    self.sift_up(self.length - 1)

  def sift_down(self, index: int):
    if index < 0 or index >= self.length:
      return
    
    min_index = index

    if (2*index) + 1 < self.length and self.heap_list[(2*index) + 1] < self.heap_list[min_index]:
       min_index = (2*index) + 1
    if (2*index) + 2 < self.length and self.heap_list[(2*index) + 2] < self.heap_list[min_index]:
       min_index = (2*index) + 2 

    if(self.heap_list[index] > self.heap_list[min_index]):
      aux = self.heap_list[min_index]
      self.heap_list[min_index] = self.heap_list[index]
      self.heap_list[index] = aux
      self.sift_down(min_index)
  
  def extract_min(self):
    max_value = self.heap_list[0]

    self.heap_list[0] = self.heap_list[self.length - 1]
    self.heap_list.pop()
    self.length -= 1

    self.sift_down(0)

    return max_value
    
  def remove_from_heap(self, index: int):
    self.heap_list[index] = -sys.maxsize - 1
    self.sift_up(index)
    self.extract_min()

  def heapify(self):
    for index in range((self.length - 1) // 2, -1, -1):
      self.sift_down(index)

  def print_heap(self):
    print(self.heap_list)
    
