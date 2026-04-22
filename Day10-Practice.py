#PROG2: Comparing size & creation time of list & tuple
import timeit
import sys
list1: list[int] = [i for i in range(100)]
tuple1: tuple[int] = tuple(list1)
print(f"Size of List: {sys.getsizeof(list1)} bytes")
print(f"Size of Tuple: {sys.getsizeof(tuple1)} bytes")
print(f"Time taken to create List: {timeit.timeit('list1 = [i for i in range(100)]', number=10000)} seconds")
print(f"Time taken to create Tuple: {timeit.timeit('tuple1 = tuple([i for i in range(100)])', number=10000)} seconds")

#PROG5: Union set operation
school_friends: list[str] = ["Alice", "Bob", "Charlie", "David"]
college_friends: list[str] = ["Eve", "Alice", "Charlie", "David"]
def all_unique_friends(*friend_lists):
    return list(set().union(*friend_lists))
unique_friends = all_unique_friends(school_friends, college_friends)
print("Unique Friends:", unique_friends)