from random import randint

list = [1, 4, 6, 7, 3, 6, 8, 9, 2, 6, "A", "H", "W", "C", "K"]
winning_ticket = [list[randint(0, len(list) - 1)], list[randint(0, len(list) - 1)], list[randint(0, len(list) - 1)], list[randint(0, len(list) - 1)]]

my_ticket = []

loop_count = 0
i = 0

while len(my_ticket) != len(winning_ticket):
    num = list[randint(0, len(list) - 1)]
    if num == winning_ticket[i]:
        my_ticket.append(num)
        num = list[randint(0, len(list) - 1)]
        i += 1
    else:
        loop_count +=1

print(f"\nThe winning ticket is: {winning_ticket} ")
print(f"My ticket is: {my_ticket}")
print(f"Number of tries: {loop_count}")
