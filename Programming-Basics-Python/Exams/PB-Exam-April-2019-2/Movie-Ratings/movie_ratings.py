number_of_movies = int(input())
import sys
max_rating = -sys.maxsize
lowest_rating = sys.maxsize
rating_sum = 0
ratings_counter = 0
lowest_movie = ""
highest_movie = ""

for i in range(1, number_of_movies +1):
    movie_name = input()
    movie_rating = float(input())
    rating_sum += movie_rating
    ratings_counter +=1

    if movie_rating > max_rating:
        max_rating = movie_rating
        highest_movie = movie_name
    if movie_rating < lowest_rating:
        lowest_rating = movie_rating
        lowest_movie = movie_name

avg_rating = rating_sum / ratings_counter

print(f"{highest_movie} is with highest rating: {max_rating:.1f}")
print(f"{lowest_movie} is with lowest rating: {lowest_rating:.1f}")

print(f"Average rating: {avg_rating:.1f}")





