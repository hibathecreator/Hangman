
import random
from words import math, science, geography, history, literature, art
from hangmen import display_hangman_1, display_hangman_2
from replit import audio

def help():
  print(""" Please enter one of the numbers shown in the menu in order to run the appropriate function. \n
  Two player game: \n
  If you choose to play with a human player then the player will get the chance to enter a word and decide the difficulty of the game. Then you will get have 6 guesses to get the word right. \n
  Playing with the computer: \n
  If you choose to play with a computer then you will be able to select the category from which you want the word along with the difficulty level you want to play at. Then the computer will randomly select a word and you will have 6 chances to get the word right.\n
  In both types of games, if you choose the easy difficulty then you will have 7 chances to guess the word and if you choose the hard difficulty, you will get 6 changes. You will also get hints to help you along the way though the number of hints will vary depending on the difficulty level. After the game is completed, you will automatically be returned to the main menu. """)
  display_menu()
  return

def duplicates(input_list, repeated_letter):
  return [i for i, letter in enumerate(input_list) if letter == repeated_letter]

def play_game(term, difficulty):
  global board
  board = []
  for letter in term:
    if letter == ' ':
      board.append(' ')
    else:
      board.append('-')
  
  guesses = []
  num_reveals = 0
  num_wrong = 0
  no_reveals = False

  if difficulty == '1':
    max_num_wrong = 7
    display_hangman_2(num_wrong)
  elif difficulty == '2':
    max_num_wrong = 6
    display_hangman_1(num_wrong)

  display_board()
  
  while num_wrong < max_num_wrong:
    if '-' not in board:
      print('Sorry you lose.')
      display_menu()
    p1_input = (input('Guess a letter ')).lower()
    while p1_input.isalpha() == False or len(p1_input) > 1:
      print('Enter one lowercase alphabetical letter.')  
      display_board()
      p1_input = (input('Guess a letter ')).lower()
      
    else:
      
      letters = []
      for i in term:
        letters.append(i)
      
      if p1_input in term:
        audio.play_file("correct_answer.wav")

        if p1_input not in guesses:
          guesses.append(p1_input)
        no_reveals = True
        if term.count(p1_input) > 1:
          repeated_indices = duplicates(letters, p1_input)
          for index in repeated_indices:
            board[index] = p1_input
        
        else:
          go_to = term.index(p1_input)
          board[go_to] = p1_input
      else:
        num_wrong += 1
        audio.play_file("wrong_answer.wav")
        no_reveals = False
    
      if difficulty == '1':
        display_hangman_2(num_wrong)
      elif difficulty == '2':
        display_hangman_1(num_wrong)

      display_board()
      if '-' not in board:
        print('\n You got it!')
        display_menu()
      else:
        if num_wrong == max_num_wrong or '-' not in board:
          
          print('\n The term was: ' + term)    
          print('\n Sorry you lose.')
          
          display_menu()
        
        if difficulty == '1' and num_wrong == 5:
          if len(term) < 5:
            num_reveals = 1
          elif len(term) > 5 and len(term) < 10:
            num_reveals = 2
          elif len(term) > 10:
            num_reveals = 2
        if difficulty == '2' and num_wrong == 4:
            if len(term) < 5:
              num_reveals = 0
            elif len(term) >= 5 and len(term) < 10:
              num_reveals = 1
            elif len(term) >= 10:
              num_reveals = 2
        
        if num_reveals != 0 and no_reveals != True:
          reveal = random.randint(0, len(term) - 1)
          while board[reveal] != '-':
            reveal = random.randint(0, len(term) - 1)
       
          if term.count(term[reveal]) > 1:
            repeated_indices = duplicates(letters, term[reveal])
            for index in repeated_indices:
              board[index] = term[reveal]
          else:
            board[reveal] = term[reveal]
          
          display_board()
          print("< Here's a hint")
          num_reveals -= 1
  return

def display_board():
  for i in board:
    print(i, end = " ")
  return

def two_players():
  term = (input('Player 1 please enter 1-3 terms. These will be the term(s) player 2 will guess:  \n ')).lower()  
  
  difficulty = input("""What level of difficult do you want the game to be Player 1? 
  1- easy
  2- difficult
  """)
  while difficulty != '1' and difficulty != '2':
    print('Please enter 1 if you want to play an easy game and 2 if you want to play a difficult game.')
    difficulty = input("""What level of difficult do you want the game to be Player 1? 
    1- easy
    2- difficult
    """)
  play_game(term,difficulty)
  return


def play_with_comp():
  category_num = input("""Which category would you like a word from:
  1 - math
  2 - science
  3 - geography
  4 - history
  5 - literature
  6 - art
   Enter the number corresponding to the approproite category:  """)
  global term
  if category_num == '1':
    num = random.randint(0,len(math)-1)
    term = math[num]
  elif category_num == '2':
    num = random.randint(0,len(science)-1)
    term = science[num]
  elif category_num == '3':
    num = random.randint(0,len(geography)-1)
    term = geography[num]
  elif category_num == '4':
    num = random.randint(0,len(history)-1)
    term = history[num]
  elif category_num == '5':
    num = random.randint(0,len(literature)-1)
    term = literature[num]
  elif category_num == '6':
    num = random.randint(0,len(art)-1)
    term = art[num]
  else:
    play_with_comp()
  
  difficulty = input("""What level of difficult do you want to play at?
  1- easy
  2- difficult
  """)
  while difficulty != '1' and difficulty != '2':
    print('Please enter 1 if you want to play an easy game and 2 if you want to play a difficult game.')
    difficulty = input("""What level of difficult do you want the game to be Player 1? 
    1- easy
    2- difficult
    """)
  play_game(term,difficulty)
  
  return

def exit():
  print('Thank you for playing!')
  user_input = input('Enter 1 to reenter the game: ')
  if user_input == '1':
    display_menu()
  else:
    exit()
  return

def display_menu():
  print("""
  Welcome to HANGMAN
  1- Help
  2- Play two player game
  3- Play with computer
  4- Exit
  """)
  
  user_input = input('Enter the appropriate number in order to run one of the functions above.')
  if user_input == '1':
    help()
  elif user_input == '2':
    two_players()
  elif user_input == '3':
    play_with_comp()
  elif user_input == '4':
    exit()
  else:
    display_menu()
display_menu() 
