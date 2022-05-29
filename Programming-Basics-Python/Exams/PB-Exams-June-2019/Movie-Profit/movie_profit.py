movie_name = input()
days = int(input())
tickets_sum = int(input())
ticket_price = float(input())
percent_for_cinema = int(input())

profit_for_a_day = ticket_price * tickets_sum
profit_sum = profit_for_a_day * days
final_profit = profit_sum * (100 - percent_for_cinema) / 100

print(f"The profit from the movie {movie_name} is {final_profit:.2f} lv.")

