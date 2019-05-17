class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # checks to see if the buffer is at its max capacity
    if len(self.storage) == self.capacity:
      self.storage.pop(0)
      
    # appends the item at the end of the buffer
    self.storage.append(item)
    print("Appending to buffer. Buffer now: ", self.storage)


  def get(self):
    #set variables for looping
    x = None
    i = 0

    #while loop to check if the index value is None
    while x == None:
      x = array[i]
      i += 1

    print("Capacity is: ", self.capacity)
    print("Last index is: ", len(self.storage) - 1)
    return self.storage in range (i - 1, len(self.storage))