# PROGRAMMING PA2
This Assignment contains 
- Normalization Problem
- Divisble by 3 Problem




# The project generates a 5x5 random matrix (ndarray).
It then normalizes the matrix by centering (subtracting the mean) and scaling (dividing by the standard deviation) the data.
The normalized matrix is saved as a file named X_normalized.npy.

## Divisible by 3 Problem:

The project creates a 10x10 matrix containing the squares of the first 100 positive integers.
It identifies all elements in this matrix that are divisible by 3.
The result is saved in a file named div_by_3.npy.

####  Why the Project Is Useful
Normalization: Normalization is a critical preprocessing step in data analytics and machine learning, ensuring that data features are on a similar scale, which can improve the performance of many algorithms.
Divisibility Check: Identifying numbers divisible by a certain value is a basic yet powerful operation, especially in filtering data sets or applying conditional operations.

#### How Users Can Get Started with the Project
To get started with this project:

Clone or download the project files.
Run the provided Python scripts for each problem:
normalization.py (or similar name) to generate and normalize the matrix.
divisible_by_3.py (or similar name) to create the matrix and filter elements divisible by 3.

The generated .npy files (X_normalized.npy and div_by_3.npy) can be loaded into any Python script using np.load('filename.npy') for further analysis or use.

## Authors
Rosario, Clifford James
