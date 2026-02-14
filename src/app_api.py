import requests

def get_movie_info_by_name(movie_name):
    url = "https://moviesapi.ir/api/v1/movies"
    params = {"q": movie_name}

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return "❌ API Error"

    response = response.json()
    data_list = response.get("data", [])

    if not data_list:
        return "❌ Movie not found"

    data = data_list[0]

    title = data.get("title", "N/A")
    year = data.get("year", "N/A")
    country = data.get("country", "N/A")
    imdb_rate = data.get("imdb_rating", "N/A")
    genres = ", ".join(data.get("genres", []))

    return f"""
🎬 *Title:* {title}
📅 *Year:* {year}
🌍 *Country:* {country}
⭐ *IMDb:* {imdb_rate}
🎭 *Genres:* {genres}
"""