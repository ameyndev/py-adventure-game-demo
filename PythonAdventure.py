
# AMEY NALAWADE

import random
import textwrap
import sys
import time
import os

screenwidth=100

#FUNTION DEFINITIONs

def type_effect(got_text):
    for char in got_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char!="\n":
            time.sleep(0.04)
        else:
            time.sleep(0.05)

#TITLE SCREEN CHOICES
def TitleScreen_options():  
    menu_option=input("> ")
    if menu_option.lower()==("play"):
        player_setup()
    elif menu_option.lower()==("help"):
        screen_of_help()
    elif menu_option.lower()==("credits"):
        roll_credits()
    elif menu_option.lower()==("quit"):
        quit()
    while menu_option.lower() not in ['play','help','credits','quit']:
        print("Invalid input please try again!")
        menu_option=input("> ")
        if menu_option.lower()==("play"):
            player_setup()
        elif menu_option.lower()==("help"):
            screen_of_help()
        elif menu_option.lower()==("credits"):
            roll_credits()
        elif menu_option.lower()==("quit"):
            quit()


#MAIN SCREEN
def TitleScreen():
    print('-------------------------------------')
    print('|              ~PyTale~             |')
    print('|   ~A text based adventure game~   |')
    print('-------------------------------------')
    print('\n\n')
    print('               -:PLAY:-              ')
    print('               -:HELP:-              ')
    print('              -:CREDITS:-             ')
    print('               -:QUIT:-              ')
    TitleScreen_options()

#HELP PAGE
def screen_of_help():
    print('-------------------------------------')
    print("Instructions to play are as follows: ")
    print('1. You have to enter inputs/commands in form of text using your keyboard.')
    print('2. Player must input proper texts as given through the dialogues and instructions.')
    print('3 This is an RPG game, so choices will affect the game play loop.')
    print('-------------------------------------')
    TitleScreen_options()

#CREDITS
def roll_credits():
    print('-------------------------------------')
    print('PyTale is a game made for a Python class project.')
    print('Name still in progress')
    print('BY 7329 AMEY NALAWADE')
    print('Made as a beginner project as a beginner')
    print('ENJOY PLAYING!!!')
    print('-------------------------------------')
    TitleScreen_options()

#PLAYER STEUP<----------------------------------------PLAYER SETUP---------------------
def player_setup():
    print('-------------------------------------')
    pre_prologue="A strong presence gets startled by your unconcious presence on the vast open grounds. \n'What are you doing here? This is no place for a mere mortal', it said in its heavy arrogant tone. \n'How dare you show your weak presence in front of the mighty see! You have no reason to be here.'\nThe giant presence lifts your unconscious body and hurls it into the skyward direction."
    type_effect(pre_prologue)
    print('\n-------------------------------------')
    print('\n\n               -:ACT 1:-              ')
    act1_1="\nYou wake up under a tree.\nYou start to gain conscious and try to look around.\n!!!!!\nYou see a large burnt out pit around you.\nMaybe it was from the impact of your body.\nYou stand up a see two roads.\n1. To the open grass fields.\n2. To a riverbed. \nWhere would you want to go?\n(Fields) OR (Riverbed)?"
    type_effect(act1_1)
    act1_1_choice=input("\n> ")
    if act1_1_choice.lower()==("fields"):
        act1_fields()
    elif act1_1_choice.lower()==("riverbed"):
        act1_riverbed()
    while act1_1_choice.lower() not in ["fields","riverbed"]:
        print("Please insert proper text choice")
        act1_1_choice=input("\n> ")
        if act1_1_choice.lower()==("fields"):
            act1_fields()
        elif act1_1_choice.lower()==("riverbed"):
            act1_riverbed()

def act1_fields():
    act1_fields_1="\nYou find yourself standing in between a rice field.\n!!!!!\n You hear a girl yell at you from behind. \n'HEEYY! What the hell are you doing in my fields?! Don't you think of stealing any of my yields or I'll feed you to the goats'. \nYou try to explain your situation to her, but she gets taken aback by seeing your situation. \n'You look beat up! Who exactly are you? How did you get here? Anyways come inside with me, I'll tend to your wounds'\nThe girl takes you inside a big horse stable.\nThe girl says, 'By the way, my name is Xialan. What's your name?'"
    type_effect(act1_fields_1)
    player1=input("\n> ")
    act1_fields_2="\nXialan:Oh! You don't seem to be from around here. Where did you come from? \nYou: Earth \nXialan: Ea- Earth? Never heard of it. Anyways, where did you go to get hurt like this? \nYou: I don't remember \nXialan: This is weird. Oh, I am really busy for now. Make yourself comfortable here and don't go out \nXialan runs out of the stable in a hurry. Leaving you to rest in the stable. \nBut you think of wandering around the stable to find out more information. \nYou come across TWO compartments \n(1)The one with a bulletin board \n(2)The one with the tools \nWhat will you choose? (Bulletin board) OR (Tools)"
    type_effect(act1_fields_2)
    act1_fields_choice_1=input("\n> ")
    if act1_fields_choice_1.lower()==("bulletin board") or act1_fields_choice_1.lower()==("bulletin") or act1_fields_choice_1.lower()==("board"):
        act1_fields_board()
    elif act1_fields_choice_1.lower()==("tools"):
        act1_fields_tools()
    while act1_fields_choice_1.lower() not in ["bulletin board","bulletin","board","tools"]:
        print("Please insert proper text choice")
        act1_fields_choice_1=input("\n> ")
        if act1_fields_choice_1.lower()==("bulletin board") or act1_fields_choice_1.lower()==("bulletin") or act1_fields_choice_1.lower()==("board"):
            act1_fields_board()
        elif act1_fields_choice_1.lower()==("tools"):
            act1_fields_tools()

def act1_fields_board():
    act1_fields_board_1="\nYou observe all the information on the bulletin board. \nThe location and the world you see isn't like Earth at all. \n Weird creatures and abilities are used by the people here. \nYou see a newspaper lying next to the board. You pick it up and read it. \nA massive earthquake was observed in the region. \nIt may be because of Kai, the Emperor. That eerily feels familiar.\nYou go out of the stable and bump into the stable as she is walking in.\nXialan: OW! Oh hey, I was just going to all you. Dinners ready. I'll bring it in for you. \nYou: Okay. \nYou have the dinner offered by Xialan. \nXialan: Okay, now get some rest, there is a spare mattress and sheets you can use. Goodnight! \nYou go to sleep."
    type_effect(act1_fields_board_1)
    final_puzzle_to_end()

def act1_fields_tools():
    act1_fields_tools_1="\nYou look around where the tools are kept. \nAll the tools are neatly arranged. \nYou decide not to touch anything. \nYou move on to the bulletin board."
    type_effect(act1_fields_tools_1)
    act1_fields_board()

def act1_riverbed():
    act1_riverbed_1="\nYou reach the riverbed. You look at your own reflection in the water.\nYou look pretty beaten up by the impact or whatever you went through before it. \nA but a soothing tune warms you up. \nThen a friendly voice speaks up, 'You okay there, traveler? You don't look so good.'\n'My name's Anos. And you are?'"
    type_effect(act1_riverbed_1)
    player1=input("\n> ")
    act1_riverbed_2="\nAnos: Well that explains your attire and your confused look. You are not from this world, are you? \nCome to my place. I'll take care of your medical treatments and your basic needs. Let's go. \nAnos points to a carriage and leads you to it. \nLooks like he is rich, but surprisingly humble. \nAnos: It's nothing much, "+player1+". But it can take you to my mansion. \nYou: No, it's okay. \nYou reach Anos' mansion. It's big but gives off a welcoming aura. \nAnos requests for assistance for your treatment and a butler and a nurse comes for your aid. \nYou are put up in an empty bedroom. \nAnos: Let me or anyone from the house know if you need anything. Okay? \nYou: Okay \nAnos: Don't mess around. Rest. \nYou are left alone in the room. \nYou look around the room. You see \n(1) a table with a newspaper on it and \n(2) a window with a view. \nWhere would you want to go? \n(Table) OR (Window)"
    type_effect(act1_riverbed_2)
    act1_riverbed_choice=input("\n> ")
    if act1_riverbed_choice.lower()==("table"):
        act1_riverbed_table()
    elif act1_riverbed_choice.lower()==("window"):
        act1_riverbed_window()
    while act1_riverbed_choice.lower() not in ["table","window"]:
        print("\nPlease input proper text choice")
        act1_riverbed_choice=input("\n> ")
        if act1_riverbed_choice.lower()==("table"):
            act1_riverbed_table()
        elif act1_riverbed_choice.lower==("window"):
            act1_riverbed_window()

def act1_riverbed_table():
    act1_riverbed_table_1="\nYou look at the newspaper. \nYou pick it up and read it. \nA massive earthquake was observed in the region. \nIt may be because of Kai, the Emperor. That eerily feels familiar. \nYou put the newspaper back and turn around but..."
    type_effect(act1_riverbed_table_1)
    final_puzzle_to_end()

def act1_riverbed_window():
    act1_riverbed_window_1="\nYou approach the window and look out of it. \nThe view is pleasant and it somehow fills you with determination.\nYou stare into the distance and notice that this world is very different from Earth. \nYou decide to get back into bed. But..."
    type_effect(act1_riverbed_window_1)
    final_puzzle_to_end()

def final_puzzle_to_end():
    print('\n-------------------------------------')
    print('\n           -:Prol0gu3 #nd:-           ')
    print('\n             -:4CT 1.?:-              ')
    final_puzzle_to_end_1="\nYou wake up to a blinding white light. \nYou try to adjust to it but you only see white light all over the place. But suddenly a voice speaks in a calm tone... \nVoice: Hello little one. The path ahead is dangerous. \nYou: Who is there? Where are you speaking from? \nVoice: I am exactly what you are thinking of. I am merely a voice. \nYou: What do you want from me? \nVoice: I am here just to help you. \nYou: By whom? \nVoice: By the one who sees it all. The wielder of the powers of the FOUNDER. \nYou: The FOUNDER? Who is that? I don't know anyone by that name. \nVoice: The time is not yet. You shall know about everything as you make your way. \nYou: Make my way? Through what? \nVoice: Everything will be explained. Even about your silence when you met the kind souls who helped you a few minutes ago. \nYou: Huh? \nVoice: This here is an infinite room which has been created for your training for your future. You shall train yourself here. \nYou: Why should I train myself? Wha- \nVoice: No further questions please. You are provided with a puzzle and you must solve it now."
    type_effect(final_puzzle_to_end_1)
    print('\n-------------------------------------')
    print("\nGUESS ALL THE LETTERS FOR The WORD")
    final_puzzle_to_end_puzzle()

def final_puzzle_to_end_puzzle():
    print('\n-------------------------------------')
    puzzle_clue="\nTo get help to solve this puzzle here is a clue. \nThe word is one of the strongest characteristics in all humans. \nOnce you have it in you, you can do anything and go through anything. \nIt is very important. \nIt starts with D and ends with the words '-tion'. \nGood luck, hunter."
    type_effect(puzzle_clue)
    terms=['determination']
    word=random.choice(terms)
    guesses=''
    turns=10
    while turns>0:
        failed=0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("\n_")
                failed+=1
            
        if failed==0:
            you_right="\nYou guessed the right word. \nThe word is DETERMINATION"
            type_effect(you_right)
            end_roll_credits()
            break
        print("Enter a character for the word")
        guess=input("\n> ")
        guesses+=guess
        if guess not in word:
            turns-=1
            print("\nWrong try again")
            print("\nYou have ",+turns," guesses left")

        if turns==0:
            print("\nYou failed the test. Try again")
            final_puzzle_to_end_puzzle()

def end_roll_credits():
    print('\n\n             -:END SCREEN:-              ')
    print('\n-------------------------------------')
    end_credits="\nThank you for playing this game. \nPyTale(Name still in progress) is a game made for a Python class project. \nBY 7329 AMEY NALAWADE. \nHope this was atleast enjoyable. \nMade as a beginner project as a beginner. \nTHANK YOU <3"
    type_effect(end_credits)
    print('\n-------------------------------------')

#GAME SET-----------------------------------------GAME SET
TitleScreen()
# final_puzzle_to_end_puzzle()