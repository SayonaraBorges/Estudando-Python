for value in range(1,6):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,15,3))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
    #squares.append(value**2)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

squares_2 = [value**2 for value in range(1,11)]
print(squares_2)
