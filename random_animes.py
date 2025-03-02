import requests
import random

def get_random_anime(genre=None , anime_type=None):

    url = "https://api.jikan.moe/v4/anime"

    params = {}
    
    if genre:
        params['genres'] = genre  # Use correct parameter name
    
    if anime_type:
        params['type'] = anime_type.lower()  # Ensure lowercase (Jikan expects lowercase)

    params['limit'] = 10  # Reduce the limit to avoid slow requests
    params['order_by'] = 'popularity'
    params['sort'] = 'desc'

    #send get requests
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json() #convert into json
        anime_list = data.get('data', [])

        if anime_list:
        #pick a random anime
            anime = random.choice(anime_list)

            return {
                'Title': anime.get('title', 'N/A'),
                'Synopsis': anime.get('synopsis', 'No synopsis available'),
                'Episodes': anime.get('episodes', 'Unknown'),
                'Score': anime.get('score', 'Not rated'),
                'Type': anime.get('type', 'Unknown'),
                "URL": anime.get('url', 'No URL available')
            }
        else:
                return "No anime found for this category."
    else:
         return f"Error fetching data from Jikan API. Status Code: {response.status_code}"

#mapping mood to genre
mood_to_genre = {
    'action': 1, #genre ID
    'adventure': 2,
    'drama': 8,
    'fantasy': 10,
    'horror': 14,
    'slice of life': 36,
    'sports': 30,
    'romance': 22
}

print("What mood are you in? (e.g. action, horror, sports, etc.)")
user_mood = input().strip().lower()

#get genre ID
genre_id = mood_to_genre.get(user_mood)

#ask for type
print("Do you prefer TV Series, Movie, or OVA?")
anime_type = input().strip().capitalize()

#recomend an anime
recommended_anime = get_random_anime(genre=genre_id, anime_type=anime_type)

#display the recommended anime
if isinstance(recommended_anime, dict):
     print("\n🎥 **Anime Recommendation:**")
     for key, value in recommended_anime.items():
          print(f"{key}:{value}")

else:
    print(recommended_anime)
