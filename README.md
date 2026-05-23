# 🎬 Movie Recommender System

An end-to-end content-based movie recommendation engine built with Python, Machine Learning, and Streamlit. The system processes raw film metadata to construct semantic tag profiles for thousands of movies, maps them into a high-dimensional vector space, and calculates similarity metrics to recommend the top 5 closest matches for any selected title.

🚀 **Live App Link:** [https://movie-recommender-hk4zb9wwcubr6h8ruksyad.streamlit.app/](https://movie-recommender-hk4zb9wwcubr6h8ruksyad.streamlit.app/)

---

## 📌 Development Process & Core Pipeline

The project implements a complete data-to-production engineering cycle divided into four primary stages:

```text
[Raw Datasets] ➔ [Metadata Extraction & Cleaning] ➔ [NLP Stemming & Vectorization] ➔ [Similarity Indexing & Deployment]
1. Metadata Extraction & Feature EngineeringStarting with the raw TMDB metadata and credits datasets, individual entities were thoroughly preprocessed:JSON Parsing: Extracted relevant strings out of stringified JSON objects within rows (such as converting nested dictionaries of movie genres and keywords into plain lists of descriptive words).Feature Selection: Filtered down columns to isolate attributes directly impacting narrative context: genres, keywords, overview, cast (top 3 actors), and crew (extracting only the Director).Whitespace Normalization: Stripped spaces inside entity names (e.g., transforming Sam Worthington to SamWorthington) to ensure the tokenizer treats full names as a single unique token rather than split entities.2. Natural Language Processing (NLP)To build clean semantic profiles, all extracted text tokens were unified into a comprehensive string of tags per movie:Lowercasing: Standardized text strings to lowercase to prevent duplications across variable casing profiles.Porter Stemming: Applied algorithmic stemming via nltk to reduce words to their root forms (e.g., mapping actions, acting, and action down to a single index feature action).3. Text Vectorization & ModelingHigh-Dimensional Mapping: Implemented a Bag-of-Words model via Scikit-Learn's CountVectorizer, expanding feature boundaries to extract the top 7,000 most frequent unique words across the dataset while filtering out standard English stop words.Matrix Computation: Constructed a dense $4806 \times 7000$ matrix representing word frequency vectors for every individual movie title.Cosine Similarity Scoring: Evaluated direction-based similarity vectors rather than standard Euclidean distance. By computing the dot product and magnitude angles between movie vectors via cosine_similarity, the system created a static similarity index matrix mapping every film against all others.⚠️ Challenges Faced & Engineering Fixes1. Bypassing GitHub's Strict 100 MB File LimitThe Problem: The final calculated cosine similarity matrix (similarity.pkl) came out to a massive 176.22 MB, causing GitHub's pre-receive hook checks to completely reject pushing code updates to the remote repository.The Solution: Implemented an array segmentation technique via NumPy. The large array was mathematically bisectioned into two clean individual chunks (similarity_part1.pkl and similarity_part2.pkl), dropping their individual file sizes down to 88.11 MB (well under the strict tracking limit). These segments are systematically re-joined using np.concatenate() on the fly right when the Streamlit application container initializes on the server.2. Git CR/LF Text Translation File CorruptionThe Problem: During initial dataset updates, Git attempted to run text normalization line-ending configurations on all untracked files. This metadata translation process corrupted the binary file serialization inside the pickle formats, breaking the app on deployment with an untraceable EOFError.The Solution: Added explicit environment configuration tracking by building a local .gitattributes file at the root folder level containing the configuration *.pkl binary. This explicitly locks down all pickle extensions, telling Git to strictly track them as raw binary data stream objects and freeze translation edits.

🗂️ Repository Layout
├── data/
│   ├── tmdb_5000_credits.csv         # Raw credits data attributes
│   └── tmdb_5000_movies.csv          # Raw movie narrative records
├── .gitattributes                    # Locks .pkl files as pure binary entities
├── .gitignore                        # Standard version control rules
├── app.py                            # Interactive Streamlit frontend UI engine
├── movie-recommender-system.ipynb   # Analytical data science prototyping workbook
├── movies_dict.pkl                   # Processed dataframe converted to serializable dictionary
├── requirements.txt                  # Python dependency configuration stack
├── similarity_part1.pkl              # Top half segment of the cosine similarity matrix
└── similarity_part2.pkl              # Bottom half segment of the cosine similarity matrix

🛠️ Tech Stack Used
Language: Python

Data Processing: Pandas, NumPy

Machine Learning & NLP: Scikit-Learn (CountVectorizer), NLTK (PorterStemmer)

Deployment & UI: Streamlit Framework

APIs: Requests (Live movie poster lookups powered via remote TMDB API handshakes)

