def sum(numbers):
    if len(numbers) < 1:
        return 0
    else:
        return numbers.pop() + sum(numbers)
        
print(sum([1, 2, 3, 1]))