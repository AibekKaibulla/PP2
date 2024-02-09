movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def is_high_imdb(movie):
    return movie["imdb"] > 5.5

def high_imdb_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

def movies_by_category(movies, category):
    my_list = []
    for i in movies:
        if i["category"] == category:
            my_list.append(i["name"])
    return my_list

def average_imdb(movies):
    imdb_scores = [movie["imdb"] for movie in movies]
    return sum(imdb_scores) / len(imdb_scores)

def average_imdb_by_category(movies, category):
    category_movies = [movie for movie in movies if movie["category"] == category]
    return average_imdb(category_movies)
print(is_high_imdb(movies[0]))
print(high_imdb_movies(movies))
print(movies_by_category(movies, "Romance"))
print(average_imdb(movies))
print(average_imdb_by_category(movies, "Romance"))