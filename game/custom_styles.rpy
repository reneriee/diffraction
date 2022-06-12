## GENERAL ########################################

style text_shadow:
    drop_shadow  [(2, 2)] 
    drop_shadow_color "#0003"
    outlines [ (absolute(1), "#0003", absolute(0), absolute(0)) ]
    color "#0003"

transform drop_shadow_blur:
    blur 4.0
    alpha 0.5

# In game settings screens

style game_menu_title:
    xpos 189
    ypos 180

style game_menu_title_text:
    size gui.title_text_size
    color "#FFFFFF"

style box:
    background None

# -------------------------------------------

#### Preferences screen ####

# Options
style pref_label:
    xsize 380
    left_margin 21
    bottom_margin 3

style pref_label_text:
    color "#21242D"
    size 26
    font "Exo-Medium.ttf"

style radio_button:
    xsize 260
    top_margin 15

style radio_button_text:
    ypos 10
    xpos 20

style check_button:
    xsize 260
    top_margin 15

style check_button_text:
    ypos 10
    xpos 20

# Sliders
style pref_label_audio:
    xsize 380
    left_margin 21
    bottom_margin 45

style pref_label_audio_text:
    color "#21242D"
    size 24
    font "Exo-Medium.ttf"

style slider_vbox:
    xsize 675
    top_margin 20

style slider_slider:
    ypos 9
    xsize 910
    ysize 28

# min-max
style slider_value_min:
    color "#5A5A5A"
    size 24
    font "Exo-Regular.ttf"
    ypos 3
    xsize 50

style slider_value_max:
    color "#5A5A5A"
    size 24
    font "Exo-Regular.ttf" 
    ypos 3


#### Save/Load screens ####
