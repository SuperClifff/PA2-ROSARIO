# PROGRAMMING PA2
## Overview
##### NORMALIZATION PROBLEM: 
- Normalize a 5x5 ndarray by centering and scaling it, and save the result.
##### DIVISIBLE BY 3 PROBLEM: 
- Create a 10x10 ndarray of squares of the first 100 positive integers, identify elements divisible by 3, and save the results.

# NORMALIZATION PROBLEM 
#### Obejective: 
Create a random 5x5 ndarray and normalize it.
#### STEPS:
1. Generate a 5x5 random ndarray and store it in variable X.
2. Normalize X using the formula:
𝑍 = x-x/𝜎
3. Save the normalized ndarray as X_normalized.npy

# DIVISIBLE BY 3 PROBLEM
#### Objective:
Create a 10x10 ndarray of squares of the first 100 positive integers and find elements divisible by 3.
#### Steps:
1. Create a 10x10 ndarray where each element is the square of integers from 1 to 100.
2. Identify elements in this ndarray that are divisible by 3.
3. Save the result as div_by_3.npy.

####  Why the Project Is Useful
##### Normalization: 
Normalization is a critical preprocessing step in data analytics and machine learning, ensuring that data features are on a similar scale, which can improve the performance of many algorithms.
##### Divisibility Check: 
Identifying numbers divisible by a certain value is a basic yet powerful operation, especially in filtering data sets or applying conditional operations.


## Files
##### normalization_and_divisibility.ipynb: 
- Jupyter Notebook containing the Python code to solve the problems.
##### X_normalized.npy: 
- Output file containing the normalized 5x5 ndarray.
##### div_by_3.npy: 
- Output file containing elements divisible by 3 from the 10x10 ndarray.
Problem Descriptions

#### How Users Can Get Started with the Project
To get started with this project:

Clone or download the project files.
Run the provided Python scripts for each problem:
normalization.py (or similar name) to generate and normalize the matrix.
divisible_by_3.py (or similar name) to create the matrix and filter elements divisible by 3.

The generated .npy files (X_normalized.npy and div_by_3.npy) can be loaded into any Python script using np.load('filename.npy') for further analysis or use.

### Author
##### Rosario, Clifford James
##### 2ECE-C
