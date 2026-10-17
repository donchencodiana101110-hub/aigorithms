# Задача 1. FizzBuzz


N = int(input("Введите N:"))

fizz = 0 
buzz = 0
fizzbuzz = 0 

for i in range(1,N+1):
    if i % 15 == 0:
        fizzbuzz += 1
        print("FizzBuzz")
    elif i % 3 == 0:
        fizz += 1
        print("Fizz")
    elif i % 5 == 0:
        buzz += 1
        print("Buzz")
    else:
        print(i)

print("Fizz", fizz)
print("Buzz", buzz)
print("FizzBuzz", fizzbuzz)


# Задача 2. Таблица умножения

A = int(input("Введите A:"))
B = int(input("Введите B:"))

for i in range(A,B + 1):
    for j in range(A,B + 1):
     print(i*j, end="\t")
print()



# Задача 3. Цифры числа


N = int(input("Введите число:"))

original = N 
count = 0 
summ = 0
reverse = 0 

while N > 0:
    digit = N % 10
    count += 1
    summ += digit
    reverse = reverse * 10 + digit
    N //= 10

print("Количество цифр:", count)
print("Сумма цифр:", summ)
print("Число в обратном порядке:", reverse)



 # Лекция № 2.


# Задание 1. 

def selection_sort(nums):
    nums = list(nums)

    for i in range(len(nums)):
         max_index = i

         for j in range(i+1,len(nums)):
             if nums[j] > nums[max_index]:
                 max_index = j

         nums[i], nums[max_index] = nums[max_index], nums[i]

    return nums
grades = [4,2,5,3,5,4,3]

print("По убыванию:", selection_sort(grades))



# Задание 2.

def count_items(nums):
     if nums == []:
         return 0 

     return 1 + count_items(nums[1:])

numbers = [10,20,30,40,50]

print("Количество элементов:", count_items(numbers))
print("Количество элементов:", count_items([]))



# Задание 3.

phone_book = {
   "John": "123-456-7890",
   "Alice": "987-654-3210",
   "Diana": "555-123-4567",
   "Sam": "111-222-3333",
   "Max": "584-837-9837"
}

name = input("Введите имя контакта: ")

if name in phone_book:
   print(f"Номер телефона {name}: {phone_book[name]}")
else:
   print("Контакт не найден.")


# Задание 4.

from collections import deque

graph = {
   "A": ["B", "C"],
   "B": ["D", "E"],
   "C": ["A","F"],
   "D": ["B","G"],
   "E": ["B","H"],
   "F": ["C","H"],
   "G": ["D"],
   "H": ["E","F"]

}

start = "A"
goal = "H"

queque = deque([start])
visited = set()
order = []

while queque:
   vertex = queque.popleft()
   order.append(vertex)

   if vertex == goal:
      break

   for neighbor in graph[vertex]:
      if neighbor not in visited:
         visited.add(neighbor)
         queque.append(neighbor)

print("Порядок проверки вершин:", order)
print("Цель найдена:", goal in visited)

