# The script of the game goes in this file.

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
    or renpy.get_screen("help")
    or renpy.get_screen("confirm")):
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

define in_game_day = 1
# Declare characters used by this game. The color argument colorizes the
# name of the character.
image morgana = "recruiter_one.png"
image barty = "recruiter_two.png"
image migel = "recruiter_three.png"
image hale = "recruiter_four.png"
image blink = "blink.png"
image silh1 = "silh1.png"
image silh2 = "silh2.png"
image silh3 = "silh3.png"
image silhgroup = "silhgroup.png"

image ctc_arrow:
    pause 0.2
    linear 0.3 alpha 0.0
    "gui/arrow.png"
    yalign 0.937 xalign 0.755
    block:
        linear 0.3 alpha 1.0
        pause 2.0
        linear 0.3 alpha 0.0
        pause 0.2
        repeat

default protag_name = "April"
default Did_Nothing = False
default Hen_Name = "???"
default Otto_Name = "Hat Boy"
default Lexi_Name = "Purse Girl"
default Kim_Name = "Cashier Woman"
default Day_1_Guy_Choice = "that guy"
default Question_Hen = False
default Ask_Collab = False
default Apologize_to_Hen = False
default Day_1_Guy_Return = "No One"

define z = Character (None, ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define f = Character("Faine", image="Faine", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define h = Character("[Hen_Name]", image="Hen", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define mc = Character("[protag_name]", image="MC", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define na = Character("???", ctc ="ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define p = Character("[protag_name]", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define b1 = Character("Recruiter 1", image = "morgana", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define ba = Character("Recruiter 7", image = "barty", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define bb = Character("Recruiter 3", image = "hale", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define b3 = Character("Recruiter 12", image = "migel", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define c = Character("Woman", image = "morgana", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define o = Character("[Otto_Name]", image="Otto", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define l = Character("[Lexi_Name]", image="Lexi", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define k = Character("[Kim_Name]", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define d = Character("Dad", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")

image mini_cg_1 = "memorycg.png"
image mini_cg_2 = "ernestcg.png"
image mini_cg_3 = "phonecg.png"
image mini_cg_4 = "gallerycg.png"
image Hen_cg = "Hen_cg.jpeg"
image Faine_cg = "Faine_cg.png"
image Store_Blurred = im.Blur("images/Backgrounds/bg store.jpg", 2.5)
image Fair_Blurred = im.Blur("images/Backgrounds/bg job fair.png", 2.5)
image Fair_Blurred_2 = im.Blur("images/Backgrounds/bg job fair rain.png", 2.5)

define flash = Fade(0.1, 0.0, 0.5, color="#666")
define fadehold = Fade(0.7, 0.3, 0.7)

init python:
    renpy.music.register_channel('ambient', 'music', True, True, True)

# The game starts here.
label start:
    $renpy.show_layer_at(blur_bg, layer= "master", camera = True)

    stop music fadeout 2.0

    $ protag_name = renpy.input ("My name is...")
    $ protag_name = protag_name.strip()

    if protag_name == "":
        $ protag_name = "April"

## Start inputting date for widgets here (weather, date, etc)
    #$weather_stuff("sunny", 5, 1, "Thursday", 15)
    #show screen widgets

################################################################################

    #scene bg mc room
    #with fade
    #z "(Insert intro text here)"
    #z "(Mc leaves the room through her window after having checked social media, done her makeup and got dressed)"
    #z "(EXIT)"
    #hide bg mc room
    #show bg scenery2
    #mc neutral "Out in the streets."
    #mc "It's raining should have brought umbrella oh well, would have to have left through the door for that."
    #mc "Thinking about this I wonder:"
    #menu:
    #    "(Where should I go?)"
    #    "To the park":
    #        "I still remembered the way there well."
    #        "It would be a short walk."
    #        jump choice_thatplace
    #    "Go to the convenience store for breakfast":
    #        "I need to eat something..."
    #        jump choice_store
    #    "cheat":
    #        jump mell_cheat
    #    "Beginning":
    #        jump starting

    #label choice_thatplace:
    #hide bg scenery2
    #hide screen widgets

    ##### New day/time example
    #$weather_stuff("rainy", 12, 31, "Friday", 20)
    #show screen widgets

    #show bg thatplace
    #with fade
    #mc judge "(MC thoughts blablabla, this is the place I met faine that day.)"
    #show Faine
    #mc "(Totally forgot wow so emotional, this is a good photo op)"
    #show Faine at hidari
    #"You spot someone who resembles your old friend...but is it really him?"
    #f anxious "Who are you?"
    #mc shock "You don't remember me?"
    #f unhappy "No..."
    #show Faine at migi
    #show Hen at hidari
    #mc "If that's how you want to be."
    #hide Hen
    #show Faine at mannaka with poof
    #hide Faine
    #show Hen at mannaka with poof
    #f "It's just how I am."
    #show Faine Small at hidari2 with poof
    #show Hen Small at migi2 with poof
    #mc sad "You don't have to be so harsh about it."
    #f anxious "Oh."
    #hide Hen
    #f thoughtful "Sorry about that. I didn't mean to be."
    #"Faine takes a small step towards you."
    #show Faine Big at mannaka with poof
    #f "I am big now."
    #hide Faine Big
    #show Faine
    #with poof
    #z "It's how it is."
    #hide Faine
    #show Hen Big with poof
    #"To be continued..."
    #hide bg thatplace
    #hide Hen
    #jump choice_done

    #label choice_store:
    #hide bg scenery2
    #show bg store
    #"(MC looking around store)"
    #show h-p2
    #show h-e1
    #show h-m1
    #h "Boo."
    #h "I have an incredibly important and essential question for you."
    #"To be continued"
    #jump choice_done

    #label choice_done:

    #label starting:

    scene bg black

    play music "<loop 0.00>Music/Prologue.mp3" fadein 5.0
    z "I'll leave Faine in your capable hands, Alright? - Alright!"
    z "I gotta go or I'll lose the duck!"
    p "Wha- you can’t- ..."
    p "Annnd he’s already gone..."
    p "Figures."
    p "We come all the way up a mountain and he abandons us to go on a literal wild goose chase."
    p "Hey Faine, you okay with this?"
    f "I think it was a wild duck chase."
    p "A wild du-....That's really not the point here."
    f "What is the point then?"
    p "... Nevermind -- You don't have a camera right? Are you just using your phone or something?"
    f "I’m okay without anything. I'll just watch you."
    z "*FLASH*" with flash
    show mini_cg_1 with Dissolve(3)
    f "Huh - why’re you taking a picture of me?"
    p "Because you have to participate somehow here; how are you going to learn to be a famous photographer at this rate?"
    f "I don’t take pictures though."
    p "Maybe you don’t but I do, I’ll be a super famous photographer one day."
    f "That sounds cool, I’m sure you’ll be great."
    p "...Are you trying to make fun of me?"
    f "No? I think you could do it."
    p "Oh."
    p "...."
    p "...What if-"
    p "...What if I said I want to be a well known influencer too...?"
    f "You’ll do amazing for sure."
    p "...."
    f "...."
    p "What if I wanted to be a T-rex?"
    stop music fadeout 5.0
    f "I heard they sell those blow up dinosaur costumes in the next town over?"
    p "Ah geeez…"
    hide mini_cg_1 with dissolve

    scene bg black
    $weather_stuff("sunny", 5, 1, "Thursday", 15)
    show screen widgets
    with fade
    na "Miss [protag_name]...?"
    na "Miss [protag_name]...?"

    show bg job fair
    with fade

    show blink with Dissolve(0.03)
    show blackscreen with Dissolve(0.03)
    pause 0.1
    hide blackscreen with Dissolve(0.03)
    hide blink with dissolve
    pause 0.05
    show blink with Dissolve(0.03)
    show blackscreen with Dissolve(0.03)
    pause 0.1
    hide blackscreen with Dissolve(0.03)
    hide blink with dissolve

    mc shock "...Huh?"
    play ambient "Audio/Crowd3.mp3" fadein 5.0
    play music "<loop 0.00 to 72.00>Music/Job_Fair.mp3" fadein 5.0 volume 0.70
    show morgana:
        size(765,1120)
        xalign 0.45
        yalign 1
    with dissolve
    b1 "Are you alright?"
    mc "(Ah... stupid, why am I daydreaming at a time like this?!)"
    menu:
        mc "I-"
        "Apologize, ask her to repeat herself.":
            $ pretend_listen = False
            $ who_is_she = False
            jump choice_apologize_repeat
        "Pretend you were listening.":
            $ pretend_listen = True
            jump choice_pretend_listen
        "Ask her who she is.":
            $ who_is_she = True
            jump choice_who_is_she

    label choice_apologize_repeat:
    mc neutral "Sorry, could you please repeat yourself?"
    b1 "As I was saying, we currently can’t afford to invest in anyone without at least 3 years of relevant work experience."
    play sound "Audio/Page_Flip.mp3" volume 0.10
    queue sound "Audio/Page_Flip.mp3" volume 0.40
    queue sound "Audio/Page_Flip.mp3"
    z "The woman vaguely flips through my portfolio. It’s clear based on how quickly she turns each page that she’s barely taking anything in."
    b1 "Now, that isn’t to say your work isn’t good; you might even be a good fit for our company once you get some experience."
    b1 "But unfortunately, 3 years of personal social media work isn’t quite our standard for “experience”."
    mc sad "...I understand."
    mc "(Of course... It’s not like I haven’t heard that one before.)"

    jump apologize_repeat_continue

    label choice_pretend_listen:

    mc neutral "Yes, of course."
    b1 "So you don’t have any questions?"
    mc shock "Uhm... "
    mc "(...Questions? ...Questions about what?)"
    z "The woman looks at me with a scrutinizing gaze before sighing."
    b1 "...Perhaps you're more suited elsewhere."
    b1 "Having some photography skill isn’t going to cut it if the only thing backing you up is 3 years of social media “experience”-"
    b1 "And poor listening skills."
    mc "(I guess I shouldn't have lied...)"
    mc sad "I... see..."
    mc "Thank you for your time then."

    jump apologize_repeat_continue

    label choice_who_is_she:
    mc neutral "Uh, who are you again?"
    b1 "...Excuse me? Are you serious?"
    mc shock "Y-yes?"
    z "The woman blinks at me slowly, confusion clear on her face."
    b1 "You {i}are{/i} the one applying to work in my studio, correct?... And you’re asking me who I am?"
    mc neutral "I-..."
    z "It's clearly too late to backtrack as I already hearing snickers and whispers of other people close by."
    b1 "...Perhaps I may give you some professional advice-"
    z "She continues on without waiting for my response."
    b1 "Our studio and many others don't quite consider 3 year of personal social media as “experience”."
    b1 "You should try working more professional gigs first. Please excuse me."

    hide morgana with dissolve

    z "The woman clearly dismisses me to speak to another attendee nearby."
    mc shock "...."
    z "The snickers from the surrounding crowd only gets louder."
    mc sad "(Let’s... try a booth a little bit further away from here next.)"

    jump who_is_she_continue

    label who_is_she_continue:

    hide morgana
    hide bg job fair
    show bg job fair
    show hale:
        size(690,1120)
        xalign 0.45
        yalign 5
    with fadehold

    bb "Ohhhh, so you do photography and social media. Does that mean you know how to use editing software too?"
    mc neutral "Yes, I do."
    bb "That's great! We've been looking for someone like you!"
    mc shock "...Really-!?"
    bb "You see, our little start-up needs to get someone that can take the photos, put together a few viral videos-"
    mc "(Wait- Videos...?)"
    bb "Maybe make some promotional flyers or postcards, and properly set up our websites."
    bb "So, when can you start?"
    mc judge "...You are hiring for a photographer, right?"
    bb "That's right!"
    mc "(....)"
    mc "Maybe I can get back to you on this one."

    jump who_is_she_Conclude

    label apologize_repeat_continue:

    hide morgana
    hide bg job fair
    show bg job fair
    show barty:
        size(765,1120)
        xalign 0.45
        yalign 5
    with fadehold

    ba "You know-"
    ba "I’d be quite happy to give you a chance despite your bland, boring portfolio."
    ba "But you need to want it! To have a passion for it!"
    ba "Our biggest clients all want tasteful, {i}cultured{/i}, body shots of themselves and we are a discreet studio dedicated to ART."
    mc judge "...."

    if pretend_listen == True:
        ba "Wait... weren’t you the girl zoning just a few booths over?"
        mc shock "(H-how does he know that?)"
        ba "Yeah, it's definitely you! Not many people with pink hair around here."
        z "He flips carelessly through my portfolio with one hand."
        ba "You have no “real skills” - besides playing around on social media - and you apparently have no passion if you can’t even listen to passionate people."
        ba "No skills, no passion, no culture - I'll never work with you!" with hpunch
        mc judge "(You can't be serious...)"
    else:
        ba "You’re just not convincing me right now with all this social media nonsense... "
        ba "We just can’t take on someone who’s done nothing but play around online over the last few years."
        ba "If you’re that good, you should start figuring out how to get some solid marketable skills or add some culture to your portfolio!"
        mc "(No thanks...)"

    hide bg job fair
    hide barty
    show bg job fair
    show migel:
        size (770,1365)
        xalign 0.45
        yalign -0.05
    with fadehold

    b3 "Wow, your portfolio is excellent!"
    mc shock "(Wait, what?!)"
    b3 "Mhm, Mhm... yes... I think we could definitely offer you a place on our internship program."
    mc "...Really-!?"
    b3 "We can’t pay you of course, but you’ll get a whole lot of exposure and work experience!"
    mc judge "(.......Should have known.)"

    if pretend_listen == True:
        b3 "You don’t even have to listen to me all the time. We’re really casual here, I promise!"
        mc startled "(Oh, come'on! Not this again!)"
        b3 "See, you're already doing it, we'll get along great!"
    else:
        b3 "So how about it!? I’m sure we can make it worth your while!"

    mc eyesclosed "(*Sigh*)"
    stop music fadeout 3.0
    mc sad "I'll give it some thought...thanks."

    hide migel

    jump all_rejections

    label who_is_she_Conclude:

    hide hale
    hide bg job fair
    show bg job fair
    show barty:
        size(765,1120)
        xalign 0.45
        yalign 5
    with fadehold

    ba "I’d be quite happy to give anyone a chance despite their bland, boring portfolio."
    ba "Afterall, our biggest clients all want tasteful, {i}cultured{/i}, body shots of themselves and we are a discreet studio dedicated to ART."
    ba "Anyone except {i}you{/i}."
    mc shock "(-What?!)"
    mc "Why?- I mean, can I ask why?"
    ba "Forget all the social media nonsense and playing around online for a few years-"
    ba "I saw the commotion you made a few booths over, disrespecting people with passion!"
    ba "If you even want me to consider you, you should start figuring out how to get some solid marketable skills or add some culture to your portfolio!"
    mc sad "(There goes that chance...)"

    jump all_rejections

    label all_rejections:

    scene bg job fair
    with fadehold
    mc eyesclosed "(No, no, no, no. Nothing but rejections.)"
    mc sad "(I was told applying at job fairs was supposed to be easier but that’s not true at all. At least email rejections aren’t as brutal.)"
    mc "(This was such a waste of time... )"
    stop ambient fadeout 8
    mc judge "(...I should just put as much distance between myself and Mr. “cultured photos”, as possible.)"
    play music "<loop 0.00>Music/Prologue.mp3" fadein 5.0 volume 0.75
    mc eyesclosed "Hahhh... "
    mc sad "Another day, another disappointment, I guess."
    show Fair_Blurred with Dissolve(2)
    mc judge"({i}That sounds cool, I’m sure you’ll be great.{/i})"
    mc "(Great my butt.)"
    mc sad "(I wonder what that boy would think if he saw me today?)"
    mc "(Would he still think I'm doing great?)"
    mc eyesclosed "(What a silly thought-)"
    mc "(Thinking about some kid after all this time.)"
    mc sad "(But it's a bit sad...)"
    mc "(I remember what he said perfectly but I can’t quite remember his name.)"
    stop music fadeout 4.0
    show silhgroup with Dissolve(1):
        size (1400,740.09)
        xalign 0.2
        ypos 250
        alpha 0.4
    mc neutral "(I swear it started with an ‘F’...Right?)"
    play sound "Audio/note1.mp3"
    show silh1 with dissolve:
        size (906.76,1000)
        xalign -0.1
        ypos 250
    mc neutral "(Was it F-Fang?)"
    play sound "Audio/note2.mp3"
    show silh2 with dissolve:
        size (600,750)
        xalign 0.8
        ypos 300
        alpha 0.75
    mc sad "(No... I think it could've been Frank?)"
    play sound "Audio/note3.mp3"
    show silh3 with dissolve:
        size (2900,3198.21)
        xpos 800
        ypos -300
    mc eyesclosed "(Maybe it was more of a Finn... ?)"
    play sound "Audio/note4.mp3"
    show Faine Tiny behind silh3 with Dissolve(1.0)
    mc shock "(Wait.)"
    show silh2 with dissolve:
        xalign 0.6
    show silh3 with dissolve:
        xpos 200
    show silh1 with dissolve:
        xalign 0.2
    mc "(Isn’t that-)"

    show blackscreen with poof

    mc "...{i}Faine{/i}."

    hide Faine Tiny with poof

    stop music fadeout 1.0
    play ambient "<loop 0.00>Audio/Crowd3.mp3" fadein 2.0
    show silh3:
        xpos -2000
    hide blackscreen with dissolve
    show silh2 with dissolve:
        xalign 0.2
    show silh1 with dissolve:
        xalign 0.5
    mc "H-hey–!"
    hide silh3 with dissolve
    show silh1:
        xalign 0.75
    hide silh2
    with dissolve
    hide silh1 with dissolve
    hide silhgroup
    with dissolve
    z "The quiet exclamation is lost in the noisy crowd, as is the sudden flicker of an all too familiar face in the distance."
    z "Without realizing, I take a few steps forward."
    hide Fair_Blurred with dissolve
    mc "(It can't be...)"
    mc "(Faine?!)"
    mc "(Why's he here? Where has he been? Did he look different !? -)"
    mc "(He-)"
    z "A million questions surface, but before there’s time to think about any of them, I’m already running after him."
    play sound "Audio/MC_Run.mp3"
    z "The crowd parts around me in a blur as I head in the direction I last saw him."
    #Add two more lines here

    z "Only in the rush, I’d forgotten to look where I was going... "
    play sound "Audio/Crash.mp3"
    stop ambient fadeout 2.0
    show Hen Giant shocked with poof
    mc startled "Wai-... Ngh-" with hpunch
    hide Hen Giant with poof
    play sound "Audio/Cell_Drop.mp3"
    h "Hey- ah-... Watch it!"
    scene Hen_cg with fadehold:
       size (1920, 1080) crop (1460, 1062, 2050, 1116)
       linear 5 crop (1460, 200, 2050, 1116)
    z "The man I collided with utters a panicked curse as his things clatter to the ground around him."

    scene Hen_cg:
        size (1920, 1080)
    with Dissolve(0.7)

    # add 1-2 more lines here
    z "A few startled people nearby also quickly back away eying us with a misxture of surprise and concern."
    mc startled "(There’s no time to worry about this, I have to get up!)"
    z "I quickly gather up my dropped portfolio and ready myself to run again when-"

    scene bg job fair with dissolve
    play sound "Audio/Crack.mp3"
    z "*CRACK*"
    mc neutral " .... "
    h " .... "
    mc crisis "(Oh crap ...)"
    show mini_cg_3 with Dissolve(2)
    z "There, {w=0.5} beneath my shoe,{w=0.5} lies a very shiny,{w=0.5} very new-looking {w=0.5}...and a {i}very{/i} broken-beyond-repair smartphone."
    hide mini_cg_3 with Dissolve(2)

    menu:
        mc "What should I do!?"
        "Keep running.":
            mc "(Ugh- I can’t deal with this now, I need to find Faine!)"
            z "Tearing my glance away from  the cracked phone and the hopefully still disoriented stranger, I turn and run, quickly resuming my pursuit."
            play sound "Audio/MC_Run.mp3"
            mc shock "(It’s probably nothing too bad... right?)"
            stop sound fadeout 2.0
            stop music fadeout 2.0
            jump Find_Faine
        "Apologize, then run after Faine.":
            mc "(Ugh- I can’t deal with this now, I need to find Faine!)"
            z "Looking up from the cracked phone, I catch the stranger’s gaze and hesitate for a moment."
            mc shock "(It’s no good, I don’t have time for this..)"
            mc startled "I-I’m sorry! I have to go ..."
            mc "I’ll come back later!"
            play sound "Audio/MC_Run.mp3"
            z "Without looking for a response, I quickly turn to run after Faine once again."
            stop sound fadeout 2.0
            $ Apologize_to_Hen = True
            stop music fadeout 2.0
            jump Find_Faine
        "Stand around awkwardly.":
            stop music fadeout 2.0
            jump Stay_Hen_1
        "Stop and apologize to the stanger, attempt to make amends.":
            $ Apologize_to_Hen = True
            stop music fadeout 2.0
            jump Stay_Hen_2

    label Stay_Hen_1:
    $ Did_Nothing = True
    z "In an instant, all thoughts of pursuing Faine had slipped from my mind in the face of this new scenario."
    z "Meeting the stranger’s gaze, I quickly step back as he moves to gather up his belongings."
    z "I find myself unable to do anything but watch."
    show Hen shocked with dissolve
    h "Nonono ... look at what she’s done to you-..."
    z "He examines the shattered phone."
    z "Without so much as looking at me, he begins to frantically press buttons, all the while clutching the device as though it were his injured child."
    h thoughtful "Cmon, cmon, please be alive!"
    z "Unfortunately he seems to have no luck."
    show Hen eyesclosed with poof
    mc shock "(Should I help him?)"
    mc sad "(It’s probably too late for me to do anything now though... )"
    show Hen thoughtful with poof
    z "I continue to hesitate."
    z "A few more attempts later, he finally lowers his hands tellingly, before directing a pointed glance up at me."
    show Hen smile with poof
    mc judge "(I’m so screwed...)"
    z "Picking himself and his belongings back up, he moves towards me with a smile?"
    show Hen Big smile with poof
    h "So, it looks like {i}your{/i} foot broke {i}my{/i} phone."

    jump Stay_Hen_Conclusion

    label Stay_Hen_2:
    z "In an instant, all thoughts of pursuing Faine had slipped from my mind in the face of this new scenario."
    z "Meeting the stranger’s gaze, I quickly remove my shoe from his phone."
    mc crisis "I’m so sorry! Let me help you."
    z "Without even waiting for confirmation, I move to help him gather up his belongings, which luckily hadn’t scattered too far."
    show Hen shocked with dissolve
    z "Meanwhile, without so much as looking at me, he’d begun to frantically press the buttons of his shattered phone, all the while clutching the device as though it were his injured child."
    h "Cmon, cmon, please be alive!"
    show Hen thoughtful with poof
    z "Nervously, I look at the screen, silently hoping it might somehow be less damaged than it looks."
    mc sad "(Well, either way I really don’t have the money to fix this ... )"
    z "After a few more failures, he finally lowers his hands."
    h eyesclosed "It’s no good ... it’s dead."
    show Hen avoidant with poof
    z "Standing up, he picks up the items I’d returned to him earlier, sliding the phone into his pocket and turning his full attention towards me."

    jump Stay_Hen_Conclusion

    label Stay_Hen_Conclusion:

    show Hen with dissolve
    mc shock "Uhm..."

    menu:
        mc "(What should I do?)"
        "(Tell him you don’t know what to do.)":
            jump Dont_Know
        "(Ask him how much the phone was worth. See if you have money to fix it.)":
            jump Money_To_Fix
        "It was an accident!!":
            jump Insist_Accident

    label Dont_Know:
    mc sad "I'm sorry, I actually don't know what to do."
    if Apologize_to_Hen == True:
        show Hen thoughtful with poof
        z "He eyes me critically as if searching for something."
        mc "(I apologized already but I still don't feel like that's enough.)"
        z "His eyes dart down to his still broken phone and then looks back up to me once more."
        show Hen eyesclosed with poof
        "Before he lets out a sigh."
    else:
        h "Really? Nothing?"
        h "I'm sure we could use some creative imagination here."
        z "I attempt to use my imagination."
        z "I still have nothing."
        mc sad "I...I really don't know."
        show Hen eyesclosed with poof
        z "He shakes his head, letting out an exasperated sigh."
        h smile "Making me do all the heavy lifting of my poor dead phone here."

    jump Dont_Know_Conclude

    label Insist_Accident:

    mc startled "It was an accident! I swear!"
    if Apologize_to_Hen == True:
        h neutral "Oh? So that apology from earlier wasn't an honest one?"
        h "{i}I'm so sorry! Let me help you,{/i} she says."
        h "But now you're insisting it's all an accident."
        mc judge "(...He has a point.)"
        mc sad "Is...is there someway I can make it up to you?"
    else:
        h neutral "Was it now?"
        h "So you just accidentally ran through a fairly crowded area of people."
        h smug "And accidentally weren't paying attention to where you were going."
        h smile "And {i}accidentally{/i} got up carelessly in your rush before stepping on my phone?"
        mc judge "(When he puts it that way...)"
        mc sad "M-maybe I can make it up to you somehow?"

    jump Insist_Accident_Conclude

    label Money_To_Fix:

    mc sad "H-how much would it cost to buy a new one... "
    mc "(I definitely can’t afford it but... it’s better to know what I’m working with here at least... )"
    z "Or so I thought."
    h smile "$5000.00"
    mc startled "($5000?!?!)"
    mc shock "(What sort of phone costs $5000???)"
    mc "(He’s got to be messing with me-)"
    mc sad "(But then again his clothes do look kind of expensive... )"
    mc judge "Are... you making a joke or something?"
    mc "I’ve never heard of a phone that costs that much... "
    h neutral "Nope."
    z "I stare at him for a moment."
    mc sad "(Is he really being serious...?)"
    mc shock "Uh... I-I’m sorry but I really don’t have that kind of money... "
    mc "Is there any other way I could make up for this?"

    if Did_Nothing == True:
        h smile "Nope."
        mc shock "(?!?!)"
        mc "I-!?"
        h avoidant "I’m just joking. "

    label Insist_Accident_Conclude:
    label Dont_Know_Conclude:

    h thoughtful "Hmmm let me see..."
    z "He makes a show of thinking for a moment."
    h "How about-"
    z "He begins, but all of a sudden we are interrupted by a shout."
    play music "<loop 0.00 to 72.00>Music/Job_Fair.mp3" fadein 5.0 volume 0.60
    na "Hey Hen! Over here!"
    show Hen neutral with poof
    z "A voice calls out, and the stranger before me reflexively turns to look in the direction the voice is coming from."
    show Hen Tiny:
        xalign 0.475
    with dissolve
    z "Two new people emerge from the crowd, a woman clutching a name brand purse and a boy waving his hand in the air to get our attention."
    show Otto Tiny at migi2
    show Lexi Tiny at hidari
    with dissolve
    mc shock "(Are they friends of his?)"
    l question "You get lost or something? We’ve been looking all over the campus for you."
    o "You didn’t answer your phone either."

    $ Hen_Name = "Hen(?)"

    h eyesclosed "Sorry, sorry, my phone got smashed so I didn’t get anything."
    show Hen neutral
    show Otto puppy
    show Lexi neutral
    with poof
    z "He holds up his cracked and dead phone in emphasis."
    o "Damn, that sucks... "
    h smile "Yup."
    z "Everyone waits a beat to see if Hen will explain what happened, but he didn’t seem to elaborate any further."
    z "He simply shrugs."
    l "...."
    o "...."
    mc judge "...."
    z "Only then, does the girl seem to notice me."
    l question "Oh, who’s this? Another fan?"
    z "She seems to study me for a moment."
    mc shock "(Fan... ? Should I feel offended?)"
    mc judge "(No, I’m just the person that broke his phone... )"
    mc neutral "I’m-"
    h neutral "-A possible new collab."
    show Hen Tiny wink with poof
    pause 0.5
    show Hen Tiny neutral with poof
    pause 0.1
    show Hen Tiny wink with poof
    pause 0.5
    show Hen Tiny neutral with poof
    z "Hen cuts me off suddenly, sending the most suggestive winks to the other two."
    show Otto smile with poof
    show Lexi neutral with poof
    z "It must have been enough because they nod understandingly."
    mc shock "(Wait, what collab? What does that mean?)"
    l "Gotcha, we’ll head back to the gym then. Join us after when you’re done."
    mc "(Done with what? They're clearly not even trying to include me in this conversation-)"
    z "No one seems to provide further context for anything though and the two walk off to the other end of the auditorium."
    hide Otto Tiny
    hide Lexi Tiny
    with dissolve
    hide Hen Tiny
    show Hen neutral
    with dissolve
    z "Hen turns back towards me as if nothing just happened."
    h smile "Alright, let’s go, I have the perfect idea."
    hide Hen with dissolve
    z "Without so much as waiting for further confirmation, he'd already begun to move, clearly expecting me to follow."

    menu:
        mc ""
        "(Go with him quietly.)":
            mc sad "It's not like I have much of a choice on whether I want to go or not."
            z "I hesitantly follow, walking a few steps behind him."
            show Hen thoughtful with dissolve
            z "Once he notices me following, Hen half turns and gives me an unreadable look."
            mc shock "(What?)"
            z "But he continues walking right after."
            hide Hen with dissolve
            jump Go_Quietly
        "(Don't go with him until he's explains where you're going and what you're doing.)":
            $ Question_Hen = True
            jump Explain_First
        "(Don't go with him/leave.)":
            jump Leave_Him_1

    label Leave_Him_1:
    mc judge "(Where's he going? There's no way I'm going with this guy.)"
    z "I look between Hen and the venue exit calculating if I might just be able to make it past him."
    z "Before I can even consider anything though, a voice cuts back in."
    h "A cautious one, I see!"
    show Hen smile with dissolve
    h "You wouldn't happen to be considering sneaking off, would you?"
    mc shock "(...?!)"
    mc "(...There goes that plan I guess.)"
    mc "I-"
    mc neutral "...."
    mc "Look, I can't just follow some stranger to who-knows-where. I don't even know if Hen's your real name."
    h neutral "Well, it's Hendric, but Hen is fine."
    $ Hen_Name = "Hen"
    mc judge "(That's not really the main issue here.)"
    h smile "But alas, you've caught me. I guess I have to share my masterplan with you now."
    h neutral "I was going to ask you to buy me some candy."
    mc shock "...."
    mc "...Candy...Seriously?"
    h "Yup."
    mc neutral "(He...doesn't look like he's lying...)"
    mc "(But I don't know if I should trust him still...)"
    h smile "So? Let's go then."
    $ Question_Hen = True

    jump Leave_Him_1_Conclude

    label Explain_First:

    mc "Hey- wait a second! Hen... right?"
    show Hen with dissolve
    z "Hen turns towards me once more."
    mc neutral "Where are we going? And at least tell me what we're doing?"
    mc judge "(I'm not just going somewhere when I have no idea what's going on!)"
    h "It's Hendric... but Hen is fine."
    $ Hen_Name = "Hen"
    h thoughtful "As for where we're going and what we're doing... –"
    h "...."
    h smile "We're going to the store so you can buy me some candy."
    mc shock "(....Candy?)"
    mc "(I hadn’t thought it was possible to feel any more confused than I already did... )"
    mc judge "Uhh... I don’t think I understand... "
    mc "Is this another joke?"
    h "Nope."
    mc neutral "We’re... going to the store... so I can buy you candy."
    h "Yup."
    mc judge "The store... down the street?"
    h "Mhm."
    z "He continues to smile at me as though this makes perfect sense. "
    mc "(This makes no sense at all... )"
    mc "(Am I missing something here? This has to be some sort of prank.)"
    mc sad "(Was he lying about how much that phone was worth? But even then... )"
    mc shock "(Ugh! I don’t understand any of this!)"
    mc sad "(*Sigh* Okay... he was heading in the direction of the exit closest to the store at least...so maybe he wasn’t lying about that?)"
    mc neutral "(I can’t think of much he could possibly pull there... )"

    label Leave_Him_1_Conclude:

    menu:
        mc "Maybe I'll-"
        "Go with him.":
            jump Go_With_Hen
        "Leave while I still can.":
            jump Leave_Him_2

    label Leave_Him_2:

    mc judge "(Nevermind, I shouldn't take the risk. I should just get out of here.)"
    show Hen thoughtful with poof
    z "I'd only taken a step back when Hen's eyes hone in on my movement."
    z "He inhales deeply."
    h smile "Oh my!"
    mc shock "...?!"
    h "I spill my heart out, tell you everything you need to know-"
    h "Only asking for a mere few bags of candy in exchange for my poor, broken, custom, engraved, {i}$5000.00{/i} phone."
    z "With each adjective, his voice grows louder until a few curious people glance our way."
    h "How cruel and unjust!"
    z "The number of glances keep increasing. A few curious whispers about us seem to be starting up as well."
    mc "(This isn't good-)"
    mc startled "Okay!-"
    mc "Okay, I'll go with you! Just stop that."
    h neutral "Okay."
    z "His voice suddenly drops back down to normal volume as if the whole scene he caused was forgotten."
    h "Let's go then."
    hide Hen with dissolve

    jump Leave_Him_2_Conclude

    label Go_With_Hen:

    mc judge "(I can’t really tell if I can trust this guy or not... but I do owe him a bit. Plus, I can always leave if things get weird.)"
    mc neutral "(It’s been a while, but I still know this area well enough.)"
    mc eyesclosed "Sure then... I guess?"
    mc sad "...But like I said, I don’t have much money."
    h neutral "Sure, sure."
    hide Hen with dissolve
    z "His distant tone makes it unclear if he was really listening to me as he begins moving once more."
    z "I hesitantly follow, walking a few steps behind him."

    label Go_Quietly:
    label Leave_Him_2_Conclude:
    stop music fadeout 3.0
    mc judge "(I... really hope I won’t regret this... ) "
    z "As we silently walk towards the venue exit, I am left quite alone to theorize on just what could possibly await me."
    z "None of my guesses are particularly reassuring. "

    show bg streets 1 with fade

    z "We exit the venue, he looks around for just a moment, then continues to lead the way to the store."
    mc neutral "(Well it doesn’t seem like he’s going to talk to {i}me{/i}... )"
    mc "Maybe I should talk to him."

    menu:
        mc "I could ask about that collab he mentioned earlier."
        "Ask him about it.":
            $ Ask_Collab = True
            mc "Hey, about that collab you mentioned-"
            show Hen with dissolve
            h "Hmm?"
            mc "What did that mean by a 'possible new collab'? What collab?"
            h smile "Oh, that. The collab between you and me, where you pay for candy and I get candy."
            h "See, a collaborative effort."
            hide Hen with dissolve
            z "He once again continues onward without even waiting for my response."
            mc judge "He's clearly not going to give me a proper answer... "
        "Leave it be.":
            mc sad "(Probably best to just keep my mouth shut for now... )"

    mc "(He’s walking in the right direction at least.)"

    show bg store with fade
    play music "<loop 0.00>Music/Store_Theme.mp3" fadein 5.0 volume 0.25
    if Question_Hen == False:
        mc shock "(Why are we at the store?)"
    else:
        mc shock "(This is definitely the store... )"
    z "Before I can even contemplate what would happen next, Hen has already wandered off, swiftly vanishing into one of the more distant aisles."
    mc "Okay then... –"
    z "I slowly follow after him."
    z "Turning the corner, I spot him already crouched in front of a shelf of different gummies."
    if Question_Hen == False and Ask_Collab == True:
        mc judge "...Is he seriously making me pay for his candy???"
    elif Question_Hen == False and Ask_Collab == False:
        mc judge "(What's he even doing here?)"
    else:
        mc judge "(I guess we’re really doing this now... )"
    z "He looks up at me as I approach... "
    z "...And immediately extends a selection of packages in my direction, an expectant look on his face."
    show Hen smile with dissolve
    h "Hold these."
    z "I soon find my arms entirely occupied by a large pile of candy."
    mc "...."
    mc "(What am I? Your shopping cart?)"
    z "With his hands now freed up, he seems to stare at the candy selection seriously for a few moments-"
    z "Apparently torn between a pack of multicolored frog gummies and what appears to be a foreign brand of whale gummies."
    h thoughtful "Hmmm... What do you think? Blue whales or Tree frogs?"
    mc shock "(This is probably the most serious I’ve seen him look so far... )"

    menu:
        mc ""
        "(Pick one from what he said)":
            jump One_Of_Two
        "Why not both?":
            jump Why_Not_Both
        "Does it matter which one you choose?":
            jump Does_It_Matter

    label One_Of_Two:
    mc neutral "Uhm..."
    z "I attempt to discreetly glance over at the shelf where he grabbed the bags only to internally grimace at the prices."
    mc judge "(I guess the tree frogs are cheaper… but ugh… my poor wallet.)"
    mc neutral "Tree frogs… I guess?"
    mc sad "(There go my pathetic savings… goodbye…)"
    play music "Music/Comedy.mp3" loop fadein 3.0 volume 0.6

    h neutral "Hmm, not a bad choice."
    mc shock "(...!)"
    z "He nods approvingly."
    h thoughtful "The multi coloured frogs are almost perfect in size and thickness for to get that satisfying gummy chew. The variety in flavours also helps to ensure that you don't get bored, but if you ask me, the citrus flavours over the other fruit ones are superior in this brand. "
    h neutral "A very balanced selection, yes."
    mc judge "(Oooookay then… Mr. Candy encyclopedia…)"
    z "He continues to state his approval, I continue to pretend I didn’t just choose the cheaper option."
    z "For some reason he seems to buy it... or perhaps he’s simply distracted."
    z "I catch him looking at the whale gummies longingly."
    mc "(Geez…)"

    jump One_Of_Two_Conclude

    label Why_Not_Both:

    z "I briefly glance down at the already ridiculous pile of candy in my arms, wondering why he’s suddenly showing some restraint."
    play music "Music/Comedy.mp3" loop fadein 3.0 volume 0.6
    h shock "I can’t do that! Don’t you see I need to watch my health!"
    mc judge "U-uhm…"
    mc "(...T-this is him watching his health…?)"
    show Hen thoughtful with poof
    z "He contemplates the two bags as if it were bars of gold, weighing one in each hand."
    mc "(Like one bag of candy more or less changes anything here– this is already a disgusting amount of sugar--)"
    z "My thoughts are interrupted as I feel the weight in my own arms increase, an additional two bags placed into the pile I’m carrying."
    h neutral "You know, you’re right. I’ll just get both."
    mc "(….)"
    mc shock "(That was a quick change?!)"
    h eyesclosed "I couldn't bear to leave one behind..."
    h shock "What if at 3AM, I have a sudden craving for gummy whales? The chewy top and soft base make for such a perfect combination of texture and flavour but they lack the overall variety of multicoloured gummy frogs. The tang of citrus gummies are best to be had in the mornings afterall-"
    mc "({i}That's{/i} his concern!?)"
    mc "(Who even eats candy at 3AM if they're watching their health!?)"
    h eyeclosed "It'll be safer this way."
    mc judge "...."
    mc happy "G-great…"
    mc judge "(I have no idea what I’m supposed to say to this…)"
    z "And so I don’t, instead begin to count up the total cost of everything I’m carrying."

    jump Why_Not_Both_Conclude

    label Does_It_Matter:

    mc neutral "It’s... just candy... does it make a difference-..."
    play music "Music/Comedy.mp3" loop fadein 3.0 volume 0.6
    z "I am almost immediately cut off by an indignant gasp."
    h shocked "Of course it makes a difference! They’re two completely different flavors!"
    play sound "Audio/Candy_Shake.mp3"
    z "He shakes the packets lightly as though to emphasize his point."
    mc judge "They... are...?"
    mc "(What’s with him all of a sudden?)"
    h thoughtful "Multi coloured tree frogs are each flavored by a different fruit, the orange ones are the best if you ask me, it’s so rare to get a decent citrus fruit flavor these days, for that alone they could be considered a great contender, but that’s not all! You see-..."
    z "He goes on to tell me in immense detail about the superiority of multi-coloured tree frogs over other fruit themed gummies."
    mc "(What is this guy? Some sort of candy maniac? What’s with all this exposition??)"
    mc neutral "If they’re so great why don’t you just pick them?"
    mc sad "(I feel like my brain is melting... )"
    z "His eyes narrow more in judgment."
    h thoughtful "What do you know? You candy heathen!"
    h shocked "You see-! Gummy whales instead have a mild mellow-flavoured marshmallow base that allows the top gelatin to diffuse the sweetness despite them having less citric or acids flavours! If anything they're a better gummie experience despite not being all uniform. If anything-"
    z "It's hard to tell if he's taking a breath during his explanation."
    mc "(I’m learning way too much about gummies today...)"
    h thoughtful "So you see, they’re both completely different!"
    mc judge "I... see... "
    mc "(I don’t see anything... I just want to go home... )  "
    mc neutral "Maybe... tree... frogs?"
    mc judge "(Please don’t ask me why... Please don’t ask me why... )"

    label One_Of_Two_Conclude:

    z "He looks at me carefully for a moment..."
    show Hen neutral with poof
    z "...Then slowly gets up and places both into the pile in my arms."

    label Why_Not_Both_Conclude:

    mc neutral "(Let's see here-these would be $3, plus that is $11.50 and those $18.75...)"
    mc shock "(This is way too much!)"
    z "Something must show on my face because he points at the pile under the bag of gummie whales in my arms."
    h smile "I’ll pay for these ones, it’s fine."
    mc "G-great..."
    mc neutral "(What was even the point of making me listen to that speech if you’re just going to get both and pay for some anyways... )"
    mc sad "(*Sigh* ...I guess I can’t complain since I did break his phone...) "
    mc neutral "So... is that everything?"
    mc judge "(I should probably double check I actually have the money for even half of this... )"
    h thoughtful "Hmm..."
    z "He looks over the candy aisle once more."
    h neutral "Yes, that should do for now."
    mc neutral "(For now... ?)"
    z "He glances at me briefly as he passes me to head to the checkout desk. "
    h "Ah, for me to eat this afternoon that is."
    h smile "Don’t worry, you’ll be all debt-free once you've paid for these."
    hide Hen with dissolve
    z "He elaborates, as though in response to my thoughts."
    mc sad "...."
    mc shock "(...wait.)"
    z "I pause for a moment."
    mc startled "You’re planning to eat all of these at once?!"
    z "Somehow it was the least important piece of information revealed in this exchange that turned out to be the most shocking."
    show Hen neutral with dissolve
    z "Pausing, he looks back at me."
    h "Yeah? Why not?"
    z "He responds plainly as though this is completely normal."
    mc "You’re going to make yourself so sick-"
    h smile "It’ll be fine. This is pretty normal for me."
    mc "(This is normal to him???)"
    hide Hen with dissolve
    stop music fadeout 5.0
    show Store_Blurred with dissolve
    z "Before I can ask any more questions, he once again turns to head to the cashier, I quickly move to catch up with him, soon placing the absurd amount of candy onto the counter."
    show Hen with dissolve
    z "The woman at the cash register raises an eyebrow as Hen quickly picks up a few of the packets he’d said he would be paying for."
    h smile "She’s paying for all but these ones."
    z "He gestures towards me loosely as I begin to pull out my wallet."
    z "The woman glances from me to Hen, her gaze lingering on him for a good few moments before she begins to scan items."

    $ Kim_Hen_April_Meet = True

    z "Hen simply continues to smile as though nothing is strange here."
    k "That’ll be $11.35, Would you like a bag?"
    z "Returning my attention to the cash register, I find the woman giving me a patient smile."
    mc neutral "Ah... y-yes please."
    z "Remembering what I was doing I resume digging out the cash from my wallet."
    h neutral "So-... "
    z "Hen begins to speak, but is immediately cut off."
    k "No, you’re not getting a discount on this."
    mc shock "(She knew what he was going to say?)"
    mc neutral "(Maybe they know each other... )"
    z "My questions are given no answers as the woman doesn’t even spare him a glance as she continues bagging the candy."
    z "Hen doesn’t seem to pursue the matter."
    z "Finally having freed the remainder of my coins from the recesses of my wallet, I hand the woman the money."
    k "Thank you!"
    z "She counts the change, then gives me another smile as she hands me the bag before turning to Hen."
    z "I stand by the counter as I wait for him to complete his purchase, which appears to be a quick affair, without any further dialogue exchanged."
    h "Okay, let’s go."
    hide Hen with dissolve
    z "Hen gives me a short expectant glance, before beginning to head outside."
    k "Have a nice day!"
    mc happy "Thanks!"
    stop music fadeout 3.0
    z "Tearing my gaze from the cashier, I slowly begin to follow Hen outside."

    hide bg store
    show bg streets 1 dim
    with fade

    show Hen with dissolve
    z "Stopping as I find him standing next to the entrance, I hold out the bag of candy."
    show Hen Big with poof
    z "He takes it from me, placing his pile of gummies inside."
    hide Hen Big
    show Hen neutral
    with dissolve
    mc neutral "So what now?"
    h "Hm?"
    mc "Well you said that this would be enough to make up for the phone, right?"
    h "Mhmmm."
    z "He continues to rummage through the bag of candy."
    mc shock "But you said your phone cost like $5000 right?…And then you said something about a collab?"
    mc sad "I... guess I’m just a bit confused."
    mc neutral "(I kind of assumed he’d had something more elaborate in mind.)"
    z "He just shrugs at that."
    mc shock "So this is all then?....I’m off the hook just like that?"
    h "Pretty much."
    mc "(Well that was easy?)"
    mc "I-..."
    h smile "Well I should get going now."
    mc "Ah-... oh- okay then."
    mc "(I guess I shouldn’t argue with him for letting me off so lightly.)"
    h "See ya!"
    hide Hen with dissolve
    z "He raises a hand in a farewell gesture, then turns to leave without so much as a second glance."
    mc "B-bye!"
    z "And so, I am all of a sudden left standing alone in the streets."
    mc neutral "(Well that was an unexpected adventure... )"
    mc judge "(What a weirdo.)"
    mc happy "(But, I guess he wasn't as bad as I thought.)"
    mc neutral "(*Sigh* What to do now... )"
    z "I look up at the slowly darkening sky."
    mc "(It looks like it’s going to rain... maybe I should go home while it’s still dry out.)"
    mc sad "(But...)"
    #[Show blurry image of the Faine scene or smth?]
    mc neutral "(...I wonder if that was really Faine back at the job fair.)"
    z "Even with all that had just unfolded, the earlier encounter had never quite slipped my mind."
    z "Looking back, I really could no longer say for sure if it wasn’t just a complete stranger, let alone why I had felt so compelled to drop everything and run after him."

    $ Day_1_Guy_Choice = "Hen"

    menu:
        mc "(But somehow...)"
        "I just can’t seem to let go of this... (Go back to look for Faine)":
            jump Return_Faine
        "Nevermind... (Go home)":
            mc neutral "Forget it, I should just get home, it looks like it's going to rain soon anyways."
            jump Go_Home_Early

    label Return_Faine:

    z "With that in mind, I begin making my way back towards the Job Fair."
    z "The walk wasn’t too far, as the store was just down the street from the venue, but I still ended up getting caught in the rain... "

    scene bg job fair rain
    $weather_stuff("rainy", 5, 1, "Thursday", 15)
    with fadehold

    mc "(If Faine’s not here, I should head straight home.)"
    mc sad "(Don’t want to get into trouble for being out late... )"
    z "Looking around, the hall is fairly empty at this point, so it’s easy to see across the expanse of the space, but unfortunately... "
    mc neutral "(Hm... no sign of him...)"
    mc "(Maybe I should ask one of the booth staff if they saw anyone matching his description?)"
    mc judge "(Besides the blue hair I don’t exactly remember many details though... )"
    mc neutral "(I’ll... just look around a bit more for now just in case I missed something.)"

    show bg job fair rain with fadehold

    mc judge "(Well it doesn’t seem like he’s here anymore.)"
    z "After circling the auditorium hall three times, asking multiple staff around the hall and booths, and even a few straggler attendees, it’s the only conclusion I can reach at this point."
    mc "(If it was even him to begin with... )"
    mc eyesclosed "(*Sigh*)"
    mc sad "(I should have just gone home... )"
    mc "(At this point I’m not even sure why I’m looking... )"
    mc eyesclosed "(Even if it was him and I did somehow find him, what then? What do I even want from him? He probably wouldn’t even remember me.)"
    mc sad "(And even if he does, it’s not like I have the time to be friends with him again... )"
    mc "(I barely have time for myself at this point... )"
    mc judge "This is so stupid..."
    z "Just as I’m beginning to turn to head home however, a nearby display catches my eye."
    show mini_cg_4 with Dissolve(1.5)
    mc shock "(....)"
    mc "(Wait...)"
    mc "(...This is-)"
    z "Without realizing it, I’ve already begun walking towards the booth in question."
    mc neutral "Gildstein community college student photography exhibit... ?"
    z "Across one full wall of the auditorium there are just over a dozen or so pictures lined up in a row, displaying the name of the respective student photographer just beneath it."
    z "It’s almost easy to mistake how small the classes here actually are with each picture blown up and taking up a lot more space than a normal photograph."
    mc shock "(I... remember this... )"
    mc "(Back when I was considering where to study, my parents took me to see one of these... )"
    z  "-Though I did end up going somewhere better, so I haven’t seen this in years."
    mc "(I can’t believe they’re still running these.)"
    mc happy "How nostalgic."
    mc sad "(I was so focussed on my job search earlier, that I must have overlooked it.)"
    mc neutral "(....)"
    z "I quickly pull out my phone to check the time."
    mc sad "(I’m already late, so taking a little peek around can’t hurt, right?)"
    mc happy "Maybe I’ll stay just a bit longer~ "

    show Fair_Blurred_2
    hide mini_cg_4
    with fadehold
    play music "<loop 0.00>Music/Home_Mellow.mp3" fadein 6.0 volume 0.7

    mc neutral "Oh, not bad, not bad at all..."
    z "It’s a lot easier now to slowly navigate from one image to the next now with the lack of crowds."
    z "There’s time to check each name carefully before taking a look at their work."
    mc happy "This one’s pretty good too..."
    z "On the far side of the wall there was a sign that said the exhibits overall theme was “Corners of Daily Life”."
    z "But the theme doesn’t seem too strict since there’s actually a variety of photo subjects here."
    z "Even then, each picture has its own charm, with edges of talent and novice mistakes scattered inbetween."
    mc neutral "(Let’s see here...)"
    mc "And this one’s by... Ernest Pickle... ?"
    z "I crouch slightly to squint at the name, making sure I read it correctly."
    z "The strip of paper still reads as 'Ernest Pickle'."
    mc judge "(I feel bad for judging a name, but what kind of name is that?)"
    mc neutral "(Could it be an online handle, maybe?)"
    mc happy "(Whatever, let’s see what this Ernest Pickle can do-)"
    mc shock "-Woah... "
    show mini_cg_2 with Dissolve(3)
    z "The picture staring back at me is an incredibly simple one and one that’s very on-theme - what with it being exactly the theme itself - depicting a cracked corner of a room."
    z "Little motes of dust and debris are the only other visible details in the photo. But somehow... "
    mc happy "(Aha, a little on the nose there.)"
    mc shock "(But that use of lighting is so interesting... )"
    mc neutral "(Among the pictures displayed, this one has the most unique lighting of the bunch.)"
    mc "(Whether that’s a good or bad thing though-)"
    mc judge "(Either way, this person has potential, I’m kind of jealous...)"
    hide mini_cg_2 with dissolve
    z "I take out my phone and snap a picture for reference."
    mc sad "(*Sigh* This makes me miss being a student... )"
    mc eyesclosed "(Things were so much easier back then.)"
    mc sad "(Everyone had the same goal and drive that it was easy to forget a passion for photography work isn’t the norm.)"
    mc "I guess we all have to grow up at some point."
    mc neutral "(Hopefully these students enjoy it while they can.)"
    z "I look down at my phone to check the time once more."
    hide Fair_Blurred_2 with dissolve
    mc shock "(Crap…it’s already 6:30PM-...)"
    mc judge "(If mom's still there, she's not going to be happy...)"
    mc neutral "(Well if I hurry up now I can still make it before dark at least.)"
    mc neutral "(Maybe if I run...)"
    z "And so I begin making my way to the building exit, and from there out onto the rainy streets."
    stop music fadeout 2.0
    $ Day_1_Guy_Return = "Faine"

    jump Go_Home_Late

    label Find_Faine:
    scene bg streets 1
    with fade

    z "Barely evading a few more startled passers-by, I made my way towards the place where I’d last spotted him, occasionally catching a glimpse of blue hair."
    z "I ended up finding myself just outside of the venue exit."
    mc startled "Ha…Ha…How is he so slippery!?"

    play sound "Audio/MC_Run.mp3"
    z "Despite the fact I had been running he seemed to have already vanished in the direction of the park."

    scene bg park
    with fade
    stop sound fadeout 1.0
    play ambient "Audio/Park.mp3" fadein 3.0 volume 0.40
    queue ambient "<loop 0.00>Audio/Park.mp3" fadein 3.0 volume 0.35
    mc sad "(Finally…)"
    mc shock "(....Wait, where did he go?)"
    z "The park appears to be empty."
    z "Or so it seems…"

    scene Faine_cg with fadehold:
       size (1920, 1080) crop (800, 0, 2100, 1181.25)
       linear 15 crop (800, 300, 2100, 1181.25)

    z "…Until I spot movement beneath a wooden picnic table, as what seems to be a head peeks out over the bench."

    scene Faine_cg:
        size (1920, 1080)
    with Dissolve(0.7)

    z "Our eyes meet for just a moment."
    mc "Faine...?"
    scene bg park with dissolve
    play sound "Audio/Wood_Impact.mp3" volume .5
    z "The boy quickly startled up, a short thump could be heard as the table wobbled slightly." with vpunch
    na "“Ouch–!! ….Ouch…ouch…."
    play sound "Audio/Debris.mp3" volume .7
    z "Clasping his head he seemed to flinch for a moment before attempting to clumsily scramble out from under the table."
    mc judge "(What was he even doing down there…)"
    stop sound fadeout 1.0
    mc "(Is he trying to hide?)"
    mc neutral "Are you okay?"

    menu:
        mc "(Maybe I should-)"
        "(Go to help him.)":
            jump Go_Help
        "(Give him some space.)":
            jump Give_Space

    label Give_Space:
    z "Despite the situation, I stay back and allow him time to get himself together."
    z "Maybe I imagined it, but I thought I heard a sigh of relief from him."
    mc shock "(Maybe he actually was trying to hide.)"
    mc sad "(I wonder why...)"
    mc neutral "...."
    z "It only takes him a minute longer to get up."
    z "But still, he says nothing."

    jump Give_Space_Conclude

    label Go_Help:
    z "Carefully, I make my way around the table - perhaps he needs help. But seemingly in response to my advance, the boy hastens his scramble to get to his feet."
    play sound "Audio/Debris.mp3" volume .7
    na "I'm fine-"
    mc shock "Uh..."
    stop sound fadeout 1.0
    z "There’s an unexpected level of coldness to his tone."
    mc sad "(Could I have made a mistake?)"
    mc neutral "(No…I'm sure it has to be him. He even reacted when I said his name!)"

    label Give_Space_Conclude:

    mc "You... {i}are{/i} Faine, right?"
    play music "<loop 0.00>Music/Meeting_v1b.mp3" fadein 3.0 volume 0.67
    show Faine mixed with Dissolve(0.5)
    f "That's me."
    f "So?"
    z "His hands and knees covered in dirt, he now stood upright, eyeing me with an uncharacteristically wary look on his face."
    mc shock "(Well that's…direct…)"
    mc "I-..."
    mc sad "..."
    mc "(I really should have thought of something to say before talking to him.)"
    mc "(Maybe he just doesn't know who I am after all these years.)"
    mc neutral "Uh...do you remember me?"
    z "Faine seems to tense up further at my question and for a moment it looks like he’ll answer me."
    f anxious "...."
    z "But instead, he continues to avoid my gaze as he fiddles nervously with the camera hanging from his neck."
    mc judge "(Well, this isn’t awkward at all.)"
    mc neutral "It’s me, [protag_name]. You know, that person you met at photography camp that one summer?"
    mc "We spent the week paired up?"
    z "Not even a flicker of emotion or recognition appears with my words."
    show Faine unhappy with poof
    f "…What do you want?"
    mc shock "...."
    mc sad "(Actually...)"
    mc "(What do I even want?)"
    mc "(I scrambled through a crowd for him... so...)"

    menu:
        mc "(...What now?)"
        "(Laugh it off and make something up.)":
            jump Make_Something_Up
        "(Be honest, you don't know what you want.)":
            jump Honesty_Faine

    label Make_Something_Up:

    mc happy "Haha...well uhh..."
    mc "It's... a silly story, you see!"
    mc judge "(What do I say, what to say?)"
    show Faine Small with dissolve
    z "Before I can think about it further, I notice that Faine has begun to shift a few steps away from me."
    z "His eyes grow even colder and his hold on his camera tightens."
    mc shock "(Wait-...Why's he acting like that?)"
    mc "(Did I upset him somehow?)"
    mc startled "(Quick- think of something to lighten the mood!)"
    mc happy "Well I...I just...-"
    mc "Wanted to ask you... Where you got your shirt!"
    mc "(Yeah... yeah, that't it... exactly what I wanted to ask... absolutely...)"
    show Faine Small mixed with poof
    f "...."
    z "Something small seems to soften in his expression."
    f "I don't know. Someone gave it to me."
    mc happy "O-oh, is that so..."
    z "Instead of words, Faine gives nothing but a small nod in reponse this time."
    mc neutral "...."
    mc judge "(Well this got even more awkward...)"
    mc "(Better think of something else to keep this conversation going.)"
    mc neutral "I-"
    show Faine unhappy with poof
    mc thunk "(....)"
    show Faine mixed with poof
    mc sad "(Why am I even keeping this conversation going?)"
    mc thunk "(Now that I think about it, I'm not actually sure why I felt compelled to run after him like I did...)"
    show Faine anxious with poof
    mc sad "(Did his words from back then really mean so much to me?)"
    z "Before I realize it, I had been quiet for much longer than I thought. His shuffling catches my attention."
    show Faine neutral with poof
    z "I look up to see eyes strikingly similar to someone from a long time ago."
    f "If that's all-"
    f "I'm late for work. Bye."
    hide Faine Tiny with dissolve
    z "Without even waiting for a response, he moves past me to leave."
    mc shock "W-wait!"
    show Faine with dissolve
    z "I quickly call out to him, and, despite everything, Faine stops and turns towards me once more."
    mc "...."
    mc "(He said he was late for work so I probably shouldn't keep him too long.)"

    menu:
        mc ""
        "(Push him for his contacts.)":
            jump Make_Something_Up_Next_1
        "(Wish him well and let him leave.)":
            jump Make_Something_Up_Next_2

    label Make_Something_Up_Next_1:

    mc shock "C-Can I have your contact info so we can stay in touch, maybe?"
    z "The words comes out all at once, a bit more forceful in my rush, and a response comes just as quick-"
    f mixed "No."
    mc sad "Oh-"
    mc "O-okay...sorry..."
    mc "You can go ahead."
    hide Faine with dissolve
    z "This time, there is barely any acknowledgement as Faine leaves."

    jump Make_Something_Up_Next

    label Make_Something_Up_Next_2:

    mc sad "Uh- nevermind, it's nothing."
    mc neutral "Good luck at work."
    f "...."
    f anxious "...Thank you."
    f neutral "Bye."
    hide Faine with dissolve
    z "Once more, he makes his way over to the park entrance without waiting for a response."

    jump Make_Something_Up_Next

    label Make_Something_Up_Next:

    mc "...."
    mc eyesclosed "(I feel so stupid.)"
    mc sad "(I barely have time for myself these days, let alone time to try and make friends.)"
    mc "(And yet, here I am doing-...doing who knows what in that conversation.)"
    mc "(What was I even trying to achieve there?)"
    mc eyesclosed "*Sigh*"
    mc "What a terrible day so far..."

    jump Make_Something_Up_Conclusion

    label Honesty_Faine:

    mc "Honestly I'm not really sure. I just saw you… and then-"
    mc neutral "...Well I just kind of ran after you without thinking I guess."
    z "He seems to study me carefully as I speak."
    mc "I've been out of town for a while and I don't really know anyone here anymore, so I guess I thought it might be nice to talk to you again?"
    mc sad "But…it's okay if you don't want to."
    show Faine neutral with poof
    z "Though his posture remains tense, something seems to give in his expression as he looks away once more, his mouth remaining closed in a thin line for a moment."
    f anxious "It's not that I don't want to..."
    f "I just..."
    z "He looked down at his camera nervously for a moment."
    show Faine eyesclosed with poof
    mc neutral "(Maybe he's feeling shy?)"
    mc "If you don't want to talk right now, how about giving me your social media? Or…I guess I could give you mine."
    show Faine neutral with poof
    z "He looks back up at me carefully."
    mc shock "You don't need to message me or anything, I probably won't really have the time to talk much anyway."
    mc "It'd just be nice to not lose contact again, you know?"
    mc sad "Well…I guess this probably seems kind of weird to you since you don't remember and all..."
    mc "(What am I even saying at this point...)"
    mc "(I barely have time for myself, let alone for reviving forgotten friendships.)"
    z "He looks at me thoughtfully."
    show Faine thoughtful with poof
    z "Before beginning to search his pockets and clumsily digging out a rather beat up looking smartphone."
    mc shock "(...!)"
    z "He takes a minute to search for something..."
    z "Finally, he points the screen at me, a profile page open."
    show Faine Big with poof
    f anxious "Here. I don't know how to do this."
    mc "Ah- just a sec."
    z "Digging out my own phone, I note his profile name."
    mc neutral "Faine...6...3...50...1..."
    mc neutral "Right, got it, thanks."
    hide Faine Big
    show Faine anxious
    with poof
    z "He hesitantly pockets the phone again, continuing to awkwardly stare at me for a bit before finally muttering."
    f neutral "...I’m late for work."
    z "Faine raises a single stiff hand in what can only be assumed to be a greeting gesture of sorts."
    f "Okay."
    f "Bye."
    hide Faine with Dissolve(0.3)
    stop music fadeout 3.0
    play ambient "<loop 0.00>Audio/Park.mp3" fadein 3.0 volume 0.40
    z "And without another word he scrambles off toward the other park entrance."
    mc shock "...."
    mc neutral "What was that?"
    mc eyesclosed "(*Sigh* Well, whatever that was, it certainly wasn’t the Faine I remember.)"
    mc neutral "(I guess I have his account now though, might as well take a peek.)"
    mc "Let’s see what we have here."
    mc "Faine..63..501." #play typing sound here
    #show screen of Faine's socials here
    mc "(Maybe his profile will tell me why he’s being so weird.)"
    mc "Five followers and one post. How does he only have one post?"
    mc judge "It’s even from three years ago."
    mc "And it has 75,000 likes."
    mc shock "...."
    mc startled "It has 75,000 likes?!"
    mc "(Wait, what is this?! How?!)"
    z "The numbers are still there no matter how much I look at the post."
    mc neutral "(This makes no sense. He might have just reposted something, right?)"
    mc judge "(This makes even less sense than before.)"
    mc "*Stomach Gurgles*"

    label Make_Something_Up_Conclusion:

    mc eyesclosed "(Well, it’s late, I can think about this later.)"
    #put away Faine's profile
    mc neutral "(I should probably get home before it starts raining anyways...)"
    mc sad "(Mom isn’t going to be happy if I’m late either...)"
    stop music fadeout 3.0
    stop ambient fadeout 3.0

    $ Day_1_Guy_Choice = "Faine"

    menu:
        mc "I should..."
        "I forgot the phone guy! Go back and look for him.":
            stop ambient fadeout 3.0
            jump Return_Hen
        "It's been a long day. Let's go home.":
            z "Leaving the park, I begin to make my way back."
            stop ambient fadeout 3.0
            jump Go_Home_Early

    label Return_Hen:
    play ambient "<loop 0.00>Audio/Park.mp3" fadein 6.0 volume 0.40
    z "I’d only taken a few steps in the direction of home ... "
    z " ... When all of a sudden, a thought flashed back into my mind."
    mc " .... "
    mc shock " .... "
    mc "(Wait ... )"
    mc startled "(Ah!! Crap I totally forgot about him!!)"
    #show mini_cg_broken_phone with dissolve
    mc "(I totally ditched him back there, what was I even thinking?!)"
    mc judge "(And I was just about to go home too... hah...)"
    mc sad "(If I go back for him now he’ll probably be super pissed... if he’s even still there... )"
    mc "(But then again if I just leave that’s also not right.)"
    mc judge "(Nevermind how awkward it would be if I ran into him again after this... )"
    mc shock "(Agh- what do I do?!)"
    mc neutral "(Okay, okay…calm down and think... )"
    mc "(It’s not that late, so the job fair is still open for a bit... I think.)"
    mc "(He might still be there if he’s attending one of the evening events... maybe???)"
    mc "(I...should probably at least try to do the right thing... shouldn’t I... )"
    mc shock "...."
    stop ambient fadeout 5
    z "Just as I am contemplating this, I feel a cold drop of rain hit my cheek."
    z "Soon, a flurry of heavy raindrops follow."
    z "Looking up, I find that the sky above has taken on a foreboding shade of gray."
    mc eyesclosed "UGH!...Fine!!"
    play ambient "<loop 0.00>Audio/Rain2.mp3" fadein 5.0 volume 0.30
    mc judge "(I SO don’t have the time for this... )"
    mc "(...But I also don’t think I can just go home after remembering this... )"
    play sound "Audio/MC_Run.mp3"
    z "And so without wasting another moment, I begin running through the rain, back towards the building where the job fair is being held."



    scene bg streets 1 dim
    $weather_stuff("rainy", 5, 1, "Thursday", 15)
    with fade

    pause 0.7
    stop sound fadeout 2.0
    stop ambient fadeout 3.0

    label mell_cheat:

    scene bg job fair rain
    with fade

    mc shock "Hah...hah..."
    z "I pause to catch my breath."
    mc judge "(I should really stop neglecting my workout routine... )"
    mc "(Ugh... and my clothes feel all damp from the rain... )"
    mc eyesclosed "(Okay...focus, focus.)"
    z "Having caught my breath, I pull myself up, scanning the space ahead for the man with the broken phone."
    z "The venue is fairly empty at this point, so I can easily see across the expanse of the hall... however..."
    mc neutral "(Hm... I can’t see him here... )"
    mc "(Could he have left already?)"
    mc "(Well he was kind of flashy looking... I guess I could... )"
    z "Catching sight of a nearby unoccupied booth, I wander over. "
    mc shock "Excuse me!"
    z "I catch a woman’s attention."
    show morgana:
        size(765,1120)
        xalign 0.45
        yalign 1
    with dissolve
    c "How can I help you?"
    mc neutral "Well uh... I was looking for someone and I was wondering if maybe you saw him?"

    menu:
        mc "He-"
        "Was tall, now that I think about it and kind of handsome-":
            jump Flattering_Choice
        "(Describe hair, eyes, and clothes.)":
            jump Uncertain_Choice
        "(Describe situation in which you encountered him since it drew attention)":
            jump Describe_Choice

    label Flattering_Choice:

    mc "He was tall, now that I think about it and kind of handsome-"
    h "-Both in his looks and personality! The whole package of handsome if you were to ask me!"
    play music "Music/Comedy.mp3" loop fadein 3.0 volume 0.6
    z "A loud voice from behind interrupts me."
    hide morgana with dissolve
    z "I turn around, only to come face-to-face with the exact person I was looking for."
    show Hen with dissolve
    h smug "Of course, if you did ask me. I would entirely agree."
    mc shock "(Wait- Where did he come from?!)"
    z "The woman's eyes dart between me and the tall man, unsure of what to make of the situation."
    z "But he continues onwards without paying her much attention."
    h "Now imagine-"
    h eyesclosed "There I was, minding my own business, when the next thing I know, poof, my phone is gone."
    h "Its life tragically ended by someone else's hands-"
    h smug "Or maybe, someone's foot is more accurate in this situation."
    mc judge "(....)"
    h neutral "My very new and very custom-"
    h smug "Engraved-"
    h smile "$5000.00 phone."
    h "And the offender just runs off!"

    if Apologize_to_Hen == False:
        h "Without so much as even an apology to spare, might I add."
        h smug "Really, where {i}are{/i} your manners?"

    jump Flattering_Choice_Conclude

    label Describe_Choice:

    mc neutral "...."
    mc judge "(How do I even begin to explain this mess to someone?)"
    mc thunk "Well, earlier today, I accidentally crashed into someone here and knocked him down?"
    mc sad "I think I might have ended up breaking his phone too..."
    mc thunk "You wouldn't have happen to have seen the guy, would you...?"
    z "The woman gives me a withering look, clearly unimpressed about what I'd just told her"
    z "She then opens her mouth as if to say something, but before she can do that, we're both interupted by a voice behind me."
    h "It's seems like the lady does know of her crime!"
    play music "Music/Comedy.mp3" loop fadein 3.0 volume 0.6
    mc shock "(...?!)"
    hide morgana with dissolve
    z "I turn towards the voice, only to find the exact person I was looking for."
    show Hen with dissolve
    h smile "And here I thought my dashing, handsome self, had been discarded like a used tissue once she disappeared."
    mc judge "(...Does he need to describe himself as “dashing” and “handsome”?)"
    h "I'm so proud of you for coming back to take responsibility-"
    h smug "For smashing someone’s custom, engraved, $5000.00 phone beyond repair and then running away-"

    if Apologize_to_Hen == False:
        h "But yet, she couldn't spare a second to even apologize earlier."
        h smug "A person has to wonder if you're truly sorry about it."

    jump Describe_Choice_Conclude

    label Uncertain_Choice:
    mc "He had brown-black hair."
    mc "Uh, maybe brown-black eyes..."
    mc sad "A brown-black jacket..."
    mc "...."
    z "The look the woman is giving me doesn't seem to be inspiring any confidence."
    mc "I think he was also... uh... tall-?"
    z "Suddenly, I am interrupted as a voice speaks up behind me."
    na "He was tall! Dashing! Handsome! I could fall in love...actually I already have."
    play music "Music/Comedy.mp3" loop fadein 3.0 volume 0.6
    mc shock "(...?!)"
    hide morgana with dissolve
    z "I turn... to find the exact man I was looking for, staring down at me."
    show Hen with dissolve
    mc " (Agh! Where did he come from?!)"
    show Hen wink with poof
    pause 0.17
    show Hen neutral with poof
    mc judge "(...Did he just wink at me?)"
    z "I open my mouth to speak but he cuts me off."
    h smug "Unfortunately I’ve committed a terrible sin!"
    show Hen eyesclosed with poof
    z "He goes on, raising his hands and speaking as though reciting a dramatic tale."
    h smug "Yes..how could a girl like me, who smashes someone’s custom, engraved, $5000.00 phone beyond repair and then runs away-"
    h "-Ever be considered worthy of someone so perfect?"
    h "I should probably beg for his forgiveness."
    h "Hope that he might have a {i}bit{/i} more integrity than I do."

    label Flattering_Choice_Conclude:
    label Describe_Choice_Conclude:

    z "His tone might be mistaken for playful joking under different circumstances, however the pointed stare he directs at me tells an entirely different story."
    mc shock "(....)"
    show Hen smile with poof
    z "He smiles at me, it is absolutely not reassuring."
    stop music fadeout 5.0
    z "For a moment, an awkward silence falls."
    mc judge "Uhm... "
    show Hen Small at hidari2
    show morgana:
        size(765,1120)
        xalign 0.80
        yalign 1
    with dissolve
    z "I awkwardly make eye contact with the woman who I’d asked for help."
    z "She continues to smile at me, but is clearly uncomfortable."
    mc "(Ugh…this is so awkward... )"
    mc "(We should probably continue this in privacy... )"
    mc happy "W-well... it... looks like I found him... T-thanks...! "
    hide Hen
    hide morgana
    with dissolve
    z "Without another word, I quickly turn to leave, soon hearing his footsteps follow behind me."
    show Hen neutral with dissolve
    z "A glance back has him smiling and shrugging at me, as though what just happened wasn’t entirely his doing."
    hide Hen with dissolve
    mc judge "(...He’s kind of starting to irritate me.)"
    mc eyesclosed "(*Sigh*)"
    mc neutral "(What should I do?)"

    z "A safe distance away from prying ears, I come to a stop, as does he."
    mc "(It doesn’t look like he’s going to help me out and make the first move here... so maybe I should.)"
    mc "You realize I was there looking for you, right?"
    show Hen neutral with dissolve
    z "I turn to face him, he looks back at me innocently."
    h "So?"
    mc judge "...."
    mc shock "So I really don’t think you had to go and make a scene like that! It was totally uncalled for!"
    h thoughtful "Huuh... "
    z "He raises an eyebrow at me skeptically, clearly unimpressed with that response."
    mc "(....)"
    mc sad "(Okay I probably did deserve this a bit since I did run and abandon him like that... but still!)"
    mc eyesclosed "*Sigh*"
    mc neutral "(This is clearly getting me nowhere... )"
    mc "Okay fine."
    mc sad "I came back to apologize about your phone, so I’m sorry about that…a-and running off afterwards."
    mc neutral "I’d like to make it up to you somehow."
    h "Hmmm... ?"
    h smile "And how are you going to do that?"
    mc "(How am I going to do that?)"
    mc "(I hadn’t actually thought that far ahead...)"
    mc "(Maybe I can tell him I’ll pay him for it when I get more money... )"
    mc "I'll pay-"
    show Hen neutral with poof
    mc sad "(Wait... wait–)"
    mc shock "(Didn’t he also say something earlier about it being worth $5000??)"
    mc "(That can’t possibly be true though... can it?!)"
    z "I look up to find him smiling at me."
    h smug "Ah, I did mention that it was worth $5000.00, didn’t I? Brand new, customized, engraved... I almost forgot to mention all that work I probably lost by not being able to access my email."
    h smile "I’d love to know what you have in mind."
    mc "I... Uhm... "
    mc judge "...."

    menu:
        mc ""
        "(You don't know how to make it up to him, but you want to try)":
            mc sad "I...I don't actually know what I can do-"
            mc thunk "But I want to try."
            h smug "Hmmmmmm."
            z "He makes a show of tapping his chin, humming all the while."
            h "Luckily for you, I am not only handsome, but also quite merciful."
            jump Want_To_Try
        "(Tell him you'll pay him when you have money (You don't know you will.)":
            jump Pay_Him
        "(Tell him to get lost, it wasn't your fault.)":
            jump Get_Lost

    label Get_Lost:

    mc startled "You know what- forget it, it wasn't my fault at all."
    mc sad "It was all and accident and what you're doing is unfair."
    h "...."
    h smug "Well, well, well..."
    h "It seems like someone wasn't being honest ealier about wanting to apologize afterall."
    h smile "What{i}ever{/i} shall we do about it?"
    z "As if it was possible, his smile seems to stretch even wider."
    mc judge "...."
    mc "(The more he smiles, the more uneasy I get.)"
    h "But luckily for you, I am not only handsome, but also quite merciful."

    jump Get_Lost_Conclude

    label Pay_Him:

    mc neutral "(I don’t know if this is possible but... ) "
    show Hen neutral with poof
    mc shock "I can pay you!"
    mc neutral "It’ll just have to wait until I have money."
    h smile "Not interested."
    mc "What if I find someone to fix your phone for you?"
    h neutral "No thanks."
    mc sad "I... don’t have anything else to offer."
    h "Hm- what a pity."
    h smile "But luckily for you, I am not only handsome, but also quite merciful."

    label Want_To_Try:
    label Get_Lost_Conclude:

    h "I’m sure we’ll think of something."
    show Hen neutral with poof
    mc neutral "....?"
    h "Well, looks like I’ve got to get going now."
    h "I’ll be in touch."
    mc shock "Wait- but how will you contact me?"
    show Hen wink with poof
    pause 0.17
    show Hen neutral with poof
    h "I have my methods."
    mc judge "(He... has his methods...?)"
    mc "(What does that mean?)"
    z "Before I can ask, he’s already turned to leave, giving me a small wave."
    hide Hen with dissolve
    mc shock "(Okay then... I guess... ???)"
    z "Thoroughly confused, I stand around for a good few moments, watching him wander off, until-"
    mc startled "(Ah crap! what am I doing just standing here?!)"
    z "I quickly wrestle my phone from my pocket to check the time."
    mc "(I knew it... it’s already 6:30PM... I’m totally going to be late now!)"
    z "I quickly begin making my way towards the nearest exit."
    mc sad "(I hope dad won’t be too upset... )"
    mc neutral "(I should probably move faster-)"
    z "And so, I did, beginning my journey home."

    $ Day_1_Guy_Return = "Hen"

    jump Go_Home_Late

    label Go_Home_Early:

    play ambient "<loop 0.00>Audio/Rain2.mp3" fadein 5.0 volume 0.30
    show bg streets 1 dim
    $weather_stuff("rainy", 5, 1, "Thursday", 15)
    with fade

    z "The walk back home is a relatively short and uneventful one."
    z "Soon enough I am standing at the entrance of my parents’ house, quietly contemplating how to delicately explain my complete lack of success at the job fair to them."
    mc judge "(I guess no matter what, they’ll find out sooner or later.)"
    mc "(Might as well just bite the bullet and get it over with...)"
    z "Turning the key, I push down the door handle."

    show bg hallway with fade
    stop ambient fadeout 2.0
    play sound "Audio/Door_Open.mp3"
    mc "(Here goes... )"
    stop sound
    play ambient "Audio/Kitchen_Noise.mp3" loop fadein 5.0 volume 0.9
    z "Walking in, I quietly close the door behind me, taking off my shoes before proceeding to walk down the now rather dim hall."
    z "I hear the muffled sound of someone eating in the kitchen. "
    mc neutral "(That's odd, mom and dad are usually quite chatty at dinner.)"
    z "Quietly opening the door, I peek into the room to see only my father eating at the table."
    stop ambient fadeout 1
    mc happy "I’m back..."
    z "He looks over at me curiously."
    d "Welcome home! Your mom got called into her shift early so it's just you and me tonight."
    mc neutral "Oh, okay..."
    d "So, how’d it go? Find anything?"
    mc judge "(Just a whole lot of trouble.)"
    mc "(Better not tell him about [Day_1_Guy_Choice]...)"
    mc sad "Not really... "
    mc "I guess I'm not what they were looking for."
    d "I see..."
    mc sad "...."
    z "He seems to pause as he looks at me for a moment, seeming to consider his next words carefully, before finally relenting with a short sigh."
    d "That’s okay sweetie, let's get you fed and we can talk about this tomorrow morning when your mother is back from her shift."
    d "But you should also dry off first, looks like you got caught in the rain a bit."
    mc shock "A-alright... I will."
    stop ambient fadeout 2.0
    mc eyesclosed "(Well that went better than I thought for now.)"

    show bg mc_room with fadehold
    play music "<loop 0.00>Music/Home_Mellow.mp3" fadein 6.0 volume 0.7

    jump Go_Home_Early_Conclude

    label Go_Home_Late:

    play ambient "Audio/Rain2.mp3" loop fadein 5.0 volume 0.30
    show bg streets 1 night with fade

    z "The walk back home is a relatively short and uneventful one."
    z "Soon enough I am standing at the entrance of my parents’ house, quietly contemplating how to delicately explain my complete lack of success at the job fair to them."
    mc judge "(I guess no matter what, they’ll find out sooner or later.)"
    mc "(Might as well just bite the bullet and get it over with...)"
    z "Turning the key, I push down the door handle."

    show bg hallway with fade
    stop ambient fadeout 2.0

    mc "(Here goes... )"
    play ambient "<loop 0.00>Audio/TV.mp3" fadein 5.0 volume 0.9
    z "Walking in, I quietly close the door behind me, taking off my shoes before proceeding to walk down the now rather dim hall."
    z "I hear the muffled sound of the tv coming from the living room. "
    mc neutral "(I guess they must have already eaten...)"
    z "Quietly opening the door, I peek into the room to see my father sitting on the sofa watching what appears to be the news."
    mc happy "I’m back..."
    z "He looks over at me curiously."
    d "You’re back late..."
    mc sad "Yeah... sorry about that, I got held up a bit."
    mc judge "(Better not tell him about [Day_1_Guy_Choice]...)"
    d "Seems it, you’re soaked through."
    d "So, how’d it go? Find anything?"
    mc sad "Not really... "
    mc "I not what they were looking for, I guess."
    d "I see..."
    mc sad "...."
    z "He seems to pause as he looks at me for a moment, seeming to consider his next words carefully, before finally relenting with a short sigh."
    d "That’s okay, we can talk about this tomorrow morning when your mother is back from her shift."
    d "Get some rest for now, you look tired."
    d "And make sure to take a warm shower or dry off completely before you catch a cold."
    mc shock "A-alright... I will."
    z "I pull the door shut slowly."
    mc neutral "Good night!"
    d "Night, sweetie!"
    stop ambient fadeout 2.0
    mc eyesclosed "(Well that went better than I thought for now.)"

    show bg mc_room with fadehold
    play music "<loop 0.00>Music/Home_Mellow.mp3" fadein 6.0 volume 0.7

    z "I make my way to my room, dumping my jacket and bag next to the door, before collapsing onto my bed."

    label Go_Home_Early_Conclude:

    z "After a quick change and some dinner, I excused myself to get some rest."
    z "I make my way to my room, plugging in my phone, before collapsing onto my bed."

    mc no_coat sad "Haah..."

    show blink with Dissolve(0.15)
    show blackscreen with Dissolve(0.15)
    pause 0.5
    hide blackscreen with Dissolve(0.15)
    hide blink with Dissolve(0.15)
    pause 0.5

    mc sad "(I wonder what mom and dad will say tomorrow...)"
    mc "(I told them I’d try my best to get a job, but look at me-)"
    mc "(All I got out of today was a load of mean comments and some guy asking me to work for exposure.)"
    mc eyesclosed "(*Sigh* Maybe that one booth guy was right... maybe my portfolio is just bland or something... )"
    mc "(Ugh- so depressing...)"
    mc startled "(Come on, think happy thoughts!)"
    mc shock "(I’ll-... I’ll just have to... work on making my portfolio even better! So they’ll have no choice but to hire me next time!)"
    mc judge "(Ughh-... who am I kidding, that’s what I tried to tell myself before this too and today was even more of a disaster than usual... )"
    mc eyesclosed "What a dayyyyy... "

    if Day_1_Guy_Choice == "Hen":
        mc neutral "(I can't believe I forgot to watch where I was going.)"
        mc "(Letting myself run into the King of Gummies like that.)"
        mc judge "(Not to mention I ended up trashing the guy’s phone.)"
        #[show faded phone cg]
        mc "(Was... me buying him some candy really enough to make up for that?)"
        mc neutral "(He... seemed so okay with it... though it was kind of difficult to tell if he was being serious-)"
        mc "(Not that it makes a difference now I guess, I’ll probably never see him again.)"
    elif Day_1_Guy_Choice == "Faine":
        mc thunk "(I still can't believe that was Faine, he acted acted so different compared to what I remember.)"
        mc shock "(Not to mention the hair.)"
        mc "(And the camera...)"
        mc "I thought he barely used phone cameras before, but the one he had was actually a good one-"

    if Day_1_Guy_Return == "Faine":
        mc "(....Speaking of which-)"
        mc sad "(*Sigh*)"
        mc "(I should definitely let the whole Faine thing go...)"
        mc neutral "(I wasted all that time going back to look for him, but still I found nothing...)"
        mc "(Was that even him in the first place? He looked so different, and who stays here their whole life?)"
        mc sad "(My brain hurts just thinking about it.)"
    elif Day_1_Guy_Return == "Hen":
        mc neutral "(....Speaking of which-)"
        mc judge "(Mr.Dashing and Handsome - More like Mr.Self Flattery.)"
        mc "(Sure, I broke his phone and left, but he could had just discussed it normally with me.)"
        mc sad "(I don't want to even know what his {i}methods{/i} are.)"
        mc judge "(Let's just hope I never see him again.)"
    elif Day_1_Guy_Return == "No One":
        mc sad "Ugh, there are more important things to focus on, like finding a paying photography job."

    mc eyesclosed "(*Yawn*)"
    mc neutral "(Maybe... I could ask mom and dad if they know anything.)"
    mc "(I don’t think they will... but it doesn’t hurt to ask.)"

    show blink with Dissolve(0.03)
    show blackscreen with Dissolve(0.03)
    pause 0.1
    hide blackscreen with Dissolve(0.03)
    hide blink with dissolve

    mc sad "(I’ll... try to finish some... uploads... tomorrow too...)"

    show blink with Dissolve(0.03)
    show blackscreen with Dissolve(0.03)
    pause 0.1
    hide blackscreen with Dissolve(0.03)
    hide blink with dissolve

    mc eyesclosed "(...Maybe send out some more job ap... plica... tions...)"

    show blink with Dissolve(0.3)
    show blackscreen with Dissolve(0.3)
    pause 1

    "CHAPTER 1 END - MAY DAY (*DEMO END*)"

#[GO AFTER FAINE + being in trouble with Hen v1 + 2 ]
#[MC thinking about how different Faine was, contemplating the broken phone scenario and hen (depending on if she went back for him) etc.]

#[MC falls asleep unintentionally]

#[Fade to black]

    return
