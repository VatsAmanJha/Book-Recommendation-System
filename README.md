# Book Recommendation System

This project implements a book recommendation system that leverages both popularity-based and collaborative filtering techniques. It includes a backend API built with FastAPI and a web-based user interface for easy interaction.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Web Interface](#web-interface)
- [Recommendation Systems](#recommendation-systems)
- [Results](#results)
- [Contributing](#contributing)

## Introduction

The Book Recommendation System suggests books to users based on their preferences and the popularity of books. It utilizes a dataset containing information about books, user ratings, and user details to generate recommendations.

## Dataset

The dataset comprises three main files:

- **Dataset Url**: https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset
- **Books.csv**: Contains details about books such as ISBN, title, author, year of publication, and publisher.
- **Ratings.csv**: Contains user ratings for different books.
- **Users.csv**: Contains demographic information about users such as user ID, location, and age.

## Installation

To set up the project, follow these steps:

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/VatsAmanJha/Book-Recommendation-System.git
   cd book-recommendation-system
   ```

2. **Install Dependencies**: 
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare the Dataset**: Ensure that the dataset files (`Books.csv`, `Ratings.csv`, `Users.csv`) are in the project directory.
   
2. **Start the FastAPI Server**: 
   ```bash
   uvicorn main:app --reload
   ```

3. **Access the Web Interface**: Open `index.html` in your browser to interact with the recommendation system.

## API Endpoints

The FastAPI backend provides the following endpoints:

- **Get Popular Books**: Retrieve a list of popular books.
  - **Endpoint**: `/popular_df`
  - **Method**: `GET`
  - **Response**: JSON list of popular books with their titles, authors, and image URLs.

- **Get Recommendations**: Get book recommendations based on a given book name.
  - **Endpoint**: `/recommendations/`
  - **Method**: `POST`
  - **Request Body**: JSON object with a `book_name` field.
  - **Response**: JSON list of recommended books with their titles, authors, and image URLs.

## Web Interface

The web interface allows users to select a book from a list of popular books and get recommendations for similar books. It is built using HTML, Bootstrap for styling, and JavaScript for making API calls.

### Features

- **Dropdown Menu**: Displays a list of popular books fetched from the backend.
- **Get Recommendations Button**: Triggers an API call to get book recommendations based on the selected book.
- **Recommendation Display**: Shows the recommended books with their titles, authors, and cover images.

## Recommendation Systems

### Popularity-Based Recommender System

This system recommends books that are popular among users. It ranks books based on the number of ratings and the average rating score.

### Collaborative Filtering Based Recommender System

This system uses user ratings to find books that are similar to the ones the user likes. It employs a pivot table and cosine similarity to identify and recommend books that have similar rating patterns.

## Results

The recommendation system provides effective book suggestions based on user preferences and book popularity. Users can access these recommendations through the API endpoints or the web interface.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to suggest improvements or report bugs.
