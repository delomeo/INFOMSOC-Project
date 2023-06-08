import pandas as pd
import matplotlib.pyplot as plt
import re
import string
data = pd.read_csv('translated_dataset2.csv')

classes = {
    'Help': ['help', 'assistance', 'support', 'donate'],
    'News': ['earthquake', 'magnitude', 'aftershock', 'rescue', 'recovery'],
    'Funding': ['fundraiser', 'donation', 'charity', 'fund'],
    'Survivor stories': ['survivor', 'personal account', 'experience', 'impact'],
    'Volunteering': ['volunteer', 'helping', 'aid', 'support'],
    'Political response': ['government', 'political', 'action', 'response'],
    'Humanitarian aid': ['humanitarian', 'aid', 'relief', 'support'],
    'Casualty reports': ['injury', 'death', 'fatal', 'missing', 'victims'],
    'Infrastructure damage': ['building', 'bridge', 'road', 'power', 'water', 'gas', 'telecommunications'],
    'Emergency services': ['ambulance', 'fire', 'police', 'emergency', 'rescue'],
    'Prayer and condolences': ['prayer', 'thoughts', 'condolences', 'sympathy'],
    'International aid': ['international', 'donor', 'aid', 'relief'],
    'Personal safety': ['safety', 'evacuation', 'shelter', 'protection', 'precaution']
}



def preprocess_text(text):
    # Remove URLs
    text = re.sub(r'http\S+', '', text)

    # Remove mentions and hashtags
    text = re.sub(r'@\w+|#\w+', '', text)

    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()

    # Remove extra whitespace
    text = re.sub('\s+', ' ', text).strip()

    return text
# Define a function to label each tweet based on its content
def classify_tweet(tweet_text):
    for class_name, keywords in classes.items():
        for keyword in keywords:
            if keyword in tweet_text:
                return class_name
    return 'Other'  # If no keyword matches, label as "Other"

# Add a new column to the dataframe with the class label for each tweet
data['translated_content'] = data['translated_content'].apply(preprocess_text)
data['classification'] = data['translated_content'].apply(classify_tweet)

print(len(data[data['classification'] != "Other"]))



data.to_csv('translated_dataset3.csv', index=False)

# Create a bar plot of the class distribution
class_counts = data['classification'].value_counts()
class_counts.plot(kind='bar')
plt.title('Class Distribution of Tweet Data')
plt.xlabel('Class')
plt.ylabel('Number of Tweets')
plt.show()

