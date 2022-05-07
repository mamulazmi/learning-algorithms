def sum(numbers):
    total = 0
    if len(numbers) < 1:
        return 0
    else:
        total += numbers.pop() + sum(numbers)
    return total
        
print(sum([1,2,3]))