# Movie Recommender System

An end-to-end content-based movie recommendation engine built using Python, NLP, Machine Learning, and Streamlit.  
The system analyzes movie metadata, constructs semantic tag representations, transforms them into high-dimensional vectors, and computes cosine similarity scores to recommend the Top 5 most similar movies for any selected title.

---

## Live Demo

Streamlit App:  
https://movie-recommender-hk4zb9wwcubr6h8ruksyad.streamlit.app/

---

# Project Overview

This project implements a complete data engineering → NLP → ML → deployment pipeline using the TMDB 5000 Movies Dataset.

The recommender system works by:

- Extracting important movie metadata
- Building semantic tag profiles
- Applying NLP preprocessing techniques
- Converting text into vector embeddings
- Computing cosine similarity between movies
- Serving recommendations through an interactive Streamlit UI

---

# Recommendation Pipeline

```text
Raw TMDB Dataset
        │
        ▼
Metadata Extraction & Cleaning
        │
        ▼
NLP Processing & Stemming
        │
        ▼
Count Vectorization (7000 Features)
        │
        ▼
Cosine Similarity Matrix
        │
        ▼
Top-5 Movie Recommendations
        │
        ▼
Streamlit Deployment
```

---

# Development Workflow

## 1. Metadata Extraction & Feature Engineering

The system starts with two raw datasets:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

### Key preprocessing operations:

### JSON Parsing

Several columns contained stringified JSON objects. These were converted into usable structured lists.

Examples:
- Genres
- Keywords
- Cast
- Crew

---

### Feature Selection

Only high-impact narrative features were retained:

| Feature | Purpose |
|---|---|
| Genres | Movie category understanding |
| Keywords | Core semantic themes |
| Overview | Story description |
| Cast (Top 3) | Actor-based similarity |
| Director | Creative style similarity |

---

### Whitespace Normalization

Entity names were merged into single tokens:

```python
Sam Worthington → SamWorthington
```

This prevents token fragmentation during vectorization.

---

# NLP Processing

After preprocessing, all textual attributes were merged into a single tag profile per movie.

Example:

```text
action adventure alien war future samworthington jamescameron
```

---

## Text Normalization

### Lowercasing

```python
Action → action
ACTION → action
```

Ensures consistent vocabulary indexing.

---

## Porter Stemming (NLTK)

Applied stemming using:

```python
from nltk.stem.porter import PorterStemmer
```

Examples:

```text
actions → action
acting → act
actors → actor
```

This significantly reduces redundant vocabulary dimensions.

---

# Vectorization & Machine Learning

## Count Vectorization

Implemented using:

```python
CountVectorizer(max_features=7000, stop_words='english')
```

### Output:

- Top 7000 most frequent words extracted
- English stop words removed
- Sparse semantic feature matrix generated

---

## Matrix Dimensions

```text
4806 Movies × 7000 Features
```

Each movie becomes a high-dimensional vector representation.

---

## Cosine Similarity

Similarity between movies is computed using:

```python
cosine_similarity()
```

Instead of Euclidean distance, cosine similarity compares vector direction:

\[
\text{similarity}(A,B)=\frac{A \cdot B}{||A|| \times ||B||}
\]

This produces more accurate semantic recommendations.

---

# Recommendation Engine Logic

For a selected movie:

1. Retrieve its vector
2. Compute similarity scores against all movies
3. Sort scores in descending order
4. Return Top 5 most similar titles

---

# Streamlit Frontend

The deployment layer is built with Streamlit.

### Features:
- Interactive movie selection
- Instant recommendation generation
- Dynamic poster fetching via TMDB API
- Lightweight and responsive UI

Run locally:

```bash
streamlit run app.py
```

---

# Engineering Challenges & Solutions

# 1. GitHub 100 MB File Limit

## Problem

The generated similarity matrix:

```text
similarity.pkl = 176.22 MB
```

GitHub rejected pushes due to its strict file size limit.

---

## Solution

The similarity matrix was split into two parts:

```text
similarity_part1.pkl
similarity_part2.pkl
```

Each chunk:

```text
≈ 88 MB
```

At runtime, both files are reconstructed using:

```python
np.concatenate()
```

This bypassed GitHub’s upload restrictions cleanly.

---

# 2. Git Binary File Corruption (CRLF Translation)

## Problem

Git attempted line-ending normalization on `.pkl` files, corrupting binary serialization and causing:

```text
EOFError
```

during deployment.

---

## Solution

A `.gitattributes` file was added:

```gitattributes
*.pkl binary
```

This forces Git to treat pickle files as raw binary streams and prevents unwanted text translation.

---

# Project Structure

```text
├── data/
│   ├── tmdb_5000_credits.csv
│   └── tmdb_5000_movies.csv
│
├── app.py
├── movie-recommender-system.ipynb
├── movies_dict.pkl
├── similarity_part1.pkl
├── similarity_part2.pkl
├── requirements.txt
├── .gitattributes
├── .gitignore
└── README.md
```

---

# Tech Stack

| Category | Technologies |
|---|---|
| Language | Python |
| Data Processing | Pandas, NumPy |
| NLP | NLTK |
| ML | Scikit-Learn |
| Vectorization | CountVectorizer |
| Similarity Metric | Cosine Similarity |
| Deployment | Streamlit |
| API Integration | TMDB API + Requests |

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

---

# Future Improvements

- Hybrid recommendation system
- Collaborative filtering integration
- Deep learning embeddings
- User authentication
- Watchlist functionality
- Real-time recommendation optimization
- Cloud database integration
- Docker containerization
- CI/CD deployment pipeline

---

# Preview

Add application screenshots here.

Example:

```markdown
![App Screenshot](images/app.png)
```

---

# Acknowledgements

- TMDB Dataset
- Scikit-Learn Documentation
- NLTK Documentation
- Streamlit Framework

---

# License

This project is licensed under the MIT License.

---

# Author

**Yug Birla**

- LinkedIn: [Add your LinkedIn](https://www.linkedin.com/in/yug-birla-4b17b4321/)
- GitHub: [Add your GitHub profile](https://github.com/yug-birla)

---
