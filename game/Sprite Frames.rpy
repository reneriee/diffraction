#Emotion Transistion Transforms
define config.say_attribute_transition = Dissolve(0.3)

transform same_transform(old, new):
    old
    new with Dissolve(0.15, alpha=True)

define config.side_image_same_transform = same_transform

define config.side_image_only_not_showing = False

transform blinkwait:
    choice:
        3.0
    choice:
        0.2
    choice:
        5.0
    choice:
        4.2
    choice:
        0.75
    choice:
        1.7

#Persistent MC Portrait
init python:
     config.side_image_tag = "MC"

transform change_transform(old,new):
    contains:
        old
        alpha 1.0
        align 0.02 yalign 1.0
        linear 0.3 alpha 0.0
    contains:
        new
        xalign 0.02 yalign 1.0
        linear 0.3 alpha 1.0

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Faine", image="Faine")
define h = Character("Hen", image="Hen")
define mc = Character("MC", image="MC")

image side MC = LayeredImageProxy("MC", Transform(crop=(0,1,1533,1400), zoom=0.3))

layeredimage MC:
    group clothing:
        attribute raincoat default:
            "mcb2"
        attribute no_coat:
            "mcb1"
    group blinks:
        attribute neutral:
            "MC_neutral_blink"
        attribute judge:
            "MC_judge_blink"
        attribute shock:
            "MC_shock_blink"
        attribute sad:
            "MC_sad_blink"
        attribute happy:
            "mce5e"
    group brows:
        attribute neutral default:
            "mce1br"
        attribute judge:
            "mce2br"
        attribute shock:
            "mce3br"
        attribute sad:
            "mce4br"
        attribute happy:
            "mce5br"
    group mouth:
        attribute neutral default:
            "mce1m"
        attribute judge:
            "mce2m"
        attribute shock:
            "mce3m"
        attribute sad:
            "mce4m"
        attribute happy:
            "mce5m"
    group hair:
        attribute fringe default:
            "mcf"

####BLINKING ANIMATION CODE####
image MC_neutral_blink:
    "mce1e"
    blinkwait
    "mce1b"
    0.13
    "mcdb"
    0.13
    repeat

image MC_judge_blink:
    "mce2e"
    blinkwait
    "mce2b"
    0.13
    "mcdb"
    0.13
    repeat

image MC_shock_blink:
    "mce3e"
    blinkwait
    "mce3b"
    0.13
    "mcdb"
    0.13
    repeat

image MC_sad_blink:
    "mce4e"
    blinkwait
    "mcdb"
    0.15
    repeat
