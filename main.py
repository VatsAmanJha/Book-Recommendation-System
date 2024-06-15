from fastapi import FastAPI, HTTPException
from typing import List, Optional
import pandas as pd
import numpy as np
import pickle
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data and functions
with open("pt.pkl", "rb") as f:
    pt = pickle.load(f)
with open("books.pkl", "rb") as f:
    books = pickle.load(f)
with open("similarity_scores.pkl", "rb") as f:
    similarity_scores = pickle.load(f)
with open("popular_df.pkl", "rb") as f:
    popular_df = pickle.load(f)


def recommend(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True
    )[1:5]
    recommended_books = []
    for i in similar_items:
        book_details = books[books["Book-Title"] == pt.index[i[0]]]
        recommended_books.append(book_details.iloc[0])
    recommended_df = pd.DataFrame(recommended_books)
    recommended_df.drop_duplicates("Book-Title", inplace=True)
    recommended_df = recommended_df[["Book-Title", "Book-Author", "Image-URL-M"]]
    return recommended_df


class BookName(BaseModel):
    book_name: str


@app.get("/popular_df", response_model=List[dict])
async def get_popular_df():
    """
    Endpoint to get popular_df data.
    """
    return popular_df.to_dict(orient="records")


@app.post("/recommendations/", response_model=List[dict])
async def get_recommendations(book_data: BookName):
    """
    Endpoint to get book recommendations based on a given book name using POST method and request body.
    """
    book_name = book_data.book_name
    if book_name not in pt.index:
        raise HTTPException(status_code=404, detail="Book not found")
    
    recommendations = recommend(book_name)
    return recommendations.to_dict(orient="records")
