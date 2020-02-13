####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E0'
strategy_name = 'Collude then betray if betrayed'
strategy_description = 'Collude but if they betray, betray twice and then continue to collude'
    
def move(my_history, their_history, my_score, their_score):
  '''if in most recent round either they betrayed or I betrayed, I will betray. We take in their history and my history as inputs and return a string with the letter 'b' or 'c' based on the most recent rounds.'''
  if their_history[-1] == 'b':
    return 'b'
  elif my_history[-2:] == 'bb':
    return 'c'
  elif my_history[-1] == 'b':
    return 'b'
  else:
    return 'c'