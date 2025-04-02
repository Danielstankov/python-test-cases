def calculate_average(numbers):
    if not numbers:
        raise ValueError("Empty list")
    return sum(numbers) / len(numbers)