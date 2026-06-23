# Program 1 (Create a Tuple)

fruits = ("Apple", "Banana","Mango")

print(fruits)


# Program 2 (Access Tuple Items)

fruits = ("Apple", "Banana", "Mango")

print(fruits[0])
print(fruits[1])
print(fruits[2])


#  Program 3 (Tuple Length)

fruits = ("Apple", "Banana","Mango", "Orange")

print(f"Length: {len(fruits)}")


# Program 4 (Count value in Tuple)

numbers = (10, 30, 20, 10 ,10 , 40)

print(numbers.count(10))


# Program 5 (Find Index in Tuple)

fruits = ("Apple", "Mango", "Banana", "Cherry")

print(fruits.index("Mango"))


# Program 6 (List vs Tuple)

fruits_list = ["Apple", "Banana", "Mango","Cherry"]
fruits_tuple = ("Apple", "Banana", "Mango", "Cherry")

print(f"List: {fruits_list}")
print(f"Tuple: {fruits_tuple}")


# Program 7 (Tuple Practice)

anime = ("One Piece", "Tokyo Ghoul", "AOT", "JJK", "Black Clover","AOT", "Erased")

print(f"Original Tuple: {anime}")
print(f"Length: {len(anime)}")
print(f"Count of AOT: {anime.count('AOT')}")
print(f"Index of JJK: {anime.index('JJK')}")

print(f"First anime: {anime[0]}")
print(f"Last anime: {anime[-1]}")