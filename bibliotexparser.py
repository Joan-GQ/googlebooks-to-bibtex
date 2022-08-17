import os
from os.path import join, dirname
from io import StringIO
import requests
from pprint import pprint

entrytypes = {
    'article': {'author',
             'date-added',
             'date-modified',
             'doi',
             'journal',
             'number',
             'pages',
             'title',
             'url',
             'volume',
             'year'},
    'book': {'address',
          'author',
          'date-added',
          'date-modified',
          'doi',
          'publisher',
          'title',
          'url',
          'year'},
    'conference': {'address',
                'author',
                'booktitle',
                'date-added',
                'date-modified',
                'pages',
                'title',
                'year'},
    'inbook': {'address',
            'author',
            'booktitle',
            'date-added',
            'date-modified',
            'doi',
            'pages',
            'publisher',
            'title',
            'url',
            'year'},
    'incollection': {'address',
                  'author',
                  'booktitle',
                  'chapter',
                  'date-added',
                  'date-modified',
                  'doi',
                  'editor',
                  'pages',
                  'publisher',
                  'title',
                  'url',
                  'year'},
    'inproceedings': {'address',
                   'author',
                   'booktitle',
                   'date-added',
                   'date-modified',
                   'doi',
                   'editor',
                   'pages',
                   'publisher',
                   'title',
                   'url',
                   'year'},
    'mastersthesis': {'author',
                   'date-added',
                   'date-modified',
                   'school',
                   'title',
                   'url',
                   'year'},
    'misc': {'author',
          'date-added',
          'date-modified',
          'institution',
          'title',
          'year'},
    'phdthesis': {'title', 'year', 'address', 'date-modified', 'author', 'school'},
    'techreport': {'address',
                'author',
                'date-modified',
                'institution',
                'number',
                'title',
                'year'},
    'unpublished': {'author',
                 'date-added',
                 'date-modified',
                 'title',
                 'url',
                 'year'}
}

def google_books_query(key,title='', author='', isbn='', tqdm:bool=False):
    query = dict()
    
    if title != '' : query['intitle'] = title
    if author != '': query['inauthor'] = author
    if isbn != ''  : query['isbn'] = isbn

    print("Searching Google Books with this info:")
    print(f'Title = {title}')
    print(f'Author = {author}')
    print(f'ISBN = {isbn}')
    
    query = '+'.join(":".join(_) for _ in query.items())
    params = {'q': query, 'key': key}
    response = requests.get('https://www.googleapis.com/books/v1/volumes', params=params)
    response_dict = response.json()
    
    volumes = []
    if tqdm:
        from tqdm import tqdm
        for r in tqdm(response_dict['items']):
            volume = dict()
            volume['id'] = r['id']
            for key in r['volumeInfo'].keys():
                volume[key] = r['volumeInfo'][key]
            volumes.append(volume)
        return volumes

    else:
        for r in response_dict['items']:
            volume = dict()
            volume['id'] = r['id']
            for key in r['volumeInfo'].keys():
                volume[key] = r['volumeInfo'][key]
            volumes.append(volume)
        return volumes

def google2bibtex(volume:dict(), entrytype:str, entryname:str):
    if entrytype == 'book':
        output = dict()
        try:
            output = dict.fromkeys(entrytypes['book'])
            output['title'] = volume['title']
            output['year'] = volume['publishedDate'][:4]
            output['publisher'] = volume['publisher']
            output['author'] = ', '.join(volume['authors'])
            output['url'] = volume['canonicalVolumeLink']
        except Exception: pass;
        
        parsed_str = []
        for k,v in output.items():
            if v != None:
                key_str = str(k) + '=' + '{' + str(v) + '}'
                parsed_str.append(key_str)
        parsed_str = ',\n'.join(parsed_str)
        output_str = '@book{'+ f'{entryname},\n' + f'{parsed_str}' + '\n}'
        
        return output_str