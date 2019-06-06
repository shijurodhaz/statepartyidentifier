# PartyCity
PartyCity is a Twitter party recognition algorithm that attempts to predict a state's political stance based off of tweets from users within that state. This is a team Final Project for EECS 486: Information Retrieval at the University of Michigan.


## Table of Contents
* [Introduction](#introduction)
* [Running the Project](#running-the-project)
* [Topic Classifier Model](#topic-classifier-model)
* [Training Model](#training-model)
* [Testing Model](#testing-model)
* [Contributors](#contributors)


## Introduction
PartyCity is a Twitter party recognition algorithm that attempts to predict a state's political stance based off of tweets from users within that state. The algorithm is mainly split into two separate modules: [training](#training-model) and [testing](#testing-model). More information on each of these modules can be found below.

In order to make our algorithm more accurate, we create separate classifiers for several political "topics". For example, if a tweet is determined to be about 'Education', then we will use classifiers built for Liberal: Education vs Conservative: Education rather than a generalized Liberal vs Conservative classifier. To choose these topics, we looked at the most important issues among voters for the 2016 Presidential Election using data from [Pew Research Center](https://www.people-press.org/2016/07/07/4-top-voting-issues-in-2016-election/).


## Running the Project
First, you'll need to clone the repo and install the python package.
```
git clone https://gitlab.eecs.umich.edu/bsuth/partycity.git
cd partycity
pip3 install -e .
```
If you don't want to install the partycity to your system, you can also use a virtual environment (after `cd partycity`):
```
python3 -m venv env
source .env/bin/activate # this may vary based on your shell
pip install -e .
```
Note that if you install using a virtual environment, then you will have to rerun `source .env/bin/activate` whenever the virtual environment is deactivated (this happens automatically when you exit the shell).

To run the program, simply run:
```
partycity
```


## Topic Classifier Model
This is a module that, given a piece of text, will determine the topic of that text from a predetermined list. The possible topics are as follows:

* Economy
* Terrorism
* Foreign Policy
* Health Care
* Gun Policy
* Immigration
* Social Security
* Education
* Trade Policy
* Environment
* Abortion
* LGBTQ Treatment
* None of the Above

Since we will be creating party classifiers for each topic, our topic classifier is required when training our party recognition algorithm (to know which party classifier to train for a particular training set). The topic classifier is also required when scraping tweets to determine whether a given tweet is relevant and which party classifier to use in evaluation.

#### Algorithm
###### Choosing Topics
To choose the above topics, we looked at the most important issues among voters for the 2016 Presidential Election using data from [Pew Research Center](https://www.people-press.org/2016/07/07/4-top-voting-issues-in-2016-election/). Note that we have chosen to leave out some topics, due to lack of relevance to current issues (ex. Supreme Court Appointments).
###### Training the Classifier
`NOTE:` UPDATE THIS AFTER CLASSIFIER IS PROGRAMMED

#### File Structure
```
NOTE: REPLACE ME WITH THE OUTPUT FROM:
$ tree topic_classification
```


## Training Model
`NOTE:` Update training description when output format is more formulated.

#### Algorithm
###### Web Scraping/Preprocessing
Training data is retrieved by scraping the web. Debate transcripts from General, Democratic and Republic debates are fetched from [here](https://www.presidency.ucsb.edu/documents/presidential-documents-archive-guidebook/presidential-candidates-debates-1960-2016?fbclid=IwAR2xkzSTf8ygEfraZ-lac6ta-rDYya3jfmSKVZVMTWBWHDWAbkHcu2EwGc8) and preprocessed to remove unnecessary html elements and tags, remove stopwords, and stem words. Preprocessed files are then output to a separate directory to be read by the main training algorithm (train.py).
###### Training
Using the output from the previous section as training data, a dictionary of terms and values (such as term frequency and document frequency) are formed, which is then in turn used to construct the following classifiers:
	* Naive Bayes (Multinomial vs Bernoulli)
	* Decision Trees
	* Rocchio Text Classification
	* Nearest Neighbour

#### File Structure
```
training/
├── __init__.py
├── keywords.py
├── preprocess.py
├── setup.py
└── train.py
```


## Testing Model
`NOTE:` SUMMARY HERE

Ex) This module scrapes tweets from a given state and uses the output from the training module to determine whether a state is more liberal or conservative.

#### Algorithm
`NOTE:` ALGORITHM HERE

#### File Structure
```
NOTE: REPLACE ME WITH THE OUTPUT FROM:
$ tree topic_classification
```


## Contributors
#### Topic Classifier
* Shameek Ray (shameek)
#### Training
* Brian Sutherland (bsuth)
* Nikita Badhwar (nbadhwar)
#### Testing
* Rodney Shibu (rodneyss)
* Sreeraj Marar (sreerajm)
