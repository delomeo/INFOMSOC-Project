import pandas as pd
import matplotlib.pyplot as plt
import re
import string

data = pd.read_csv('./archive/english_data_with_locations.csv')

classes = {
    'Need': ['emergency', 'urgent', 'stranded', 'trapped', 'stuck', 'need', 'require', 'request', 'seeking', 'missing', 'seek', 'suffering', 'desperate', 'homeless'],
    'Offer': ['provide', 'volunteer', 'offer', 'available', 'rescue', 'assisting', 'extend', 'lend', 'pitch in', 'contribute', 'give', 'supportive'],
    'News': ['earthquake', 'magnitude', 'aftershock', 'recovery', 'update', 'latest'],
    'Funding': ['fundraiser', 'donation', 'charity', 'fund', 'support', 'contribute', 'financial aid'],
    'Survivor stories': ['survivor', 'personal account', 'experience', 'impact', 'narrative', 'testimonial', 'journey'],
    'Volunteering': ['volunteer', 'helping', 'aid', 'support', 'contribute', 'community', 'service', 'dedicate'],
    'Political response': ['government', 'political', 'action', 'response', 'official', 'policy', 'decision'],
    'Humanitarian aid': ['humanitarian', 'aid', 'relief', 'support', 'assistance', 'donation', 'charitable'],
    'Casualty reports': ['injury', 'death', 'fatal', 'missing', 'victims', 'fatalities', 'casualties', 'affected'],
    'Infrastructure damage': ['building', 'bridge', 'road', 'power', 'water', 'gas', 'telecommunications', 'structural', 'damaged', 'utility'],
    'Emergency services': ['ambulance', 'fire', 'police', 'emergency', 'rescue', 'paramedics', 'firefighters', 'law enforcement'],
    'Prayer and condolences': ['prayer', 'thoughts', 'condolences', 'sympathy', 'grief', 'comfort', 'mourning'],
    'International aid': ['international', 'donor', 'relief', 'support', 'assistance', 'global', 'humanitarian'],
    'Personal safety': ['safety', 'evacuation', 'shelter', 'protection', 'precaution', 'security', 'secure', 'safe']
}





def preprocess_text(text):
    if pd.isna(text):
        return ''
    # Remove URLs
    text = re.sub(r'http\S+', '', text)

    # Remove mentions and hashtags
    text = re.sub(r'@\w+|#\w+', '', text)

    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()

    # Remove extra whitespace
    text = re.sub('\s+', ' ', text).strip()

    return text

def classify_tweet(tweet_text):
    for class_name, keywords in classes.items():
        for keyword in keywords:
            if keyword in tweet_text:
                return class_name
    return 'Other'  # If no keyword matches, label as "Other"

# Add a new column to the dataframe with the class label for each tweet
data['content'] = data['content'].apply(preprocess_text)
data['classification'] = data['content'].apply(classify_tweet)

print(len(data[data['classification'] != "Other"]))



data.to_csv('translated_dataset3_2.csv', index=False)

# Create a bar plot of the class distribution
class_counts = data['classification'].value_counts()
class_counts.plot(kind='bar')
plt.title('Class Distribution of Tweet Data')
plt.xlabel('Class')
plt.ylabel('Number of Tweets')
plt.show()

