import typing
# Node class with only the next property
class _Node:
  def __init__(self, data = None):
    self._data = data
    self._next_node = None
  def __del__(self):
    del self._data
    del self._next_node 
  
  @property
  def value(self):
    return self._data
  
  @property
  def next(self):
    return self._next_node
    
  @next.setter
  def next(self, next_node):
    self._next_node = next_node


# Implementation of Singly Linked List with a Dummy Node
class SinglyLinkedList:
  def __init__(self):
      # Implement Dummy Node head feature
      self._head_node = None
      self._list_length = 0
  def __len__(self) -> int:
    return self._list_length
  def __del__(self):
    if self.is_empty:
      return
    else:
      #Add feature that deletes all nodes created
      raise NotImplementedError
  def __str__(self) -> str:
    current_node = self._head
    linked_list_string = '['
    while current_node != None:
      value = current_node.value
      if type(value) == str:
        linked_list_string += "\'" + value + "\'"
      else:
        linked_list_string += value
      if current_node.next != None:
        linked_list_string += ', '
      current_node = current_node.next
    linked_list_string += ']'
    return linked_list_string
  
  @property
  def _head(self):
    return self._head_node

  @_head.setter
  def _head(self, node):
    self._head_node = node

  @property
  def _length(self):
    return self._list_length
  @_length.setter
  def _length(self, n):
    self._list_length = n

  @property
  def is_empty(self):
    if len(self) == 0:
      return True
    else:
      return False
  
  # Inserts new node at specified index, the node inserted will take place of previous node at specified index
  def insert_at_index(self, data, index: int):
    if index < 0 or len(self) < index:
      raise IndexError('Index is out of bounds.')
    elif self.is_empty:
      self._head = _Node(data)
      self._length += 1
    elif index == 0:
      new_node = _Node(data)
      new_node.next = self._head
      self._head = new_node
      self._length += 1
    else:
      new_node = _Node(data)
      current_node = self._node_at_index(index - 1)
      new_node.next = current_node.next
      current_node.next = new_node
      self._length += 1

  # Delete node at desired index
  def delete_at_index(self, index: int):
    if self._index_out_of_bounds(index):
      raise IndexError('Index is out of bounds. Tried to delete index {}.'.format(index))
    elif index == 0:
      current_node = self._head
      data = current_node.value
      self._head = current_node.next
      del current_node
      self._length -= 1
      return data
    else:
      current_node = self._node_at_index(index - 1)
      delete_node = current_node.next
      data = delete_node.value
      current_node.next = delete_node.next
      del delete_node
      self._length -= 1
      return data

  # Insert node at the head node which puts the new node ahead of the previous head node
  def insert_at_head(self, data):
    # 0 is the start of the list and what head points to
    self.insert_at_index(data, 0)
  
  # Deletes the head node of the SinglyLinkedList
  def delete_at_head(self):
    if self._index_out_of_bounds(0):
      raise IndexError('Tried to delete from empty SinglyLinkedList.')
    else:
      current_node = self._head
      data = current_node.value
      self._head = current_node.next
      del current_node
      self._length -= 1
      return data

  # This is slow compared to Doubly Linked List since there is no tail reference
  # However, this method will be implemented anyways, avoid usage
  # It is a O(n) operation
  def insert_at_tail(self, data):
    if len(self) == 0:
      self.insert_at_index(data,0)
    else:
      new_node = _Node(data)
      current_node = self._node_at_index(len(self) - 1)
      current_node.next = new_node
      self._length += 1

  # Returns value stored in the node at desired index
  def value_at_index(self, index: int):
    if self._index_out_of_bounds(index):
      raise IndexError('Index is out of bounds. No value and node at this index.')
    else:
      value = self._node_at_index(index).value
      print(value)
      return value  

  # Helper method used to return the node object at desired index
  def _node_at_index(self, index: int) -> _Node:
    if self._index_out_of_bounds(index):
      raise IndexError('Index is out of bounds. No node at this index.')
    else:
      current_node = self._head
      for _ in range(0, index):
        current_node = current_node.next
      return current_node

  # This helper method is only for checking indexes when accessing nodes since it returns out of bounds for empty lists
  def _index_out_of_bounds(self, index: int) -> bool:
    if self.is_empty:
      return True
    elif index < 0 or len(self) - 1 < index:
      return True
    else:
      return False
