#Script to prepare hierarchical data
import requests
import csv
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API Key from environment variable
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.themoviedb.org/3'

if not API_KEY:
    raise ValueError('API_KEY not found in .env file')

def get_popular_movies(pages=5):
    """Gets popular movies from TMDB"""
    all_movies = []
    
    for page in range(1, pages + 1):
        url = f'{BASE_URL}/movie/popular'
        params = {
            'api_key': API_KEY,
            'language': 'en-US',
            'page': page
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            all_movies.extend(data['results'])
            print(f'Page {page} downloaded - {len(data["results"])} movies')
            time.sleep(0.25)  # Pause to avoid API rate limits
        except Exception as e:
            print(f'Error on page {page}: {e}')
    
    return all_movies

def get_top_rated_movies(pages=5):
    """Gets top rated movies from TMDB"""
    all_movies = []
    
    for page in range(1, pages + 1):
        url = f'{BASE_URL}/movie/top_rated'
        params = {
            'api_key': API_KEY,
            'language': 'en-US',
            'page': page
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            all_movies.extend(data['results'])
            print(f'Page {page} downloaded - {len(data["results"])} movies')
            time.sleep(0.25)
        except Exception as e:
            print(f'Error on page {page}: {e}')
    
    return all_movies

def save_to_csv(movies, filename='movies_tmdb.csv'):
    """Saves data to a CSV file"""
    if not movies:
        print('No data to save')
        return
    
    fields = [
        'id',
        'title',
        'original_title',
        'overview',
        'release_date',
        'popularity',
        'vote_average',
        'vote_count',
        'original_language',
        'adult',
        'poster_path',
        'backdrop_path',
        'genre_ids'
    ]
    
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        
        for movie in movies:
            row = {
                'id': movie.get('id', ''),
                'title': movie.get('title', ''),
                'original_title': movie.get('original_title', ''),
                'overview': movie.get('overview', ''),
                'release_date': movie.get('release_date', ''),
                'popularity': movie.get('popularity', ''),
                'vote_average': movie.get('vote_average', ''),
                'vote_count': movie.get('vote_count', ''),
                'original_language': movie.get('original_language', ''),
                'adult': movie.get('adult', ''),
                'poster_path': movie.get('poster_path', ''),
                'backdrop_path': movie.get('backdrop_path', ''),
                'genre_ids': ','.join(map(str, movie.get('genre_ids', [])))
            }
            writer.writerow(row)
    
    print(f'\n✓ File saved: {filename}')
    print(f'Total movies: {len(movies)}')

def main():
    print('=== TMDB Data Extractor ===\n')
    
    # Option 1: Popular movies
    print('Getting popular movies...')
    popular_movies = get_popular_movies(pages=10)
    save_to_csv(popular_movies, 'popular_movies.csv')
    
    # Option 2: Top rated movies
    print('\nGetting top rated movies...')
    top_rated_movies = get_top_rated_movies(pages=10)
    save_to_csv(top_rated_movies, 'top_rated_movies.csv')

if __name__ == '__main__':
    main()