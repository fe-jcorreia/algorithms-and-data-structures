from heap import Heap

class TestHeap():
  def run_all_tests(self):
    self.test_insert_on_heap()
    self.test_sift_up()
    self.test_get_min()
    self.test_get_size()
    self.test_is_empty_heap()
    self.test_extract_min()
    self.test_sift_down()
    self.test_remove_from_heap()
    self.test_heapify()
  
  def test_insert_on_heap(self):
    heap = Heap()

    heap.insert_on_heap(15)
    heap.insert_on_heap(10)
    heap.insert_on_heap(24)
    heap.insert_on_heap(46)
    heap.insert_on_heap(30)
    heap.insert_on_heap(99)
    heap.insert_on_heap(342)
    heap.insert_on_heap(64)
    heap.insert_on_heap(87)
    heap.insert_on_heap(1)
    heap.insert_on_heap(12)
    heap.insert_on_heap(17)

    assert heap.heap_list[0] == 1
    assert heap.heap_list[1] == 10
    assert heap.heap_list[2] == 17
    assert heap.heap_list[3] == 46
    assert heap.heap_list[4] == 12
    assert heap.heap_list[5] == 24
    assert heap.heap_list[6] == 342
    assert heap.heap_list[7] == 64
    assert heap.heap_list[8] == 87
    assert heap.heap_list[9] == 30
    assert heap.heap_list[10] == 15
    assert heap.heap_list[11] == 99

    assert heap.length == 12

    print("Test insert_on_heap: OK")
  
  def test_sift_up(self):
    heap = Heap()

    heap.heap_list.append(45)
    heap.heap_list.append(27)
    heap.heap_list.append(18)
    heap.heap_list.append(67)
    heap.heap_list.append(90)
    heap.heap_list.append(76)
    heap.heap_list.append(13)
    heap.heap_list.append(14)
    heap.length = 8

    heap.sift_up(6)
    assert heap.heap_list[0] == 13
    heap.sift_up(7)
    assert heap.heap_list[1] == 14

    print("Test sift_up: OK")

  def test_get_min(self):
    heap = Heap()

    heap.insert_on_heap(30)
    heap.insert_on_heap(99)
    heap.insert_on_heap(342)
    heap.insert_on_heap(64)
    heap.insert_on_heap(87)
    heap.insert_on_heap(15)

    assert heap.heap_list[0] == 15

    print("Test get_min: OK")

  def test_get_size(self):
    heap = Heap()

    heap.insert_on_heap(15)
    heap.insert_on_heap(15)
    assert heap.get_size() == 2
    heap.insert_on_heap(24)
    heap.insert_on_heap(46)
    assert heap.get_size() == 4

    print("Test get_size: OK")
  
  def test_is_empty_heap(self):
    heap = Heap()

    assert heap.is_empty_heap() == True
    heap.insert_on_heap(15)
    assert heap.is_empty_heap() == False

    print("Test is_empty_heap: OK")
  
  def test_extract_min(self):
    heap = Heap()

    heap.insert_on_heap(15)
    heap.insert_on_heap(10)
    heap.insert_on_heap(24)
    heap.insert_on_heap(46)
    heap.insert_on_heap(30)
    heap.insert_on_heap(99)
    heap.insert_on_heap(342)
    heap.insert_on_heap(64)
    heap.insert_on_heap(87)
    heap.insert_on_heap(1)
    heap.insert_on_heap(12)
    heap.insert_on_heap(17)

    assert heap.extract_min() == 1
    assert heap.extract_min() == 10
    assert heap.extract_min() == 12
    assert heap.length == 9 
    
    print("Test extract_min: OK")

  def test_sift_down(self):
    heap = Heap()

    heap.heap_list.append(45)
    heap.heap_list.append(27)
    heap.heap_list.append(18)
    heap.heap_list.append(67)
    heap.heap_list.append(90)
    heap.heap_list.append(76)
    heap.heap_list.append(13)
    heap.heap_list.append(14)
    heap.length = 8

    heap.sift_down(0)
    assert heap.heap_list[0] == 18
    assert heap.heap_list[2] == 13
    assert heap.heap_list[6] == 45

    heap.sift_down(3)
    assert heap.heap_list[3] == 14
    assert heap.heap_list[7] == 67

    print("Test sift_down: OK")

  def test_remove_from_heap(self):
    heap = Heap()

    heap.insert_on_heap(15)
    heap.insert_on_heap(10)
    heap.insert_on_heap(24)
    heap.insert_on_heap(46)
    heap.insert_on_heap(30)
    heap.insert_on_heap(99)
    heap.insert_on_heap(342)
    heap.insert_on_heap(64)
    heap.insert_on_heap(87)
    heap.insert_on_heap(1)
    heap.insert_on_heap(12)
    heap.insert_on_heap(17)

    heap.remove_from_heap(1)

    assert heap.heap_list[1] == 12
    assert heap.heap_list[4] == 15
    assert heap.heap_list[3] == 46
    assert heap.length == 11

    print("Test remove_from_heap: OK")
  
  def test_heapify(self):
    heap = Heap()

    heap.heap_list.append(14)
    heap.heap_list.append(45)
    heap.heap_list.append(27)
    heap.heap_list.append(13)
    heap.heap_list.append(18)
    heap.heap_list.append(67)
    heap.heap_list.append(90)
    heap.heap_list.append(76)
    heap.length = 8

    heap.heapify()

    assert heap.heap_list[0] == 13
    assert heap.heap_list[1] == 14
    assert heap.heap_list[2] == 27
    assert heap.heap_list[3] == 45
    assert heap.heap_list[4] == 18
    assert heap.heap_list[5] == 67
    assert heap.heap_list[6] == 90
    assert heap.heap_list[7] == 76

    print("Test heapify: OK")
