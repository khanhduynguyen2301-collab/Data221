def distribution_analysis(numbers):
    distribution_dictionary = {}
    for number in sorted(set(numbers)):
        counting = sum(1 for element in numbers if element <= number)
        distribution_dictionary[number] = (counting / len(numbers)) * 100
    return distribution_dictionary

numbers = [3, 1, 2, 3, 4, 2]
print(distribution_analysis(numbers))