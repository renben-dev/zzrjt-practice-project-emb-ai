from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        res_1 = sentiment_analyzer("I love working with python")
        self.assertEqual(res_1['label'], 'SENT_POSITIVE')

        res_2 = sentiment_analyzer("I hate working with python")
        self.assertEqual(res_2['label'], 'SENT_NEGATIVE')

        res_3 = sentiment_analyzer("I am ok with python")
        self.assertEqual(res_3['label'], 'SENT_NEUTRAL')


unittest.main()

