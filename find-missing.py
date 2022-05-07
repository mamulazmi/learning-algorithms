def findMissing(numbers):
    lengthNumbers = len(numbers)

    subtotal = (lengthNumbers + 1) * ( lengthNumbers + 2) / 2

    return subtotal - sum(numbers)


def sum(numbers):
    if len(numbers) < 1:
        return 0
    else:
        return numbers.pop() + sum(numbers)

numbers = [1, 2, 3, 4, 5]


print(findMissing(numbers))