####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E0'
strategy_name = 'Your fault'
strategy_description = 'if opponent colludes more, then we will collude or vice versa.'
    
def move(my_history, their_history, my_score, their_score):
  '''used the input of their history to count how many times they colluded and betrayed in the last ten rounds and we output whatever they had more of.'''
  counter = 0
  if len(their_history) < 10:
    if len(their_history) % 2 == 0:
      return 'c'
    else:
      return 'b'
  else:
    for number in range(10):
      if their_history[-number]=='b':
        counter += 1
      else:
        counter += -1
    if counter > 0:
      return 'b'
    else:
      return 'c'
    