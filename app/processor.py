import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

class processor:
    def __init__(self, df = None):
        self.df = df

    def rarest_word(self, tweet):
        words = tweet.split()
        words_dict = dict()
        lowest = 100
        rarest = ''
        for w in words:
            if w in words_dict:
                words_dict[w] += 1
            else:
                words_dict[w] = 1
            if words_dict[w] < lowest:
                lowest = words_dict[w]
                rarest = w
        return rarest

    def tweet_sentiment(self, tweet):
        score = SentimentIntensityAnalyzer().polarity_scores(tweet)
        high = 0
        result = ''
        for k in score.keys():
            if score[k] > high:
                high = score[k]
                result = k
        sentiment = result.replace('neg', 'negative').replace('pos', 'positive').replace('neu', 'neutral')

        return sentiment

    def check_weapon(self, tweet):
        words = tweet.split()
        with open("C:/Users/israel/Desktop/data/hostile-tweets-ex/data/weapon_list.txt", 'r') as f:
            weapons = f.read()
        weapon_list = weapons.split('\n')
        found = ''
        for w in words:
            if w in weapon_list:
                found = w
                return found
        return found

    def get_processing(self, document):
        rarest_word = self.rarest_word(document['Text'])
        sentiment = self.tweet_sentiment(document['Text'])
        weapons_detected = self.check_weapon(document['Text'])
        result = {'id': str(document['_id']),
                  'original text': document['Text'],
                  'rarest_word': rarest_word,
                  'sentiment': sentiment,
                  'weapons_detected': weapons_detected}
        return result
