# Airline Sentiment Analysis

Airline Sentiment Analysis is a sentiment analysis web application built with Python.  
It classifies tweets related to airlines as positive, negative, or neutral.

## Features

- **Data Preprocessing:** Cleans and prepares text data for analysis.
- **Machine Learning:** Utilizes TF-IDF vectorization and Logistic Regression to classify tweet sentiments.
- **Interactive Web App:** Built with Streamlit for a user-friendly interface.
- **Visualization:** Provides graphs such as confusion matrices to evaluate model performance.

## Project Structure

    .
    ├── data/
    │   └── Tweets.csv              # Dataset file
    ├── model_training.ipynb        # Notebook for model training and evaluation
    ├── sentiment_app.py            # Streamlit web application
    ├── model.pkl                   # Saved trained model (generated after training)
    ├── tfidf_vectorizer.pkl        # Saved TF-IDF vectorizer (generated after training)
    ├── requirements.txt            # List of dependencies
    └── README.md                   # This file

## Installation
Clone the Repository:


1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/airline-sentiment-analysis.git
   cd airline-sentiment-analysis
   ```
   
2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

   - Activate the virtual environment:

      - **Windows:** ```venv\Scripts\activate```
      - **macOS/Linux:** ```source venv/bin/activate```
   

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
   
5. **Download the Dataset:**

   Place the ```Tweets.csv``` file inside the ```data/``` folder.
   You can use the [Twitter US Airline Sentiment dataset](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment)
 or another similar dataset.


## Model Training

   1. Open ```model_training.ipynb``` in Jupyter Notebook or JupyterLab.
   2. Run all the cells to train the model.
   3. The trained model and TF-IDF vectorizer will be saved as ```model.pkl``` and ```tfidf_vectorizer.pkl```.

### Running the Web Application

   1. Run the following command in your terminal
   
   ```bash
   streamlit run sentiment_app.py
   ```
   
   2. A browser window will open with the web interface.
   3. Enter a tweet or review in the text area and click the Analyze button to see the sentiment prediction.

## Usage

   - **Input:** Type or paste a tweet/review in the provided text area.
   - **Action:** Click the "Analyze" button.
   - **Output:** The application displays the predicted sentiment (positive, negative, or neutral).

## Dependencies

   - Python 3.9+
   - Pandas
   - NumPy
   - scikit-learn
   - Streamlit
   - Joblib
   - Matplotlib
   - Seaborn
   - NLTK
 
## Contributing
Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
   - [Kaggle](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment) for providing the dataset.
   - [Streamlit](https://streamlit.io/) for the amazing web application framework.
