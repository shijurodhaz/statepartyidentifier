import os
TOPIC_DIR = os.path.dirname(__file__)
TRAINING_DIR = os.path.join(TOPIC_DIR, 'training_data/')

from partycity.topic_classification.train import create_naive_bayes
from partycity.topic_classification.data_gen import data_gen
from partycity.topic_classification.preprocess import ppTweet
