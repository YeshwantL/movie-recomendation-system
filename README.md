# 🎬 Movie Recommendation System

A simple content-based movie recommendation system built using **Python**, **Pandas**, **Scikit-Learn**, and **TF-IDF Vectorization**.
The system recommends movies similar to the user’s favorite movie based on metadata such as **genres**, **keywords**, **tagline**, **cast**, and **director**.

---

## 📌 Features

* Uses **TF-IDF Vectorizer** to convert movie metadata into numerical features.
* Computes **cosine similarity** to measure closeness between movies.
* Accepts a movie name from the user and suggests the **top 5 similar movies**.
* Uses **difflib** to match misspelled or partly typed movie names.
* Handles missing values in movie metadata.

---

## 📂 Dataset

The program uses a CSV file named **`movies.csv`**.
The file must contain at least the following columns:

```
index
title
genres
keywords
tagline
cast
director
```

---

## 🧠 How It Works

1. Load the dataset using Pandas.
2. Select important textual features:

   * Genres
   * Keywords
   * Tagline
   * Cast
   * Director
3. Fill null values with empty strings.
4. Combine these features into one text column for each movie.
5. Convert text into numerical vectors using **TfidfVectorizer**.
6. Calculate **cosine similarity** between all movies.
7. Take user input and find the closest movie title using **difflib**.
8. Recommend the top 5 most similar movies.

---

## ▶️ Usage

1. Place `movie_recommender.py` and `movies.csv` in the same folder.
2. Install required libraries:

```bash
pip install pandas numpy scikit-learn
```

3. Run the script:

```bash
python movie_recommender.py
```

4. Enter your favorite movie name when prompted:

```
enter your favourite movie name: avatar
```

5. The program will output:

```
Top 5 similar movies to avatar are:
Movie 1
Movie 2
Movie 3
Movie 4
Movie 5
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* difflib

---

## 🚀 Future Improvements

* Add a web interface using Flask or FastAPI
* Add JSON-based API
* Use word embeddings (Word2Vec, BERT) for better recommendations
* Display movie posters and descriptions using external APIs (TMDb)

---

