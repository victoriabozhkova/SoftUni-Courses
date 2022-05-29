import sys
max_points = -sys. maxsize
command = input()
movie_counter = 0
last_movie = ""
while command != "STOP":
    movie = command
    current_movie_points = 0
    movie_counter += 1
    if movie_counter >= 7:
        print(f"The limit is reached.")
        break
    for i in range(len(movie)):
        current_movie_points += ord(movie[i])
        if 65 <= ord(movie[i]) <= 90:
            current_movie_points -= len(movie)
        elif 97 <= ord(movie[i]) <= 122:
            current_movie_points -= 2 * len(movie)

        if current_movie_points > max_points:
            max_points = current_movie_points
            last_movie = movie


    command = input()

print(f"The best movie for you is {last_movie} with {max_points} ASCII sum.")








