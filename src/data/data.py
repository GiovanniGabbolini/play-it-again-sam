'''
Created on Fri Jan 17 2020

@author Giovanni Gabbolini
'''


import pandas as pd
import os
import numpy as np
preprocessed_dataset_path = 'res/p'
raw_dataset_path = 'res/r'
feature_path = f"{preprocessed_dataset_path}/features"
path_file_name_normalized_idf = preprocessed_dataset_path

_idf_correction = {}
_genres_graph = None


def playlist():
    df = pd.read_csv(os.path.join(preprocessed_dataset_path,
                                  'playlist.csv'))
    return df


def genres_graph():
    path = os.path.join(preprocessed_dataset_path, 'genres_graph.npy')
    if not os.path.exists(path):
        g = build_graph()
        np.save(path, g)
    global _genres_graph
    if _genres_graph == None:
        _genres_graph = np.load(os.path.join(preprocessed_dataset_path,
                                             'genres_graph.npy'), allow_pickle='TRUE').item()
    return _genres_graph


def the_chain():
    df = pd.read_csv(os.path.join(raw_dataset_path,
                                  'the_chain.csv'))
    return df


def track_album_artists_id(index=''):
    df = pd.read_csv(os.path.join(preprocessed_dataset_path,
                                  'track_album_artists_id.csv'))
    if index != '':
        df = df.set_index(index)
    return df
