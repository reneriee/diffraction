# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("April")
define f = Character("Faine")
define h = Character("Hendric")
define na = Character("???")
# The game starts here.
label start:
    scene bg mc room
    with fade
    "(Insert intro text here)"
    "(Mc leaves the room through her window after having checked social media, done her makeup and got dressed)"
    "(EXIT)"
    hide bg mc room
    show bg scenery
    "Out in the streets."
    "It's raining should have brought umbrella oh well, would have to have left through the door for that."
    "Thinking about this I wonder:"
    menu:
        "(Where should I go?)"
        "To the park":
            "I still remembered the way there well."
            "It would be a short walk."
            jump choice_thatplace
        "Go to the convenience store for breakfast":
            "I need to eat something..."
            jump choice_store

    label choice_thatplace:
    hide bg scenery
    show bg thatplace
    with fade
    "(MC thoughts blablabla, this is the place I met faine that day.)"
    "(Totally forgot wow so emotional, this is a good photo op)"
    show faine
    "You spot someone who resembles your old friend...but is it really him?"
    "To be continued..."
    jump choice_done

    label choice_store:
    hide bg scenery
    show bg store
    "(MC looking around store)"
    show h-p2
    show h-e1
    show h-m1
    na "Boo."
    na "I have an incredibly important and essential question for you."
    "To be continued"
    jump choice_done

    label choice_done:
    # This ends the game.

    return
