

print('foo\nbar')

print(r'foo\nbar')

print('foo\\bar')

print(R'foo\\bar')

var = ['Pandas', 'NumPy', 'Scikit Learn']
print(var)
print(var[0])

List = [['Python', 'Java'], ['C']]
print(List[0][1])
print(List[1][0])

list1 = ("welcome to the real world")
string = list1.split(' ')
print(string)

List = [1,2,3,4]
print("Initial List: ")
print(List)
 # Addition of Element at
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, 14)
print("\nList after performing Insert Operation: ")
print(List)

List = [1, 2, 3, 4, 5]
 # Removing element from the list using the pop() method
List.pop()
print("\nList after popping an element: ")
print(List)
# Removing element at a specific location from the list using the pop() method
List.pop(2)
print("\nList after popping a specific element: ")
print(List)

# Creating a Tuple with the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

# Creating a Tuple
# with the use of built-in function
Tuple1 = tuple('Python')
print("\nTuple with the use of function: ")
print(Tuple1)


# Accessing Tuple with Indexing
tup = tuple('Python')
print("\nFirst element of Tuple: ")
print(tup)


 # Tuple unpacking
tup = ('Python', 'Java', 'C')
 # This line unpack values of tup
a, b, c = tup
print("\nValues after unpacking: ")
print(a)
print(b)
print(c)

# Concatenation of tuples
tup_1 = (0, 1, 2, 3)
tup_2 = ('Python', 'Java', 'C')
tup_3 = tup_1 + tup_2
print(tup_3)

# Creating a Dictionary with Integer Keys
dict = {1: 'Python', 2: 'Java', 3: 'C'}
print("\nDictionary with the use of Integer Keys: ")
print(dict)

# Creating a Dictionary with Mixed keys
dict = {'Name': 'Python' , 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(dict)




# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
# Adding elements one at a time
Dict[0] = 'Python'
Dict[2] = 'Java'
print("\nDictionary after adding 2 elements: ")
print(Dict)

Dict = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

print(Dict)
Dict[4]='hello'
print(Dict.get(4))
print(Dict.items())
print(Dict.keys())
print(Dict.values())
print(Dict.get(1))

# Creating a Set
my_set = set()
print("Initial blank Set: ")
print(my_set)
# Adding element and tuple to the Set
my_set.add(8)
my_set.add(9)
my_set.add((6, 7))
print("\nSet after Addition of Three elements: ")
print(my_set)
# Adding elements to the Set  using Iterator
for i in range(1, 6):
    my_set.add(i)
print("\nSet after Addition of elements from 1-5: ")
print(my_set)



my_set = set(["Python", "Java", "C"])
print("\nInitial set")
print(my_set)
# Accessing element using for loop
print("\nElements of set: ")
for i in my_set:
    print(i, end=" ")
# Checking the element using in keyword


print("Python" in my_set)



# Creating a Set
my_set = set([1, 2, 3, 4, 5, 6])
print("Initial Set: ")
print(my_set)
# Removing elements from Set using Remove() method
my_set.remove(5)
print("\nSet after Removal of one elements: ")
print(my_set)
# Removing elements from Set using Discard() method
my_set.discard(6)
print("\nSet after Discarding one elements: ")
print(my_set)
# Removing elements from Set using iterator method
for i in range(1, 3):
    my_set.remove(i)
print("\nSet after Removing a range of elements: ")
print(my_set)

my_set = set([1, 2, 3, 4, 5, 6])
print("Initial Set: ")
print(my_set)

# Removing element from the Set using the pop() method
my_set.pop()
print("\nSet after popping an element: ")
print(my_set)


# importing "array" for array creations
import array as arr
# creating an array with integer type
a = arr.array('i', [1, 2, 3])
# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()
# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])
# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 3):
    print (b[i], end =" ")



# importing "array" for array creations
import array as arr
# array with int type
a = arr.array('i', [1, 2, 3])
print ("Array before insertion : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()
# inserting array using insert() function
a.insert(1, 4)
print ("Array after insertion : ", end =" ")
for i in (a):
    print (i, end =" ")
print()



# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])
print ("Array before insertion : ", end =" ")
for i in range (0, 3):
    print (b[i], end =" ")
print()
# adding an element using append()
b.append(4.4)
print ("Array after insertion : ", end =" ")
for i in (b):
    print (i, end =" ")
print()





