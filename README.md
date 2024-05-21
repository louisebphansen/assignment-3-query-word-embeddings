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
| ```out``` | Contains the output txt files with results from the expanded query search|
| ```src```  | Contains the Python script for performing the query expansion on a desired artist and search term |
| ```run.sh```    | Bash script for running the code with default arguments |
| ```setup.sh```  | Bash script for setting up virtual environment |
| ```requirements.txt```  | Packages required to run the code |
|```emissions```| Contains csv files with information about how much carbon is emitted when running the code, which is used for [Assignment 5](https://github.com/louisebphansen/assignment-5-evaluating-environmental-impact-louisebphansen)|

### Methods
This repository contains the code to perform an expanded query search using a chosen search term on a chosen artist's songs. More specifically, the ```src/song_search.py``` script uses util functions defined in ```src/search_utils.py``` to find the 10 most similar words to a given search term based on cosine similarities of word embeddings calculated using the ```gensim``` package and the *"glove-wiki-gigaword-50"* model. The chosen search term and the 10 most similar words are then used in a word search in each of the artist's song. The script outputs a txt file containing the percentage amount of songs by the artist containing the search term and words related to it. 

### Data
The project uses a dataset, *'Spotify Million Song Dataset_exported.csv'*, of 57,650 lyrics of songs from different artists. See more [here](https://www.kaggle.com/datasets/joebeachcapital/57651-spotify-songs).

### Usage

All code for this assignment was designed to run on an Ubuntu 24.04 operating system using Python version 3.12.2. It is therefore not guaranteed that it will work on other operating systems.

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

Create a new folder in the main directory called ```in``` and place the *'Spotify Million Song Dataset_exported.csv'* file here. 

#### Run code

To run the code, you can do the following:

##### Run script with predefined arguments

To run the code in this repo with predefined/default arguments, run:
```
bash run.sh
```

This will activate the virtual environment and run the ```src/song_search.py``` with default arguments (artist: ABBA, search term: love). The output from this can be found in the ```out``` folder.

##### Define arguments yourself

Alternatively, the script can be run with different arguments:

```
# activate the virtual environment
source ./env/bin/activate

python3 src/song_search.py --artist <artist> --search_term <search_term>

```

**Arguments:**

- **Artist:** What artist to search for. Default: ABBA
- **Search_term:** Search term to find related words to and search for in the song lyrics. Default: love

### Results

An example of an output txt file can be found in ```out```. When searching for 'ABBA' and 'love', this is the result:

***94.0% of ABBA's songs contain words related to 'love'***

### Discussion
In order to examine the results the code in this repository produce, I have used five common themes in popular music (as found in [this paper](https://journals.sagepub.com/doi/full/10.1177/0305735617748205)) as search terms for an expanded query search of ABBA's songs:

- 94.0% of ABBA's songs contain words related to 'love'

- 24.0% of ABBA's songs contain words related to 'desire'

- 15.0% of ABBA's songs contain words related to 'music'

- 15.0% of ABBA's songs contain words related to 'dancing'

- 2.0% of ABBA's songs contain words related to 'identity'

These results display a crude way of examining themes in a corpus of text, here music lyrics. They indicate that most of ABBA's songs are about more happy, 'lighter' topics, such as love, desire, music and dancing, and less about more heavy topics such as 'identity', as there are not many words related to this topic. It is interesting to see that almost all of ABBA's songs contain words related to 'love', which appears, to some extend, to be a theme in most of ABBA's songs.

#### Limitations
Using a method such as query search on word embeddings will not take instances of polysemy, i.e., when a word has more than one meaning, into account. This is because the code calculates static word embeddigs, which will not take the context of the other words present in that sentence into account, meaning that it won't be able to solve the ambiguity of polysemic words. This is of course not a problem with the chosen search terms presented above, but could become a problem if one were to use a polysemic word as a search term. 

It should be mentioned that this method is a very crude way of assessing the contents of popular music songs. The analysis show if words related to a certain search term appears in a text, which means that only one word related to that search term needs to appear in a song for it to be counted as containing a word related to the search term. It is therefore not possible to assess the extend to which the songs are about the search term. A more sophisticated way of examining themes of popular music songs could be to perform topic modelling on the dataset instead, for example by using the BERTopic model, which uses sentence transformers. By using this method, one could get a more thorough way of examining themes in popular music songs compared to an expanded query search. 


### A note on carbon emissions
The measured CO2-eq emissions for this project was ..
See [Assignment 5](https://github.com/louisebphansen/assignment-5-evaluating-environmental-impact-louisebphansen) for a further discussion of this. 
