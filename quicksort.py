def quicksort(numbers):
    if len(numbers) < 2:
        return numbers
    else:
        pivot = numbers[0]

        less = [i for i in numbers[1:] if i <= pivot]
        greater = [i for i in numbers[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 11, 30, 2, 5, 10, 11, 99, 19, 101]))