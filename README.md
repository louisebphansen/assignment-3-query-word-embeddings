# Assignment 3 - Query expansion with word embeddings

This assignment is the third assignment for the portfolio exam in the Language Analytics course at Aarhus University, spring 2024.

### Contributions
All code was created by me, but code provided in the notebooks for the course has been reused. 

### Assignment description

Write a script which does the following:

- Loads the song lyric data
- Downloads/loads a word embedding model via ```gensim``` (see below)
- Takes a given word as an input and finds the most similar words via word embeddings
- Find how many songs for a given artist feature terms from the expanded query
- Calculate the percentage of that artist's songs featuring those terms
- Print and/or save results in an easy-to-understand way
    - For example, "45% of {ARTIST}'s songs contain words related to {SEARCH TERM}"

### Contents of the repository


| <div style="width:120px"></div>| Description |
|---------|:-----------|
| ```out``` | Contains the output txt files with results from the query search.|
| ```src```  | Contains the Python script for performing the query expansion on a desired artist and search term. |
| ```run.sh```    | Bash script for running the code. |
| ```setup.sh```  | Bash script for setting up virtual environment. |
| ```requirements.txt```  | Packages required to run the code|

### Methods
This repository contains the code to perform a search on words related to a given search term in a given artist's songs. More specifically, the ```src/song_search.py``` script finds the 10 most similar words to a given search term based on cosine similarities of word embeddings calculated by the *"glove-wiki-gigaword-50"* model. The chosen search term and the 10 most similar words are then used in a word search in each of the artist's song. The script outputs a txt file containing the percentage amount of songs by the artist containing the search term and words related to it. 

### Data
The project uses a dataset of 57,650 songs and their lyrics.

### Usage

All code for this assignment was designed to run on an Ubuntu 22.04 operating system using Python version 3.10.12. It is therefore not guaranteed that it will work on other operating systems.

It is important that you run all code from the main folder, i.e., *assignment-3-query-word-embeddings-louisebphansen*. Your terminal should look like this:

```
--your_path-- % assignment-3-query-word-embeddings-louisebphansen %
```

#### Set up virtual environment
To run the code in this repository, clone it using ```git clone```.

In order to set up the virtual environment, the *venv* package for Python needs to be installed first:

```
sudo apt-get update

sudo apt-get install python3-venv
```

Next, run:

```
bash setup.sh
```

This will create a virtual environment in the directory (```env```) and install the required packages to run the code.

#### Download data
Download the dataset from Kaggle [(link)](https://www.kaggle.com/datasets/joebeachcapital/57651-spotify-songs?resource=download) and unzip it. 

Create a new folder in the main directory called ```in``` and place the csv file here. 

#### Run code

To run the code, you can do the following:

##### Run script with predefined arguments

To run the code in this repo with predefined/default arguments, run:
```
bash run.sh
```

This will activate the virtual environment and run the ```src/song_search.py``` with default arguments (artist: ABBA, search term: love). The output from this can be found in the 'out' folder.

##### Define arguments yourself

Alternatively, the script can be run with different arguments:

```
# activate the virtual environment
source env/bin/activate

python3 src/song_search.py --artist <artist> --search_term <search_term>

```

**Arguments:**

- **Artist:** What artist to search for. Default: ABBA
- **Search_term:** Search term to find related words to and search for in the song lyrics. Default: love

### Results

An example of an output txt file can be found in ```out```. When searching for 'ABBA' and 'love', this is the result:

***94.0% of ABBA's songs contain words related to 'love'***