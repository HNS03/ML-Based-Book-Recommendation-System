# Machine Learning Based Book Recommendation System

## Overview

This project implements a book recommendation system using collaborative filtering techniques. The system utilizes the NearestNeighbors algorithm from scikit-learn to recommend books based on user ratings. The dataset used includes information about books, users, and ratings, and is processed to create a matrix that forms the basis of recommendations.

## Technologies Used

**Python**: Core programming language used for data processing and model implementation.
**Pandas, NumPy**: Libraries used for data manipulation and analysis.
**Matplotlib, Seaborn**: Used for data visualization.
**Scikit-learn**: Machine learning library for implementing the NearestNeighbors algorithm.
**Pickle**: Used for model serialization and storage.

## Datasets

**Books**: Contains details about books such as ISBN, Title, Author, Year of Publication, Publisher, and Image URL.
**Users**: Contains user information.
**Ratings**: Contains book ratings provided by users.

## Project Workflow

**1. Data Preprocessing:**
Cleaned and selected relevant features from the datasets.
Renamed columns for better readability.
Filtered users based on a minimum threshold of ratings.
Merged datasets to create a unified dataset of books and their ratings by users.

**2. Modeling:**
Created a pivot table of books vs. users and filled NaN values with zeros.
Converted the pivot table into a sparse matrix for memory efficiency.
Trained a NearestNeighbors model using the sparse matrix.

**3. Recommendations:**
Implemented a function to recommend books based on a given book name.
The function returns similar books based on user ratings.

