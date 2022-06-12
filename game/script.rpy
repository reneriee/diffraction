﻿# The script of the game goes in this file.

# Custom gui functions etc
init python:

# Blur the gui 
  def do_the_blurry(transform, st, at):    
    if (renpy.get_screen("preferences") 
    or renpy.get_screen("gallery")
    or renpy.get_screen("load")
    or renpy.get_screen("save")
    or renpy.get_screen("tracks")
    or renpy.get_screen("history")
    or renpy.get_screen("about")
    or renpy.get_screen("about")
    or renpy.get_screen("help")):
        transform.blur = 18.0
    else:
        transform.blur = 7.0
        transform.delay  = 4.0
        transform.blur = 0.0

    return 20.0

# Weather widget thing
  def weather_stuff(weather_now, month_now, day_now, dayofweek_now, temperature_now):
      store.weather = weather_now
      store.month = month_now
      store.day = day_now
      store.dayofweek = dayofweek_now
      store.temperature = temperature_now
 
# Assistant things and variables
transform blur_bg:
  function do_the_blurry

# The game starts here.
label start:
    $renpy.show_layer_at(blur_bg,layer= "master", camera = True)

## Start inputting date for widgets here (weather, date, etc)
    $weather_stuff("sunny", 12, 30, "Thursday", 15)
    show screen widgets

################################################################################

    scene bg mc room
    with fade
    "(Insert intro text here)"
    "(Mc leaves the room through her window after having checked social media, done her makeup and got dressed)"
    "(EXIT)"
    hide bg mc room
    show bg scenery
    mc "Out in the streets."
    mc "It's raining should have brought umbrella oh well, would have to have left through the door for that."
    mc "Thinking about this I wonder:"
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
    hide screen widgets

    ##### New day/time example
    $weather_stuff("rainy", 12, 31, "Friday", 20)
    show screen widgets

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
    h "Boo."
    h "I have an incredibly important and essential question for you."
    "To be continued"
    jump choice_done

    label choice_done:
    # This ends the game.

    return
