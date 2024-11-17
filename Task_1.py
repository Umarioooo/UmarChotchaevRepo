numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_without_none = sum(x for x in numbers if x is not None)

count_with_none = len(numbers)
mean_value = round(sum_without_none / (count_with_none), 2)
numbers[numbers.index(None)] = mean_value
print("Измененный список:", numbers)
