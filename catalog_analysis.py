import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019,
    "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98,
     "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112,
     "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101,
     "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89,
     "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124,
     "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137,
     "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118,
     "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95,
     "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129,
     "actors": ["P. Diaz", "T. Chalamet"]},
]
# Task №1
def average_rating(movies):
    astim = 0
    for movie in movies:
        astim += movie["rating"]
    astim = astim / len(movies)
    return round(astim, 2)

def catalog_age_stats(movies, current_year=2026) -> tuple[int, int, int]: 
    year_sort = sorted([movie["year"] for movie in movies])
    midle_m = current_year - math.ceil(sum(year_sort) / len(year_sort)) 
    print(midle_m)
    return (current_year - year_sort[0], current_year - year_sort[-1], midle_m)

def duration_in_hours(minutes):
    hour_min = [str(minutes // 60), 'ч ', str(minutes % 60), 'м']
    return "".join(hour_min) 

# Task №2
def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif 7 <= rating < 9:
        return "хорошо" 
    else:
        return "средне" if rating >= 5 else "слабо"

def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year < 2015:
            return "старые"
        case _:
            return "недавние"

# Task №3
def move_exept_genres(movies, genres="comedy"):
    movie_set = {genres}
    for movie in movies:
        if movie_set.issubset(movie["genres"]):
            continue
        print(movie['title'])

def search_amaizing(movies, rating=9.0):
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > rating:
            print(movies[i]["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")

def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:           
            count += 1      
    print(f"{count} ф. длиннее {threshold} минут")
    return count    #не знаю надо возвращать значение? сделал и так и так.

# Task №4
def normalize_title(title):
    title = title.split()
    return " ".join([word[0].upper() + word[1:].lower() for word in title])

def make_slug(title):
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    sort_genres = sorted(movie["genres"])
    return f"\"{
        normalize_title(movie["title"])}\" ({
            movie["year"]}) - {
                movie["rating"]}/10, {
                    duration_in_hours(movie["duration_min"])}, жанры: {
                        ", ".join(sort_genres)}"

def main():     

    print("Hello from homework-1!")


if __name__ == "__main__":
    main()




