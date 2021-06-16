from genericpath import sameopenfile
import pandas as pd
import os
import json

KEYS_TO_USE = ['id', 'all_artists', 'title', 
               'medium', 'acquisitionYear', 
               'height', 'width', 'units']

def get_record_from_file(file_path, keys_to_use):
    """ Process single json file and return a tuple 
    containing specific fields """

    with open(file_path) as artwork_file:
        content = json.load(artwork_file)
    
    record = []
    for field in keys_to_use:
        record.append(content[field])
    
    return tuple(record)

# Single file processing demo
SAMPLE_JSON = os.path.join('pandas-fundamentals','demos', 'collection-master', 'artworks', 'a', '000', 'a00001-1035.json')

sample_record = get_record_from_file(SAMPLE_JSON, KEYS_TO_USE)

def read_artworks_from_json(keys_to_use):
    """Traverse the directories with JSON files.
    For the first file in each directory call function for processing 
    single file and go to the next directory"""

    JSON_ROOT = os.path.join('pandas-fundamentals','demos', 'collection-master', 'artworks')

    artworks = []

    for path, directories, files in os.walk(JSON_ROOT):
        for f in files:
            if f.endswith('json'):
                record = get_record_from_file(os.path.join(path, f), keys_to_use)
                artworks.append(record)
            break
    
    df = pd.DataFrame.from_records(artworks, columns=KEYS_TO_USE, index="id" )
    return df

df = read_artworks_from_json(KEYS_TO_USE)
print('')
