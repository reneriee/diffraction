#Emotion Transistion Transforms
define config.say_attribute_transition = Dissolve(0.3)

transform same_transform(old, new):
    old
    new with Dissolve(0.15, alpha=True)

define config.side_image_same_transform = same_transform


transform migi:
    xalign 1.3

transform migi2:
    xalign 0.95

transform hidari:
    xalign -0.3

transform hidari2:
    xalign 0.05

transform mannaka:
    xalign 0.5

define poof = Dissolve(0.2)

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
#init python:

#    if persistent.show_mc_side_image == True:
#        config.side_image_tag = "MC"

# transform change_transform(old,new):
#     contains:
#         old
#         alpha 1.0
#         align 0.02 yalign 1.0
#         linear 0.3 alpha 0.0
#     contains:
#         new
#         xalign 0.02 yalign 1.0
#         linear 0.3 alpha 1.0

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
        attribute eyesclosed:
            "mcdb"
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
        attribute eyesclosed:
            "mce4br"
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
        attribute eyesclosed:
            "mce2m"
    group hair:
        attribute fringe default:
            "mcf"

image Faine Tiny = LayeredImageProxy("Fainey", Transform(crop=(0,0,1872,2150), zoom=0.45))
image Faine Small = LayeredImageProxy("Fainey", Transform(crop=(0,1,1872,1750), zoom=0.58))
image Faine = LayeredImageProxy("Fainey", Transform(crop=(0,1,1872,1600), zoom=0.70))
image Faine Big = LayeredImageProxy("Fainey", Transform(crop=(0,1,1872,1350), zoom=0.85))

layeredimage Fainey:
    always:
        "ffb1"
    group eyes:
        attribute neutral default:
            "f_neutral_blink"
        attribute unhappy:
            "f_neutral_blink"
        attribute anxious:
            "f_anxious_blink"
        attribute thoughtful:
            "f_thoughtful_blink"
        attribute eyesclosed:
            "ffdb"
        attribute mixed:
            "f_anxious_blink"
    group brows:
        attribute neutral default:
            "ffe1br"
        attribute unhappy:
            "ffe2br"
        attribute anxious:
            "ffe3br"
        attribute thoughtful:
            "ffe4br"
        attribute eyesclosed:
            "ffe1br"
        attribute mixed:
            "ffe2br"
    group mouth:
        attribute neutral default:
            "ffe1m"
        attribute unhappy:
            "ffe2m"
        attribute anxious:
            "ffe3m"
        attribute thoughtful:
            "ffe4m"
        attribute eyesclosed:
            "ffe1m"
        attribute mixed:
            "ffe1m"
    group hair:
        attribute hair default:
            "fff"

image Hen Tiny = LayeredImageProxy("Hendric", Transform(crop=(0,1,1800,1975), zoom=0.53))
image Hen Small = LayeredImageProxy("Hendric", Transform(crop=(0,1,1800,1800), zoom=0.60))
image Hen = LayeredImageProxy("Hendric", Transform(crop=(0,1,1800,1550), xoffset=50, zoom=0.70))
image Hen Big = LayeredImageProxy("Hendric", Transform(crop=(0,1,1800,1300), xoffset=50, zoom=0.85))
image Hen Giant = LayeredImageProxy("Hendric", Transform(crop=(0,1,1800,1500), xoffset=50, zoom=0.90))

layeredimage Hendric:
    group base:
        attribute coffee default:
            "hfb1"
        attribute monkey:
            "hfb2"
    group expressions:
        attribute neutral default:
            "h_neutral_blink"
        attribute avoidant:
            "h_avoidant_blink"
        attribute shocked:
            "h_shocked_blink"
        attribute smile:
            "hfe4e"
        attribute thoughtful:
            "h_thoughtful_blink"
        attribute wink:
            "hfe6e"
        attribute smug:
            "h_thoughtful_blink"
        attribute eyesclosed:
            "hfdb"
    group brows:
        attribute neutral default:
            "hfe1br"
        attribute avoidant:
            "hfe2br"
        attribute shocked:
            "hfe3br"
        attribute smile:
            "hfe4br"
        attribute thoughtful:
            "hfe5br"
        attribute wink:
            "hfe6br"
        attribute smug:
            "hfe3br"
        attribute eyesclosed:
            "hfe1br"
    group mouth:
        attribute neutral default:
            "hfe1m"
        attribute avoidant:
            "hfe2m"
        attribute shocked:
            "hfe3m"
        attribute smile:
            "hfe4m"
        attribute thoughtful:
            "hfe5m"
        attribute wink:
            "hfe6m"
        attribute smug:
            "hfe6m"
        attribute eyesclosed:
            "hfe5m"
    group hair:
        attribute fringe default:
            "hff"

image Otto Tiny = LayeredImageProxy("Totto", Transform(crop=(0,1,1800,2100), xoffset= 200, yoffset= 30, zoom=0.50))

layeredimage Totto:
        always:
            "otto"

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

image f_neutral_blink:
    "ffe1e"
    blinkwait
    "ffe1b"
    0.13
    "ffdb"
    0.13
    repeat

image f_unhappy_blink:
    "ffe2e"
    blinkwait
    "ffdb"
    0.20
    repeat

image f_anxious_blink:
    "ffe3e"
    blinkwait
    "ffe3b"
    0.13
    "ffdb"
    0.13
    repeat

image f_thoughtful_blink:
    "ffe4e"
    blinkwait
    "ffe4b"
    0.13
    "ffdb"
    0.13
    repeat

image h_neutral_blink:
    "hfe1e"
    blinkwait
    "hfe1b"
    0.13
    "hfdb"
    0.13
    repeat

image h_avoidant_blink:
    "hfe2e"
    blinkwait
    "hfe2b"
    0.13
    "hfdb"
    0.13
    repeat

image h_shocked_blink:
    "hfe3e"
    blinkwait
    "hfe3b"
    0.13
    "hfdb"
    0.13
    repeat

image h_thoughtful_blink:
    "hfe5e"
    blinkwait
    "hfe5b"
    0.13
    "hfdb"
    0.13
    repeat
