"""Module for calculating average"""


def calculate_average(nums):
    """Function returning average for a list of numbers"""
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average


numbers = [10, 15, 20]
result = calculate_average(numbers)
print("The average is:", result)
