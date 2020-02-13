####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E3'
strategy_name = 'probably collude'
strategy_description = '''Figure out whether the opponent colluded or betrayed more in their history of last 10 rounds. Then betray if they betrayed more and vice versa.'''
    
def move(my_history, their_history, my_score, their_score):
  '''take in their history and my history as inputs. for the first round, collude. Then for the most recent ten rounds, if our opponent colluded more than they betrayed, then collude, otherwise betray.'''
  count = 0
  if len(my_history)==0: # It's the first round; collude.
    return 'c'
  elif len(my_history) < 10:
    for letter in their_history:
      if letter == 'b':
        count += 1
      else:
        count += -1
    if count > 0:
      return 'b'
    else:
      return 'c'
  else:
    for counter in range(1, 11):
      if their_history[-counter] == 'b':
        count += 1
      else:
        count += -1
    if count > 0:
      return 'b'
    else:
      return 'c'