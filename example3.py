####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E3'
strategy_name = 'predicting a pattern'
strategy_description = '''we try to predict the pattern that our opponent has, and return values based on that pattern. if no pattern is detected, then we will figure out whether they betrayed or colluded more in their last 10 rounds and act upon that.'''
    
def move(my_history, their_history, my_score, their_score):
    '''We used their history as an input to figure out their last few moves and we used our history to see whether we betrayed or colluded in the last round so that we can continue the pattern. finally, based on which pattern our opponent followed our output was "c" or "b"'''
    counter = 0
    if len(my_history)==0: # It's the first round; collude.
      return 'c'
    elif 'bbb' in their_history[-4:]:
      return 'b' # Betray if they were severely punished last time,
    elif 'ccc' in their_history[-4:]:
      return 'b'
    elif 'bcbc' in their_history[-4:]:
      if my_history[-1]=='b':
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
