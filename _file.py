"""The functions of this file are resposible
for getting the data in the file and pushing
the data contained in the working memory.

"""

import json

_FILES : dict = {
        'data' : 'data.json',
        'countries' : 'paises-gentilicos-google-maps.json',
    };

def _get(filename : str) -> dict:
    """This function opens the json file
    and returns its contents if it
    exists; else returns a empty dict.

    """

    try:
        with open(filename) as fil:
            data = json.load(fil);
    except FileNotFoundError:
        return dict();
    else:
        return data;

def _push(data : dict, filename : str) -> None:

    with open(filename, 'w') as fil:
        json.dump(data, fil);

def get_data() -> tuple:

    global _FILES;
    
    data : dict = _get(_FILES['data']);

    if data:
        return data['cup'], data['games'];

    groups : list = [
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
        ];

    cup : dict = {group : list() for group in groups};
    games : dict = {group : list() for group in groups};

    return cup, games;

def push_data(cup : dict, games : dict) -> None:

    global _FILES;

    _push({'cup' : cup, 'games' : games}, _FILES['data']);

def get_countries() -> list:

    global _FILES;

    data : dict = _get(_FILES['countries']);

    if data:
        return data;

    return [];

