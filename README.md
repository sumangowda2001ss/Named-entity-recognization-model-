# Named Entity Recognition (NER) using SpaCy

## 📌 Project Overview
This project is a Named Entity Recognition (NER) model built using **SpaCy**. The model is trained on a custom dataset and deployed using **Flask** to provide an interactive web interface for entity extraction.

## 📂 Project Structure
```
├── ner_dataset.csv         # Labeled dataset for training the NER model
├── NER_Model_using_spacy.ipynb  # Jupyter Notebook for model training & evaluation
├── app.py                  # Flask application for NER inference
├── ner_model/              # Trained SpaCy NER model
├── templates/
│   ├── index.html          # Frontend for web app
├── static/
│   ├── style.css           # Styling for the web interface
├── requirements.txt        # Dependencies
├── Dockerfile              # Docker setup (if applicable)
├── README.md               # Project Documentation
```

## 📊 Dataset Explanation
The dataset `ner_dataset.csv` consists of labeled words with entity types:
- **Sentence #**: Groups words into sentences.
- **Word**: The actual token.
- **POS**: Part-of-Speech tag.
- **Tag**: Named entity label using BIO format (e.g., `B-PER`, `I-LOC`).

Example:
| Sentence # | Word     | POS  | Tag   |
|------------|---------|------|------|
| Sentence: 1 | Barack   | NNP  | B-PER |
| NaN        | Obama   | NNP  | I-PER |
| NaN        | visited | VBD  | O    |
| NaN        | London  | NNP  | B-LOC |

## 🚀 Model Training
We trained a SpaCy **custom NER model** using:
- Data preprocessing (stopword removal, lemmatization, tokenization).
- Converting labeled data into SpaCy's `DocBin` format.
- Splitting data into training and validation sets.
- Training a SpaCy pipeline with optimized hyperparameters.
- Evaluating model performance using precision, recall, and F1-score.
- Saving the trained model in `.spacy` and `.pkl` formats.

## 🌐 Web-Based Inference
The **Flask web interface** allows users to enter text and view extracted named entities in real-time.

### 🔧 How to Use the Web Interface
![Screenshot 2025-03-20 180810](https://github.com/user-attachments/assets/18abfb07-d928-4fcb-a982-245589f80fb1)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Flask app:
   ```bash
   python app.py
   ```
3. Open `http://127.0.0.1:5000/` in your browser.
4. Enter text in the provided input box and click **Analyze**.
5. View extracted entities and their types in the **Entity Visualization** section.

## 🐳 Docker Deployment (Optional)
1. Build the Docker image:
   ```bash
   docker build -t ner-app .
   ```
2. Run the container:
   ```bash
   docker run -p 5000:5000 ner-app
   ```

## 📌 Future Enhancements
- Improve dataset quality by adding more entity types.
- Deploy on **Heroku, AWS, or Google Cloud Run**.
- Use **Transformers (BERT-based NER)** for better accuracy.

## 🤝 Contributing
Feel free to fork this repository, create issues, and submit pull requests. Any contributions are welcome!

## 📜 License
This project is licensed under the MIT License.

