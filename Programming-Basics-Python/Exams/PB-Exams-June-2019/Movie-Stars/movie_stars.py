budget = float(input())
budget_left = budget
is_budget_not_enough = False

command_line = input()
while command_line != "ACTION":
    actor = command_line
    if len(actor) <= 15:
        actor_salary = float(input())
    else:
        actor_salary = budget_left * 0.2

    budget_left -= actor_salary
    if budget_left <= 0:
        is_budget_not_enough = True
        break
    command_line = input()

if is_budget_not_enough:
    print(f"We need {abs(budget_left):.2f} leva for our actors.")
else:
    print(f"We are left with {budget_left:.2f} leva.")