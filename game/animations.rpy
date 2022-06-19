init -2:
# animations for quick menu buttons

    image quickmain_button:
        "gui/button/quickmain_idle.png"
        on idle:
            "gui/button/quickmain_idle.png" with Dissolve(0.22, alpha=True)
        on hover:
            "gui/button/quickmain_idle.png"
            "gui/button/quickmain_hover.png" with Dissolve(0.22, alpha=True)
        on selected_idle:
            "gui/button/quickmain_hover.png" with Dissolve(0.22, alpha=True)
        on selected_hover:
            "gui/button/quickmain_hover.png" with Dissolve(0.22, alpha=True)

    image quickprefs_button:
        "gui/button/quickprefs_idle.png"
        on idle:
            "gui/button/quickprefs_idle.png"  with Dissolve(0.22, alpha=True)
        on hover:
            "gui/button/quickprefs_idle.png"
            "gui/button/quickprefs_hover.png" with Dissolve(0.22, alpha=True)
        on selected_idle:
            "gui/button/quickprefs_hover.png" with Dissolve(0.22, alpha=True)
        on selected_hover:
            "gui/button/quickprefs_hover.png" with Dissolve(0.22, alpha=True)

    image quickhistory_button:
        "gui/button/quickhistory_idle.png"
        on idle:
            "gui/button/quickhistory_idle.png"  with Dissolve(0.22, alpha=True)
        on hover:
            "gui/button/quickhistory_idle.png"
            "gui/button/quickhistory_hover.png" with Dissolve(0.22, alpha=True)
        on selected_idle:
            "gui/button/quickhistory_hover.png" with Dissolve(0.22, alpha=True)
        on selected_hover:
            "gui/button/quickhistory_hover.png" with Dissolve(0.22, alpha=True)
            
    image quickauto_button:
        "gui/button/quickplay_idle.png"
        on idle:
            "gui/button/quickplay_idle.png"  with Dissolve(0.22, alpha=True)
        on hover:
            "gui/button/quickplay_hover.png"
            "gui/button/quickplay_hover.png" with Dissolve(0.22, alpha=True)
        on selected_idle:
            "gui/button/quickauto_hover.png" with Dissolve(0.22, alpha=True)
        on selected_hover:
            "gui/button/quickauto_hover.png" with Dissolve(0.22, alpha=True)

    image quickskip_button:
        "gui/button/quickskip_idle.png"
        on idle:
            "gui/button/quickskip_idle.png"  with Dissolve(0.22, alpha=True)
        on hover:
            "gui/button/quickskip_hover.png"
            "gui/button/quickskip_hover.png" with Dissolve(0.22, alpha=True)
        on selected_idle:
            "gui/button/quickskip_hover.png" with Dissolve(0.22, alpha=True)
        on selected_hover:
            "gui/button/quickskip_hover.png" with Dissolve(0.22, alpha=True)


# animations for slot buttons (save/load)

    image save_slot_button_empty:
        "gui/button/slot_save_idle_background_empty.png"
        on idle:
            "gui/button/slot_save_idle_background_empty.png"  with Dissolve(0.25, alpha=True)
        on hover:
            "gui/button/slot_save_idle_background_empty.png"
            "gui/button/slot_save_hover_background_empty.png" with Dissolve(0.25, alpha=True)