class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):

    # checks to see if the buffer is at its max capacity
    if len(self.storage) == self.current:
      # self.storage.pop(0)
      self.current = 0
    self.storage[self.current] = item
    self.current += 1


  def get(self):
    #set variables for looping
    x = self.storage[0]
    i = 0

    #while loop to check if the index value is None
    while x != None and i <= len(self.storage) -1:
      x = self.storage[i]
      i += 1

    if x != None:
      return self.storage

    return self.storage[0:i-1:]

# class FullRingBuffer:
#   def __init__(self):


#   def append(self, item):
#     self.storage[self.current] = item
#     self.current = (self.current + 1) % self.capacity

#   def get(self):
#     return self.storage[self.current:] + self.storage[:self.current]