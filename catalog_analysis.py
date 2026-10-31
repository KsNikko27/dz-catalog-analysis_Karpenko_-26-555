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
    midle_m = math.ceil(current_year - (sum(year_sort) / len(year_sort)))
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

# Task №5
def titles_by_sorted(movies):
    sorted_titles = sorted(movies, key=lambda movie: movie['rating'], reverse=True)
    return [top_title["title"] for top_title in sorted_titles]


def top_n_by_rating(movies, n=3):
    sorted_titles = sorted(movies, key=lambda movie: movie['rating'], reverse=True)
    return [(title_top['title'],title_top['rating']) for title_top in sorted_titles[:n]]

# Task №6
def count_by_genre(movies): 
    list_genres = {}
    
    for movie in movies:
        for genre in movie["genres"]:
           list_genres[genre] = list_genres.get(genre,0) + 1
    return {k: v for k, v in sorted(list_genres.items(),
                                    key=lambda item: item[1],
                                    reverse=True)} 

def actor_filmography(movies):
    list_actors_title = {}
    for movie in movies:
            for actor in movie["actors"]:
                if actor not in list_actors_title:
                    list_actors_title[actor] = []
                else:
                    list_actors_title[actor].append(movie["title"])
    return list_actors_title

def title_more_middle_rating(movies):
    return {movie["title"]: movie["rating"] 
            for movie in movies 
            if movie["rating"] > average_rating(movies)}

# Task №7
def all_genres(movies): # не совсем понял как без цикла сделать 
    set_genre = set()  #интересно узнать будьте так любезны показать.
    for movie in movies:
        set_genre = set_genre | movie["genres"]
    return set_genre

def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])

def genres_only_in_one(movies_a, movies_b):
    if isinstance(movies_a, dict):
        movies_a = [movies_a]
    if isinstance(movies_b, dict):
            movies_b = [movies_b]
    return set().union(
        *[movie_a["genres"] for movie_a in movies_a]
        ) - set().union(
            *[movie_b["genres"] for movie_b in movies_b]
            )

#Task 8
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie
def demonstrate_generator(generator):# Работа генератора
    for movie in generator:
        print(format_report_line(movie))

def generator_expression(movies):
    return sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)

def build_report(movies):
    print("ОТЧеТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет")
    print("\nТоп-3 фильма:")
    for top in sorted(movies, key=lambda movie: movie['rating'], reverse=True)[:3]:
        print(f"\t{format_report_line(top)}")
    print("\nФильмов по жанрам:") 
    dict_genre = count_by_genre(movies)
    for genre in dict_genre:
        print(f"\t{genre} - {dict_genre.get(genre, 0)}")
    print(f"Все жанры каталога: {" ".join(list(all_genres(movies)))}")

def main():     
    build_report(movies)


if __name__ == "__main__":
    main()




