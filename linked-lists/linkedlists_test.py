import pytest
from linkedlists import SinglyLinkedList

class TestSinglyLinkedList:
  def test_insert_at_head(self):
    test = SinglyLinkedList()
    test.insert_at_head('test0')
    assert test._head.value == 'test0'
    test.insert_at_head('test1')
    assert test._head.value == 'test1'
    assert test._head.next.value == 'test0'
    assert len(test) == 2

  def test_is_empty(self):
    test = SinglyLinkedList()
    assert test._head == None
    assert test.is_empty == True
    test.insert_at_head('test0')
    assert test.is_empty == False

  def test_insert(self):
    test = SinglyLinkedList()
    test.insert_at_index('test0', 0)
    assert test._head.value == 'test0'
    test.insert_at_index('test1',0)
    assert test._head.value == 'test1'
    assert test._head.next.value == 'test0'
    assert len(test) == 2

  def test_length(self):
    test = SinglyLinkedList()
    assert len(test) == 0
    test.insert_at_index('test0', 0)
    assert len(test) == 1
    test.insert_at_head('test1')
    assert len(test) == 2
    assert test.delete_at_index(0) == 'test1'
    assert len(test) == 1

  def test_node_at_index(self):
    test = SinglyLinkedList()
    test.insert_at_head('test0')
    assert test._node_at_index(0) is test._head
    test.insert_at_head('test1')
    assert test._node_at_index(0).value == 'test1'
    assert test._node_at_index(1).value == 'test0'

  def test_value_at_index(self):
    test = SinglyLinkedList()
    test.insert_at_head('test0')
    test.insert_at_head('test1')
    assert test.value_at_index(0) == 'test1'
    assert test.value_at_index(1) == 'test0'

  def test_insert_at_tail(self):
    N = 5
    test = SinglyLinkedList()
    for i in range(0,N):
      test.insert_at_tail('test' + str(i))
    for i in range(0,N):
      assert test.value_at_index(i) == 'test' + str(i)
    assert len(test) == N

  def test_str(self):
    N = 5
    test = SinglyLinkedList()
    for i in range(0,N):
      test.insert_at_head('test' + str(i))
    assert str(test) == "['test4', 'test3', 'test2', 'test1', 'test0']"

  def test_delete_at_index(self):
    N = 5
    test = SinglyLinkedList()
    for i in range(0, N): test.insert_at_head('test' + str(i))
    assert test.delete_at_index(0) == 'test4'
    assert len(test) == N - 1
    assert test.delete_at_index(1) == 'test2'
    assert len(test) == N - 2
    with pytest.raises(IndexError):
      test.delete_at_index(3)
    assert test.value_at_index(0) == 'test3'
    assert test.value_at_index(1) == 'test1'
    assert test.value_at_index(2) == 'test0'

  def test_index_out_of_bounds(self):
    test = SinglyLinkedList()
    assert test._index_out_of_bounds(-1) == True
    assert test._index_out_of_bounds(0) == True
    assert test._index_out_of_bounds(1) == True
    test.insert_at_head('test0')
    assert test._index_out_of_bounds(-1) == True
    assert test._index_out_of_bounds(0) == False
    assert test._index_out_of_bounds(1) == True

  def test_delete_at_head(self):
    test = SinglyLinkedList()
    with pytest.raises(IndexError):
      test.delete_at_head()
    for i in range(0, 2): test.insert_at_head('test' + str(i))
    assert test.delete_at_head() == 'test1'
    assert len(test) == 1
    assert test.delete_at_head() == 'test0'
    assert len(test) == 0
    
    