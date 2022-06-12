init -2:
# animations for buttons

    image quickmain_button:
        "gui/quickmain_idle.png"
        on idle:
            "gui/quickmain_idle.png"  with Dissolve(0.25, alpha=True)
        on hover:
            "gui/quickmain_idle.png"
            "gui/quickmain_hover.png" with Dissolve(0.25, alpha=True)
        on selected_idle:
            "gui/quickmain_hover.png" with Dissolve(0.25, alpha=True)
        on selected_hover:
            "gui/quickmain_hover.png" with Dissolve(0.25, alpha=True)