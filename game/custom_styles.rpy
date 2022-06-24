
## GENERAL ########################################

style text_shadow:
    drop_shadow  [(2, 2)] 
    drop_shadow_color "#0004"
    outlines [ (absolute(1), "#0004", absolute(0), absolute(0)) ]
    color "#0004"

transform drop_shadow_blur:
    blur 3.5
    alpha 0.6

transform opacity_08:
    alpha 0.8

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
style slot_save_in_game_day_text:
    xpos 355
    ypos 65
    size 30
    color "#494949"
    font "Exo-Medium.ttf" 

style slot_save_date_time:
    xpos 357
    ypos 105
    size 17
    color "#494949"
    font "Exo-Regular.ttf" 

style slot_empty_save:
    yalign 0.5
    xalign 0.5
    color "#494949"
    font "Exo-Medium.ttf" 

style save_pagination:
    color "#1D2230"
    hover_color "#89BFDE"
    selected_color "#fff"

style save_page_label:
    color "#093a77"
    hover_color "#64dcf1"
    selected_color "#fff"
