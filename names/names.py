import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.count = 1
   
  def __str__(self):
      return 'value: {0}, count: {1}'.format(self.value, self.count)

def insert(root, value):
    if not root:
        return BinarySearchTree(value)
    elif root.value == value:
        root.count += 1
    elif value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root

def create(seq):
    root = None
    for word in seq:
        root = insert(root, word)

    return root

def search(root, word, depth=1):
    if not root:
        return False
    elif root.value == word:
        return True
    elif word < root.value:
        return search(root.left, word, depth + 1)
    else:
        return search(root.right, word, depth + 1)


tree = create(names_1)
for name in names_2:
  if search(tree,name) != False:
    duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# duplicates = []
# start_time = time.time()
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")
