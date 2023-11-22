from textblob import TextBlob
import os

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def process_folder(folder_path, sentiment_label):
    files = os.listdir(folder_path)
    sentiment_scores = []

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        sentiment_score = analyze_sentiment(text)
        sentiment_scores.append(sentiment_score)

        # Print sentiment score for each file
        print(f"Sentiment score for {sentiment_label} file '{file_name}': {sentiment_score}")

    # Print sentiment score for overall file
    print(f"Average sentiment score for {sentiment_label} files: {sum(sentiment_scores) / len(sentiment_scores)}")

positive_folder_path = "/Users/darshilpatel/Desktop/txt_sentoken/pos"
negative_folder_path = "/Users/darshilpatel/Desktop/txt_sentoken/neg"

process_folder(positive_folder_path, "positive")
process_folder(negative_folder_path, "negative")
