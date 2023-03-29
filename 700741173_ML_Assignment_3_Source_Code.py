#!/usr/bin/env python
# coding: utf-8

#Question-1a

import numpy as np

# create a random vector of size 15 with integers in the range of 1-20
random_vector = np.random.randint(1, 20, size=15)

# reshape the array to 3 by 5
random_vector = random_vector.reshape(3, 5)

# print the array shape
print("Array Shape:", random_vector.shape)
print("Before Update:\n",random_vector)

# replace the max in each row by 0
random_vector[np.arange(len(random_vector)), np.argmax(random_vector, axis=1)] = 0

# print the updated array
print("Updated Array:\n", random_vector)

# create a 2-dimensional array of size 4 x 3
array_2d = np.zeros((4, 3), dtype=np.int32)

# print the shape, type, and data type of the array
print("\nArray Shape:", array_2d.shape)
print("Array Type:", type(array_2d))
print("Array Data Type:", array_2d.dtype)


#=========================================================================================================================================


# Question-1b


import numpy as np

# define the square array
arr = np.array([[3, -2], [1, 0]])

# compute the eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(arr)

# print the eigenvalues and right eigenvectors
print("Eigenvalues: ", eigenvalues)
print("Right Eigenvectors: \n", eigenvectors)


#=========================================================================================================================================


# Question-1c

import numpy as np

# define the array
arr = np.array([[0, 1, 2], [3, 4, 5]])

# compute the sum of the diagonal elements
sum_of_diagonal = np.trace(arr)
print(arr)
# print the sum of the diagonal elements
print("Sum of the diagonal elements: ", sum_of_diagonal)


#=========================================================================================================================================


# Question-1d


import numpy as np

# create the original array
original_array = np.array([[1, 2], [3, 4], [5, 6]])

# reshape the array to 2x3
reshaped_array = np.reshape(original_array, (2, 3))

# print the original and reshaped arrays
print("Original array:\n", original_array)
print("Reshaped array:\n", reshaped_array)


#=========================================================================================================================================


#Question-2(2.1,2.2)

import matplotlib.pyplot as plt

# define the data
languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# find the index of the language with the highest popularity
highest_popularity_index = popularity.index(max(popularity))

# create the explode list
explode = [0] * len(languages)
explode[highest_popularity_index] = 0.1

# create the pie chart with the explode parameter and set the startangle
plt.pie(popularity, labels=languages, explode=explode, autopct='%1.1f%%', startangle=140)

# set the title
plt.title("Popularity of Programming Languages")

# show the plot
plt.show()




