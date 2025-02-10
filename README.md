# airplane_sentiment
# Airline Sentiment Analysis

Airline Sentiment Analysis is a sentiment analysis web application built with Python. The application classifies tweets related to airlines as positive, negative, or neutral. This project showcases skills in data preprocessing, machine learning model training, and creating interactive web applications using Streamlit.

## Features

- **Data Preprocessing:** Cleans and prepares text data for analysis.
- **Machine Learning:** Utilizes TF-IDF vectorization and Logistic Regression to classify tweet sentiments.
- **Interactive Web App:** Provides a user-friendly interface built with Streamlit.
- **Visualization:** Includes visualizations (e.g., confusion matrix) to evaluate model performance.

## Project Structure

. ├── data/ │ └── Tweets.csv # Dataset file ├── model_training.ipynb # Notebook for model training and evaluation ├── sentiment_app.py # Streamlit web application ├── model.pkl # Saved trained model (generated after training) ├── tfidf_vectorizer.pkl # Saved TF-IDF vectorizer (generated after training) ├── requirements.txt # List of dependencies └── README.md # This file

bash
Copy
Edit

## Installation

**Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/airline-sentiment-analysis.git
   cd airline-sentiment-analysis
Set Up a Virtual Environment:

bash
Copy
Edit
python -m venv venv
Activate the virtual environment:
Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Download the Dataset:

Place the Tweets.csv file inside the data/ folder.
You can use the Twitter US Airline Sentiment dataset or another similar dataset.
Model Training
Open model_training.ipynb in Jupyter Notebook or JupyterLab.
Run all the cells to train the model.
The trained model and TF-IDF vectorizer will be saved as model.pkl and tfidf_vectorizer.pkl.
Running the Web Application
Run the following command in your terminal:
bash
Copy
Edit
streamlit run sentiment_app.py
A browser window will open with the web interface.
Enter a tweet or review in the text area and click the Analyze button to see the sentiment prediction.
Usage
Input: Type or paste a tweet/review in the provided text area.
Action: Click the "Analyze" button.
Output: The application displays the predicted sentiment (positive, negative, or neutral).
Dependencies
Python 3.9+
Pandas
NumPy
scikit-learn
Streamlit
Joblib
Matplotlib
Seaborn
NLTK
Contributing
Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Kaggle for providing the dataset.
Streamlit for the amazing web application framework.
Copy
Edit

Цей файл README.md містить основну інформацію про проект, його структуру, інструкції з встан
