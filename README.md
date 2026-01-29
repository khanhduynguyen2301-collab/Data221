# DATA 221 Assignment 1 – Python Exercises

This repository contains solutions for Assignment 1 of the DATA 221 course. Each Python file corresponds to a single question and can be executed independently.

## File Structure

- `Question_1_Controlled_Multiplication_Loop.ipynb`  
  Uses a loop to multiply consecutive integers starting from `currentNumber = 1` while tracking `product` until it exceeds a predefined `threshold`. Outputs the final product and the integer that caused the threshold to be exceeded.


- `Question_2_Nested_Dictionary_from_Strings.ipynb`  
  Defines a function that processes a list of strings and returns a nested dictionary. Each string maps to a dictionary containing its `length` and its `parity` (`even` or `odd`).


- `Question_3_Safe_Function_Application.ipynb`  
  Defines a power function that computes `x ** y`. Iterates over a list of `(x, y)` pairs using argument unpacking, skips pairs where `y` is negative, and stores valid results in a list.


- `Question_4_Sorted_Search_with_Conditions.ipynb`  
  Generates a list of random values named `values`, sorts the list, and identifies all indices where elements are greater than or equal to a random threshold value `x`.


- `Question_5_Circle_Area_Comparison_with_Validation.ipynb`  
  Implements the function `circleAreaCoverage(radiusOfCircle1, radiusOfCircle2)`. The function validates that both `radiusOfCircle1` and `radiusOfCircle2` are positive integers, computes the areas of both circles, determines the `larger_area` and `smaller_area`, and returns the percentage of the larger area covered by the smaller area. Returns an error message for invalid input.


- `Question_6_Distribution_Analysis.ipynb`  
Implements the function `distribution_analysis(numbers)`, which computes a cumulative distribution over a list of numeric values. The function iterates over the sorted unique values in `numbers` and calculates, for each value, the percentage of elements in the original list that are less than or equal to that value. The result is returned as a dictionary sorted by key.


- `Question_7_Time_Conversion_Function.ipynb`  
    Defines a time conversion function that takes an integer representing the number of seconds since midnight. The function validates the input, converts the total seconds into hours, minutes, and seconds using integer division and modulo operations, determines whether the time is AM or PM, and returns a formatted string in the form `H M S AM/PM`.


- `Question_8_Pandas_DataFrame_with_Computed_Column.ipynb`  
  Uses the Pandas library to create a DataFrame from columns `A`, `B`, and `C`, adds a derived column computed from existing data, and prints the final DataFrame.

## Requirements
- Python 3 
- Pandas (required for Question 8)
