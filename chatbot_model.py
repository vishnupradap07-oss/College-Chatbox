import json
import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
DATA_PATH = os.path.join(os.path.dirname(__file__), 'chatbot_data.json')

with open(DATA_PATH, 'r') as f:
    data = json.load(f)

questions = [item['question'].lower() for item in data]
answers = [item['answer'] for item in data]

# Initialize and train the Vectorizer
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

def get_response(user_input):
    user_input = preprocess(user_input)
    
    if not user_input.strip():
        return "Please ask a question."
        
    user_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vector, question_vectors)
    
    max_sim = similarities[0].max()
    best_index = similarities[0].argmax()
    
    if max_sim >= 0.3:
        return answers[best_index]
    else:
        return "Sorry, I don't know that 😅"
