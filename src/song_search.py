'''
LANGUAGE ANALYTICS @ AARHUS UNIVERSITY, ASSIGNMENT 3: Expanded query search with word embeddings

AUTHOR: Louise Brix Pilegaard Hansen

DESCRIPTION:
This script performs a word search on words related to (as defined by cosine similarities of word embeddings) a given search term on a given artist's songs.
The output of the search can be found as a txt file in the 'out' folder.
'''

# import modules
import gensim
import gensim.downloader as api
import os
import pandas as pd
import string
import re
import argparse 
import sys
from codecarbon import EmissionsTracker 
from codecarbon import track_emissions

# from my own search_utils script with defined helper functions, import
from search_utils import preprocess # function to preprocess texts
from search_utils import filter_and_clean # function filter dataframe on chosen artist and apply preprocessing
from search_utils import find_word_matches # function to find exact word matches from a list of similar words (based on word embeddings) to a chosen search term
from search_utils import calc_percentages # function to calculate how many percentage of songs contain words related to the search term
from search_utils import save_result # save results from expanded word query

# define emissionstracker to track CO2 emissions (for assignment 5)
tracker = EmissionsTracker(project_name="assignment3_subtasks",
                           experiment_id="song_search",
                           output_dir='emissions',
                           output_file="assignment3_subtasks.csv")


# define argument parser
def argument_parser():

    parser = argparse.ArgumentParser()

    parser.add_argument('--artist', type=str, help= 'Name of artist to search for in query', default='ABBA')
    parser.add_argument('--search_term', type=str, help= 'name of keyword to search for', default='love')

    args = vars(parser.parse_args())
    
    return args

def query_search(df, artist, model, search_term):

    '''
    Perform expanded query search on a given artist and search term.
    Results are saved in the 'out' folder.

    Arguments:
        - df: pandas df containing song lyrics data with 'artist' and 'text' columns
        - artist: chosen artist
        - model: gensim model to use for word embeddings
        - search_term: chosen search term to find similar words to and search for in songs
    
    Returns
        None
    '''

    # track preprocessing task
    tracker.start_task('Filter df and preprocess text')

    # create df with only the searched for artist
    artist_df = filter_and_clean(df, artist)

    # stop task tracking
    preprocessing_emissions = tracker.stop_task()

    # track query search
    tracker.start_task('Query search')

    # find percentage of songs containing words similar to or the search term
    result = calc_percentages(model, search_term, artist_df['cleaned_text'])

    # stop tracking
    search_emissions = tracker.stop_task()

    # save txt file with result
    save_result(result, artist, search_term)

    tracker.stop()

# create new tracker using a decorator to track emissions for running the entire script
@track_emissions(project_name="assignment3_full",
                experiment_id="assignment3_full",
                output_dir='emissions',
                output_file="emissions_assignment3_FULL.csv")
def main():

    # load args
    args = argument_parser()
    
    # track model and data loading
    tracker.start_task('Load GLOVE embedding model')

    # load glove model from gensim
    model = api.load("glove-wiki-gigaword-50")

    # stop tracking
    loading_emissions = tracker.stop_task()
    tracker.stop()

    # define path to Spotify data and load to pandas df
    in_path = os.path.join('in', 'Spotify Million Song Dataset_exported.csv')
    df = pd.read_csv(in_path)
    
    # perform expanded query search on the desired artist and search term
    query_search(df, args['artist'], model, args['search_term'])

if __name__ == '__main__':
   main()

