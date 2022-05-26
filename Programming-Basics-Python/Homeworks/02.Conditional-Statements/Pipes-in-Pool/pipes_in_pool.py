pool_litres = int(input())
first_pipe_for_hour = int(input())
second_pipe_for_hour = int(input())
hours = float(input())

first_pipe_sum_l = first_pipe_for_hour * hours
second_pipe_sum_l = second_pipe_for_hour * hours

pool_litres_full = first_pipe_sum_l + second_pipe_sum_l

first_pipe_percent = (first_pipe_sum_l / pool_litres_full) * 100
second_pipe_recent = (second_pipe_sum_l/ pool_litres_full) * 100
pool_full_percent = (pool_litres_full / pool_litres) * 100

if pool_litres_full > pool_litres:
    litres_more = pool_litres_full - pool_litres
    print(f"For {hours} hours the pool overflows with {litres_more:.2f} liters.")
else:
    print(f"The pool is {pool_full_percent:.2f}% full. Pipe 1: {first_pipe_percent:.2f}%." \
               f" Pipe 2: {second_pipe_recent:.2f}%.")
