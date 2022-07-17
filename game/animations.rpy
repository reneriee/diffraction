init -2:
# Animated main screen
    image main_menu_animated:
        pause 0.35
        animation
        "gui/main_menu.png"
        ypos -50
        alpha 0.0
        easeout 2.7 ypos 0 alpha 0.95 
        easeout 1.0 alpha 1.0 

    image logo_animated:
        pause 1.5
        animation
        "gui/logo.png"
        alpha 0.0
        xsize 647
        ysize 259
        easeout 2.0 alpha 1.0 

    image arrow_thing_animated:
        animation
        "gui/button/main_chevron_right.png"
        alpha 0.0
        easeout 2.0 alpha 1.0 

# animations for quick menu buttons

    image quickmain_button:
        "gui/button/quickmain_idle.png"
        on idle:
            "gui/button/quickmain_idle.png" with Dissolve(0.15, alpha=True)
        on hover:
            "gui/button/quickmain_idle.png"
            "gui/button/quickmain_hover.png" with Dissolve(0.15, alpha=True)
        on selected_idle:
            "gui/button/quickmain_hover.png" with Dissolve(0.15, alpha=True)
        on selected_hover:
            "gui/button/quickmain_hover.png" with Dissolve(0.15, alpha=True)

    image quickprefs_button:
        "gui/button/quickprefs_idle.png"
        on idle:
            "gui/button/quickprefs_idle.png" with Dissolve(0.15, alpha=True)
        on hover:
            "gui/button/quickprefs_idle.png"
            "gui/button/quickprefs_hover.png" with Dissolve(0.15, alpha=True)
        on selected_idle:
            "gui/button/quickprefs_hover.png" with Dissolve(0.15, alpha=True)
        on selected_hover:
            "gui/button/quickprefs_hover.png" with Dissolve(0.15, alpha=True)

    image quickhistory_button:
        "gui/button/quickhistory_idle.png"
        on idle:
            "gui/button/quickhistory_idle.png" with Dissolve(0.15, alpha=True)
        on hover:
            "gui/button/quickhistory_idle.png"
            "gui/button/quickhistory_hover.png" with Dissolve(0.15, alpha=True)
        on selected_idle:
            "gui/button/quickhistory_hover.png" with Dissolve(0.15, alpha=True)
        on selected_hover:
            "gui/button/quickhistory_hover.png" with Dissolve(0.15, alpha=True)
            
    image quickauto_button:
        "gui/button/quickplay_idle.png"
        on idle:
            "gui/button/quickplay_idle.png" with Dissolve(0.15, alpha=True)
        on hover:
            "gui/button/quickplay_idle.png"
            "gui/button/quickplay_hover.png" with Dissolve(0.15, alpha=True)
        on selected_idle:
            "gui/button/quickauto_hover.png" with Dissolve(0.15, alpha=True)
        on selected_hover:
            "gui/button/quickauto_hover.png" with Dissolve(0.15, alpha=True)

    image quickskip_button:
        "gui/button/quickskip_idle.png"
        on idle:
            "gui/button/quickskip_idle.png" with Dissolve(0.15, alpha=True)
        on hover:
            "gui/button/quickskip_idle.png" 
            "gui/button/quickskip_hover.png" with Dissolve(0.15, alpha=True)
        on selected_idle:
            "gui/button/quickskip_hover.png" with Dissolve(0.15, alpha=True)
        on selected_hover:
            "gui/button/quickskip_hover.png" with Dissolve(0.15, alpha=True)

    image quicksave_button:
        "gui/button/save_button_idle.png"
        on idle:
            "gui/button/save_button_idle.png" with Dissolve(0.15, alpha=True)
        on hover:
            "gui/button/save_button_idle.png" 
            "gui/button/save_button_hover.png" with Dissolve(0.15, alpha=True)
        on selected_idle:
            "gui/button/save_button_hover.png" with Dissolve(0.15, alpha=True)
        on selected_hover:
            "gui/button/save_button_hover.png" with Dissolve(0.15, alpha=True)

    image quickload_button:
        "gui/button/load_button_idle.png"
        on idle:
            "gui/button/load_button_idle.png" with Dissolve(0.15, alpha=True)
        on hover:
            "gui/button/load_button_idle.png" 
            "gui/button/load_button_hover.png" with Dissolve(0.15, alpha=True)
        on selected_idle:
            "gui/button/load_button_hover.png" with Dissolve(0.15, alpha=True)
        on selected_hover:
            "gui/button/load_button_hover.png" with Dissolve(0.15, alpha=True)

# mini buttons (top right corner)
    image mini_main_button:
        "gui/button/mini_main_idle.png"
        on idle:
            "gui/button/mini_main_idle.png" with Dissolve(0.15, alpha=True)
        on hover:
            "gui/button/mini_main_idle.png"
            "gui/button/mini_main_hover.png" with Dissolve(0.15, alpha=True)
            
    image mini_twitter_button:
        "gui/button/mini_twitter_idle.png"
        on idle:
            "gui/button/mini_twitter_idle.png" with Dissolve(0.15, alpha=True)
        on hover:
            "gui/button/mini_twitter_idle.png"
            "gui/button/mini_twitter_hover.png" with Dissolve(0.15, alpha=True)

    # image mini_ql_button:
    #     "gui/button/mini_ql_idle.png"
    #     on idle:
    #         "gui/button/mini_ql_idle.png" with Dissolve(0.15, alpha=True)
    #     on hover:
    #         "gui/button/mini_ql_idle.png"
    #         "gui/button/mini_ql_hover.png" with Dissolve(0.15, alpha=True)
        
    image mini_qs_button:
        "gui/button/mini_qs_idle.png"
        on idle:
            "gui/button/mini_qs_idle.png" with Dissolve(0.15, alpha=True)
        on hover:
            "gui/button/mini_qs_idle.png"
            "gui/button/mini_qs_hover.png" with Dissolve(0.15, alpha=True)

    image mini_auto_button:
        "gui/button/mini_auto_idle.png"
        on idle:
            "gui/button/mini_auto_idle.png" with Dissolve(0.15, alpha=True)
        on hover:
            "gui/button/mini_auto_idle.png"
            "gui/button/mini_auto_hover.png" with Dissolve(0.15, alpha=True)
        on selected_idle:
            "gui/button/mini_auto_hover.png" with Dissolve(0.15, alpha=True)
        on selected_hover:
            "gui/button/mini_auto_hover.png" with Dissolve(0.15, alpha=True)

# animations for choice buttons 

    image custom_choice_button:
        "gui/button/choice_idle_background.png"
        on idle:
            "gui/button/choice_idle_background.png"  with Dissolve(0.15, alpha=True)
        on hover:
            "gui/button/choice_idle_background.png"
            "gui/button/choice_hover_background.png" with Dissolve(0.15, alpha=True)
        on selected_idle:
            "gui/button/choice_selected_background.png" with Dissolve(0.15, alpha=True)
        on selected_hover:
            "gui/button/choice_selected_background.png" with Dissolve(0.15, alpha=True)

    image custom_choice_button_selected:
        "gui/button/choice_selected_background.png"
        on idle:
            "gui/button/choice_selected_background.png"  with Dissolve(0.15, alpha=True)
    

# animations for slot buttons (save/load)

    image save_slot_button:
        "gui/button/slot_save_idle_background.png"
        on idle:
            "gui/button/slot_save_idle_background.png"  with Dissolve(0.25, alpha=True)
        on hover:
            "gui/button/slot_save_idle_background.png"
            "gui/button/slot_save_hover_background.png" with Dissolve(0.25, alpha=True)
        on selected_idle:
            "gui/button/slot_save_idle_background.png" with Dissolve(0.25, alpha=True)
        on selected_hover:
            "gui/button/slot_save_hover_background.png" with Dissolve(0.25, alpha=True)
    
    image save_slot_button_empty:
        "gui/button/slot_save_idle_empty_background.png"
        on idle:
            "gui/button/slot_save_idle_empty_background.png"  with Dissolve(0.25, alpha=True)
        on hover:
            "gui/button/slot_save_idle_empty_background.png"
            "gui/button/slot_save_hover_empty_background.png" with Dissolve(0.25, alpha=True)
        on selected_idle:
            "gui/button/slot_save_idle_empty_background.png" with Dissolve(0.25, alpha=True)
        on selected_hover:
            "gui/button/slot_save_hover_empty_background.png" with Dissolve(0.25, alpha=True)

    image load_slot_button:
        "gui/button/slot_load_idle_background.png"
        on idle:
            "gui/button/slot_load_idle_background.png"  with Dissolve(0.25, alpha=True)
        on hover:
            "gui/button/slot_load_idle_background.png"
            "gui/button/slot_load_hover_background.png" with Dissolve(0.25, alpha=True)
        on selected_idle:
            "gui/button/slot_load_idle_background.png" with Dissolve(0.25, alpha=True)
        on selected_hover:
            "gui/button/slot_load_hover_background.png" with Dissolve(0.25, alpha=True)
    
    image load_slot_button_empty:
        "gui/button/slot_load_idle_empty_background.png"
        on idle:
            "gui/button/slot_load_idle_empty_background.png"  with Dissolve(0.25, alpha=True)
        on hover:
            "gui/button/slot_load_idle_empty_background.png"
            "gui/button/slot_load_hover_empty_background.png" with Dissolve(0.25, alpha=True)
        on selected_idle:
            "gui/button/slot_load_idle_empty_background.png" with Dissolve(0.25, alpha=True)
        on selected_hover:
            "gui/button/slot_load_hover_empty_background.png" with Dissolve(0.25, alpha=True)

# Confirm box

    image yes_button:
        "gui/button/yes_idle.png"
        on idle:
            "gui/button/yes_idle.png"  with Dissolve(0.15, alpha=True)
        on hover:
            "gui/button/yes_hover.png" with Dissolve(0.15, alpha=True)
        on selected_idle:
            "gui/button/yes_idle.png" with Dissolve(0.15, alpha=True)
        on selected_hover:
            "gui/button/yes_hover.png" with Dissolve(0.15, alpha=True)
    
    image no_button:
        "gui/button/no_idle.png"
        on idle:
            "gui/button/no_idle.png"  with Dissolve(0.15, alpha=True)
        on hover:
            "gui/button/no_hover.png" with Dissolve(0.15, alpha=True)
        on selected_idle:
            "gui/button/no_idle.png" with Dissolve(0.15, alpha=True)
        on selected_hover:
            "gui/button/no_hover.png" with Dissolve(0.15, alpha=True)
    