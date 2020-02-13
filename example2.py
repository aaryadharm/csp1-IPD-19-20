####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E2'
strategy_name = 'Alternate twice but adapt'
strategy_description = 'try to identify a pattern and use te best strategy for that but if we cannot identify a strategy, then collude twice and betray twice back anf forth.'
    
def move(my_history, their_history, my_score, their_score):
  '''take in their history and my history as inputs and if we identify a pattern in the recent parts of their history, we will use the best strategy to combat it. if a pattern is unable to be distinguished, then betray twice and collude twice.'''
  if their_history[-4:] == 'cccc':
    return 'c'
  elif their_history[-4] == 'bbbb':
    return 'b'
  elif 'cbcb' == their_history[-4]:
    return 'b'
  elif my_history[-2:] == 'bb':
    return 'c'
  elif my_history[-1] == 'b':
    return 'b'
  elif my_history[-2:] == 'cc':
    return 'b'
  else:
    return 'c'