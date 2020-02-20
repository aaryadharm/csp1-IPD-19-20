####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E2'
strategy_name = 'basically random'
strategy_description = "uses the opponent's last 10 rounds to determine a probability to use for choosing our output"

import random

def move(my_history, their_history, my_score, their_score):
  '''we input the opponent's history and see how many times they betrayed and use that to determine the probability of us outputting a "b" of a "c"'''
  number = 0
  counterb = 0
  if len(their_history) < 10:
    if len(their_history) % 2 == 0:
      return 'c'
    else:
      return 'b'
  else:
    for number in range(10):
      if their_history[-number]=='b':
        counterb += 1
    number = random.choice(range(1,11))
    if number >= counterb:
      return 'c'
    else:
      return 'b'