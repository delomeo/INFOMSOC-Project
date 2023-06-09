import pandas as pd

import swifter
from transformers import MarianMTModel, MarianTokenizer
from geotext import GeoText
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

data = pd.read_csv('translated_dataset.csv')
from googletrans import Translator


def dest_text(text):
    return GeoText(text).cities

x = 0
def trans(text):
    trans = translation.translate(text)
    global x
    x += 1
    if( x % 100 == 0):
        print(x)
        
    return trans



turkish_tweets = data[data['language'] == 'tr']
turkish_tweets = turkish_tweets[turkish_tweets['city_mention'] != '[]']

#turkish_tweets['translated_hashtags'] = turkish_tweets['hashtags'].apply(translate_text)

#data.to_csv('translated_dataset2.csv', index=False)
# Import Argos Translate modules
import argostranslate.package
import argostranslate.translate


from_code = "tr"
to_code = "en"

# Download and install Argos Translate package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
available_package = list(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)[0]
download_path = available_package.download()
argostranslate.package.install_from_path(download_path) 

# Translate
installed_languages = argostranslate.translate.get_installed_languages()
from_lang = list(filter(
        lambda x: x.code == from_code,
        installed_languages))[0]
to_lang = list(filter(
        lambda x: x.code == to_code,
        installed_languages))[0]
translation = from_lang.get_translation(to_lang)
text = "Merhaba dünya"

df = turkish_tweets

df['translated_content'] = df['content'].swifter.apply(lambda x: translation.translate(x))
df.to_csv('translated_dataset2.csv', index=False)

print(len(df))