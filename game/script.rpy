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

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image morgana = "recruiter_one.png"
image barty = "recruiter_two.png"
image migel = "recruiter_three.png"
image hale = "recruiter_four.png"
image blink = "blink.png"
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
default Kim_Hen_April_Meet = False

define z = Character (None, ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define f = Character("Faine", image="Faine", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define h = Character("[Hen_Name]", image="Hen", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define mc = Character("[protag_name]", image="MC", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define na = Character("???", ctc ="ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define p = Character("[protag_name]", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define b1 = Character("Recruiter 1", image = "morgana", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define ba = Character("Recruiter 5", image = "barty", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define b3 = Character("Recruiter 12", image = "migel", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define c = Character("Woman", image = "morgana", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define o = Character("[Otto_Name]", image="Otto", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define l = Character("[Lexi_Name]", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")
define k = Character("[Kim_Name]", ctc = "ctc_arrow", ctc_timepause = "ctc_arrow", ctc_position = "fixed")

image mini_cg_1 = "memory.png"
image Hen_cg = "Hen_cg.jpg"

define flash = Fade(0.1, 0.0, 0.5, color="#666")
define fadehold = Fade(0.7, 0.3, 0.7)

# The game starts here.
label start:
    $renpy.show_layer_at(blur_bg,layer= "master", camera = True)

## Start inputting date for widgets here (weather, date, etc)
    $weather_stuff("sunny", 12, 30, "Thursday", 15)
    show screen widgets

################################################################################

    scene bg mc room
    with fade
    z "(Insert intro text here)"
    z "(Mc leaves the room through her window after having checked social media, done her makeup and got dressed)"
    z "(EXIT)"
    hide bg mc room
    show bg scenery2
    mc neutral "Out in the streets."
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
        "cheat":
            jump mell_cheat

    label choice_thatplace:
    hide bg scenery2
    hide screen widgets

    ##### New day/time example
    $weather_stuff("rainy", 12, 31, "Friday", 20)
    show screen widgets

    show bg thatplace
    with fade
    mc judge "(MC thoughts blablabla, this is the place I met faine that day.)"
    show Faine
    mc "(Totally forgot wow so emotional, this is a good photo op)"
    show Faine at hidari
    "You spot someone who resembles your old friend...but is it really him?"
    f anxious "Who are you?"
    mc shock "You don't remember me?"
    f unhappy "No..."
    show Faine at migi
    show Hen at hidari
    mc "If that's how you want to be."
    hide Hen
    show Faine at mannaka with poof
    hide Faine
    show Hen at mannaka with poof
    f "It's just how I am."
    show Faine Small at hidari2 with poof
    show Hen Small at migi2 with poof
    mc sad "You don't have to be so harsh about it."
    f anxious "Oh."
    hide Hen
    f thoughtful "Sorry about that. I didn't mean to be."
    "Faine takes a small step towards you."
    show Faine Big at mannaka with poof
    f "I am big now."
    hide Faine Big
    show Faine
    with poof
    z "It's how it is."
    hide Faine
    show Hen Big with poof
    "To be continued..."
    hide bg thatplace
    hide Hen
    jump choice_done

    label choice_store:
    hide bg scenery2
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


    scene bg black

    z "I'll leave Faine in your capable hands, Alright? - Alright!"
    play music "<loop 0.00>Prologue.mp3" fadein 5.0
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
    with fade
    na "Miss [protag_name]...?"
    na "Miss [protag_name]...?"

    show bg_job
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
    play music "<loop 0.00>Job_Fair.mp3" fadein 5.0 volume 0.75
    show morgana:
        size(765,1120)
        xalign 0.45
        yalign 1
    with dissolve
    b1 "Are you alright?"
    mc "(Ah…stupid, why am I daydreaming at a time like this?!)"
    menu:
        mc "I-"
        "Apologize, ask her to repeat herself.":
            jump choice_apologize_repeat
        "Pretend you were listening.":
            jump choice_pretend_listen
        "Ask her who she is.":
            jump choice_who_is_she

    label choice_apologize_repeat:
    mc neutral "Sorry, could you please repeat yourself?"
    b1 "As I was saying, we currently can’t afford to invest in anyone without at least 3 years of relevant work experience."
    z "The woman vaguely flips through my portfolio. It’s clear based on how quickly she turns each page that she’s barely taking anything in."
    b1 "Now, that isn’t to say your work isn’t good; you might even be a good fit for our company once you get some experience."
    b1 "But unfortunately, 3 years of personal social media work isn’t quite our standard for “experience”."
    mc sad "...I understand."

    hide morgana
    hide bg_job
    show bg_job
    show barty:
        size(765,1120)
        xalign 0.45
        yalign 5
    with fadehold

    ba "You know-"
    ba "I’d be quite happy to give you a chance despite your bland, boring portfolio."
    ba "But you need to want it! To have a passion for it!"
    ba "Our biggest clients all want tasteful, cultured, body shots of themselves and we are a discreet studio dedicated to ART."
    mc judge "...."
    ba "You’re just not convincing me right now with all this social media nonsense…"
    ba "We just can’t take on someone who’s done nothing but play around online over the last few years."
    ba "If you’re that good, you should start figuring out how to get some solid marketable skills or add some culture to your portfolio!"
    mc "(No thanks...)"

    hide bg_job
    hide barty
    show bg_job
    show migel:
        size (770,1365)
        xalign 0.45
        yalign -0.05
    with fadehold

    b3 "Wow, your portfolio is excellent!"
    mc shock "(Wait, what?!)"
    b3 "Mhm, Mhm…yes…I think we could definitely offer you a place on our internship program."
    mc "...Really-!?"
    b3 "We can’t pay you of course, but you’ll get a whole lot of exposure and work experience!"
    mc judge "(.......Should have known.)"
    b3 "So how about it!? I’m sure we can make it worth your while!"
    mc "(*Sigh*)"
    stop music fadeout 3.0
    mc sad "I'll give it some thought...thanks."

    hide migel
    hide bg_job
    jump all_rejections

    label all_rejections:

    scene bg_job
    with fade

    mc eyesclosed "(No, no, no, no. Nothing but rejections.)"
    mc sad "(I was told applying at job fairs was supposed to be easier but that’s not true at all. At least email rejections aren’t as brutal.)"
    mc "(This was such a waste of time ...)"
    mc judge "(... I should just put as much distance between myself and Mr. “cultured photos” as possible.)"
    mc sad "Hahhh ..."
    mc judge"({i}That sounds cool, I’m sure you’ll be great.{/i})"
    mc "(Great my butt.)"
    mc sad "(I wonder what that boy would think if he saw me today?)"
    mc "(There’s probably not much point in giving myself a headache over it.)"
    mc neutral "(But now that I think about it, even though I remember what he said, I can’t remember his name…)"
    mc "(It started with an ‘F’, right? ... Fang?)"
    mc "(No ... was it Frank?)"
    mc "(Maybe it was more of a Finn ... ?)"
    show Faine Tiny with dissolve
    mc shock "(Wait.)"
    mc "(Isn’t that-)"
    mc "...Faine."
    hide Faine Tiny with poof
    mc "H-hey–!"
    z "The quiet exclamation is lost in the noisy crowd, as is the sudden flicker of an all too familiar face in the distance."
    z "Without realizing, I take a few steps forward."
    mc "(It can't be...)"
    mc "(Faine?!)"
    mc "(Why was he here? Where has he been? Did he look different !? -)"
    z "A million questions surface, but before there’s time to think about it, I’m already running after him."
    z "Only in the rush, I’d forgotten to look where I was going ..."
    show Hen Giant shocked with poof
    mc "Wai- ... Ngh-" with hpunch
    hide Hen Giant with poof
    h "Hey- ah- ... Watch it!"

    scene Hen_cg with fadehold:
       size (1920, 1080) crop (1460, 1062, 2050, 1116)
       linear 3 crop (1460, 200, 2050, 1116)
    z "The man I collided with utters a panicked curse as his things clatter to the ground."

    scene Hen_cg:
        size (1920, 1080)
    with Dissolve(0.7)

    z "The people around us quickly back away as if to avoid the site of the collision."
    mc "(There’s no time to worry about this, I have to get up and-)"

    scene bg_job with dissolve

    z "*CRACK*"
    mc " .... "
    h " .... "
    mc shock "(Oh crap ...)"
    z "There, {w=0.5} beneath my shoe,{w=0.5} lies a very shiny, very new-looking {w=0.5}...and a {i}very{/i} broken-beyond-repair smartphone."

    menu:
        mc "What should I do!?"
        "Keep running.":
            mc "(Ugh- I can’t deal with this now, I need to find Faine!)"
            z "Tearing my glance away from  the cracked phone and the hopefully still disoriented stranger, I turn and run, quickly resuming my pursuit."
            mc "(It’s probably nothing too bad….right?)"
            jump Find_Faine
        "Apologize, then run after Faine.":
            mc "(Ugh- I can’t deal with this now, I need to find Faine!)"
            z "Looking up from the cracked phone, I catch the stranger’s gaze and hesitate for a moment."
            mc "(It’s no good, I don’t have time for this..)"
            mc "I-I’m sorry! I have to go ..."
            mc "I’ll come back later!"
            z "Without looking for a response, I quickly turn to run after Faine once again."
            #$ Apologize_to_Hen = True
            jump Find_Faine
        "Stand around awkwardly.":
            jump Stay_Hen_1
        "Stop and apologize to the stanger, attempt to make amends.":
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
    mc "(Should I help him?)"
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
    mc shock "I’m so sorry! Let me help you."
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
        "Tell him you don’t know what to do.":
            jump Stay_Hen_Conclusion_part2
        "Ask him how much the phone was worth. See if you have money to fix it.":
            jump Stay_Hen_Conclusion_part2
        "It was an accident!!":
            jump Stay_Hen_Conclusion_part2

    label Stay_Hen_Conclusion_part2:

    mc sad "H-how much would it cost to buy a new one... "
    mc "(I definitely can’t afford it but... it’s better to know what I’m working with here at least... )"
    z "Or so I thought."
    h smile "$5000.00"
    mc shock "($5000?!?!)"
    mc "(What sort of phone costs $5000???)"
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

    h thoughtful "Hmmm let me see..."
    z "He makes a show of thinking for a moment."
    h "How about-"
    z "He begins, but all of a sudden we are interrupted by a shout."
    na "Hey Hen! Over here!"
    show Hen neutral with poof
    z "A voice calls out, and the stranger before me reflexively turns to look in the direction the voice is coming from."
    show Hen Tiny at mannaka with dissolve
    z "Two new people emerge from the crowd, a woman clutching a name brand purse and a boy waving his hand in the air to get our attention."
    show Otto Tiny at migi2 with dissolve
    mc shock "(Are they friends of his?)"
    l "You get lost or something? We’ve been looking all over the campus for you."
    o "You didn’t answer your phone either."

    $ Hen_Name = "Hen(?)"

    h eyesclosed "Sorry, sorry, my phone got smashed so I didn’t get anything."
    show Hen neutral with poof
    z "He holds up his cracked and dead phone in emphasis."
    o "Damn, that sucks... "
    h smile "Yup."
    z "Everyone waits a beat to see if Hen will explain what happened, but he didn’t seem to elaborate any further."
    z "He simply shrugs."
    o "...."
    l "...."
    mc judge "...."
    z "Only then, does the girl seem to notice me."
    l "Oh, who’s this? Another fan?"
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
    z "It must have been enough because they nod understandingly."
    mc shock "(Wait, what collab? What does that mean?)"
    l "Gotcha, we’ll head back to the gym then. Join us after when you’re done."
    mc "(Done with what? They're clearly not even trying to include me in this conversation-)"
    z "No one seems to provide further context for anything though and the two walk off to the other end of the auditorium."
    hide Otto Tiny with dissolve
    hide Hen Tiny
    show Hen neutral
    with dissolve
    z "Hen turns back towards me as if nothing just happened."
    h smile "Alright, let’s go, I have the perfect idea."
    hide Hen with dissolve
    z "Without so much as waiting for further confirmation, he'd already begun to move, clearly expecting me to follow."

    #CHOICE MENU Here

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
    mc sad "(*Sigh* Okay... he was heading in the direction of the exit closest to the store at least...so maybe he wasn’t lying about that? I can’t think of much he could possibly pull there... )"

    menu:
        mc "Maybe I'll-"
        "Go with him.":
            jump Go_With_Hen
        "Leave while I still can.":
            jump Dont_Go_With_Hen

    label Go_With_Hen:

    mc judge "(I can’t really tell if I can trust this guy or not... but I do owe him a bit. Plus, I can always leave if things get weird.)"
    mc neutral "(It’s been a while, but I still know this area well enough.)"
    mc eyesclosed "Sure then... I guess?"
    mc sad "...But like I said, I don’t have much money."
    h neutral "Sure, sure."
    hide Hen with dissolve
    z "His distant tone makes it unclear if he was really listening to me as he begins moving once more."
    z "I hesitantly follow, walking a few steps behind him."
    mc judge "(I... really hope I won’t regret this... ) "
    z "As we silently walk towards the venue exit, I am left quite alone to theorize on just what could possibly await me."
    z "None of my guesses are particularly reassuring. "

    show bg streets 1 with fade

    z "We exit the venue, he looks around for just a moment, then continues to lead the way to the store."
    mc neutral "(Well it doesn’t seem like he’s going to talk to me... )"

    menu:
        mc "Maybe I should ask about that collab he mentioned earlier."
        "Ask him about it.":
            mc "Hey, about that collab you mentioned-"
            show Hen with dissolve
            h "Hmm?"
            mc "What did that mean by a 'possible new collab'? What collab?"
            h smile "Oh that. The collab of me getting candy and you paying."
            h "A collaborative effort."
            hide Hen with dissolve
            z "He once again continues onward without even waiting for my response."
            mc judge "He's clearly not going to give me a proper answer... "
        "Leave it be.":
            mc sad "(Probably best to just keep my mouth shut for now... )"

    mc "(He’s walking in the right direction at least.)"

    label mell_cheat:
    show bg_store with fade

    mc shock "(This is the store... )"
    z "Before I can even contemplate what would happen next, Hen has already wandered off, swiftly vanishing into one of the more distant aisles."
    mc "Okay then... –"
    z "I slowly follow after him."
    z "Turning the corner, I spot him already crouched in front of a shelf of different gummies."
    mc judge "(I guess we’re really doing this now... )"
    z "He looks up at me as I approach... "
    z "...And immediately extends a selection of packages in my direction, an expectant look on his face."
    show Hen smile with dissolve
    h "Hold these."
    z "I soon find my arms entirely occupied by a large pile of candy."
    mc "...."
    mc "(What am I? Your shopping cart?)"
    z "With his hands now freed up, he seems to stare at the candy selection seriously for a few moments, apparently torn between a pack of multicolored frog gummies and what appears to be a foreign brand of whale gummies."
    h thoughtful "Hmmm... What do you think? Blue whales or Tree frogs?"
    mc shock "(This is probably the most serious I’ve seen him look so far... )"

    #menu:
    #    mc "What were the options again?"
    #    "Why not both?":
    #    "Does it matter which one you choose?":

    mc neutral "It’s... just candy... does it make a difference-..."
    z "I am almost immediately cut off by an indignant gasp."
    h shocked "Of course it makes a difference! They’re two completely different flavors!"
    z "He shakes the packets lightly as though to emphasize his point."
    mc judge "They... are...?"
    mc "(What’s with him all of a sudden?)"
    h thoughtful "Multi coloured tree frogs are each flavored by a different fruit, the orange ones are the best if you ask me, it’s so rare to get a decent citrus fruit flavor these days, for that alone they could be considered a great contender, but that’s not all! You see-..."
    z "He goes on to tell me in immense detail about the superiority of multi-coloured tree frogs over other fruit themed gummies."
    mc "(What is this guy? Some sort of candy maniac? What’s with all this exposition??)"
    mc neutral "If they’re so great why don’t you just pick them?"
    mc sad "(I feel like my brain is melting... )"
    z "His eyes narrow more in judgment. I can almost feel them say “What do you know? You candy heathen!"
    h shock "You don’t understand! Gummy whales instead are have a mild mellow-flavoured base that allows the top gummies to not taste as sweet despite them having less citric or acids flavours! If anything they're a better experience despite not being all gummie-"
    z "It's hard to tell if he's taking a breath during his explanation."
    mc "(I’m learning way too much about gummies today...)"
    h thoughtful "So you see, they’re both completely different!"
    mc judge "I... see... "
    mc "(I don’t see anything... I just want to go home... )  "
    mc neutral "Maybe... tree... frogs?"
    mc judge "(Please don’t ask me why... Please don’t ask me why... )"
    z "He looks at me carefully for a moment..."
    show Hen neutral with poof
    z "...Then slowly gets up and places both into the pile in my arms."
    mc neutral "(Let's see here-these would be $3, plus that is $11.50 and those $18.75...)"
    mc shock "(This is way too much!)"
    z "Something must show on my face because he points at the bags of tree frogs in my arms."
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
    mc "You’re planning to eat all of these at once?!"
    z "Somehow it was the least important piece of information revealed in this exchange that turned out to be the most shocking."
    show Hen neutral with dissolve
    z "Pausing, he looks back at me."
    h "Yeah? Why not?"
    z "He responds plainly as though this is completely normal."
    mc "You’re going to make yourself so sick-"
    h smile "It’ll be fine. This is pretty normal for me."
    mc "(This is normal to him???)"
    hide Hen with dissolve
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
    mc smile "Thanks!"
    z "Tearing my gaze from the cashier, I slowly begin to follow Hen outside."

    hide bg_store
    show bg streets 1
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

    menu:
        mc "(But somehow...)"
        "I just can’t seem to let go of this... (Go back to look for Faine)":
            jump Return_Faine
        "Nevermind... (Go home)":
            jump Home_Early

    label Find_Faine:
    scene bg mc room
    with fade

    z "Barely evading a few more startled passers-by, I made my way towards the place where I’d last spotted him, occasionally catching a glimpse of blue hair."
    z "I ended up finding myself at the venue exit."
    mc shock "Ha…Ha…How is he so slippery!?"
    z "Despite the fact I had been running he seemed to have already vanished in the direction of the park."

    scene bg park
    with fade

    mc sad "(Finally…)"
    play music "<loop 0.00>Meeting_v1b.mp3" fadein 3.0 volume 0.65
    mc shock "(....Wait, where did he go?)"
    z "The park appears to be empty."
    z "Or so it seems…"
    z "…Until I spot movement beneath a wooden picnic table, as what seems to be a head peeks out over the bench."
    z "Our eyes meet for just a moment."
    mc "Faine...?"
    z "The boy quickly startled up, a short thump could be heard as the table wobbled slightly." with vpunch
    na "“Ouch–!! ….Ouch…ouch…."
    z "Clasping his head he seemed to flinch for a moment before attempting to clumsily scramble out from under the table."
    mc judge "(What was he even doing down there…)"
    mc "(Is he trying to hide?)"
    mc neutral "Are you okay?"
    z "Carefully, I make my way around the table - perhaps he needs help. But seemingly in response to my advance, the boy hastens his scramble to get to his feet."
    na "I'm fine-"
    mc shock "Uh..."
    z "There’s an unexpected level of coldness to his tone."
    mc sad "(Could I have made a mistake?)"
    mc neutral "(No…I'm sure it has to be him. He even reacted when I said his name!)"
    mc "You are…Faine, right?"
    show Faine mixed with Dissolve(0.5)
    f "That's me."
    f "So?"
    z "His hands and knees covered in dirt, he now stood upright, eyeing me with an uncharacteristically wary look on his face."
    mc shock "(Well that's…direct…)"
    mc "I-..."
    mc sad "..."
    mc "(I really should have thought of something to say before talking to him.)"
    mc "(He probably doesn’t even know who I am…)"
    mc neutral "Uh...do you remember me?"
    z "Faine seems to tense up further at my question and for a moment it looks like he’ll answer me."
    f anxious "...."
    z "But instead, he continues to avoid my gaze as he fiddles nervously with the camera hanging from his neck."
    mc judge "(Well, this isn’t awkward at all.)"
    mc neutral "It’s me, [protag_name]. You know, that person you met at photography camp that one summer?"
    mc "We spent the week paired up?"
    z "Not even a flicker of emotion or recognition appears with my words."
    mc "(He clearly doesn’t remember me much.)"
    show Faine unhappy with poof
    f "…What do you want?"
    mc shock "...."
    mc sad "(Actually… What do I even want? I scrambled through a crowd for him…so what now?)"
    mc "Honestly I'm not really sure. I just saw you… and then…-"
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
    z "Faine raises a single stiff hand in what can only be assumed to be a greeting gesture."
    f "Okay."
    f "Bye."
    hide Faine with Dissolve(0.3)
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
    mc "It has 75,000 likes?!"
    mc "(Wait, what is this?! How?!)"
    z "The numbers are still there no matter how much I look at the post."
    mc "(This makes no sense. He might have just reposted something, right?)"
    mc "(This makes even less sense than before.)"
    mc "*Stomach Gurgles*"
    mc eyesclosed "(It’s late though, I can think about this later.)"
    #put away Faine's profile
    mc neutral "(I should probably get home before it starts raining anyways...)"
    mc sad "(Mom isn’t going to be happy if I’m late either...)"
    stop music fadeout 3.0

    menu:
        mc "I should..."
        "I forgot the phone guy! Go back and look for him.":
            jump Return_Hen
        "It's been a long day. Let's go home.":
            z "Leaving the park, I begin to make my way back."
            jump Go_Home_Early

    label Return_Hen:
    z "I’d only taken a few steps in the direction of home ... "
    z " ... When all of a sudden, a thought flashed back into my mind."
    mc " .... "
    mc shock " .... "
    mc "(Wait ... )"
    mc "(Ah!! Crap I totally forgot about him!!)"
    #show mini_cg_broken_phone with dissolve
    mc "(I totally ditched him back there, what was I even thinking?!)"
    mc sad "(And I was just about to go home too... hah...)"
    mc "(If I go back for him now he’ll probably be super pissed... if he’s even still there... )"
    mc "(But then again if I just leave that’s also not right.)"
    mc judge "(Nevermind how awkward it would be if I ran into him again after this... )"
    mc shock "(Agh- what do I do?!)"
    mc neutral "(Okay, okay…calm down and think... )"
    mc "(It’s not that late, so the job fair is still open for a bit... I think.)"
    mc "(He might still be there if he’s attending one of the evening events... maybe???)"
    mc "(I...should probably at least try to do the right thing... shouldn’t I... )"
    mc shock "...."
    z "Just as I am contemplating this, I feel a cold drop of rain hit my cheek."
    z "Soon, a flurry of heavy raindrops follow."
    z "Looking up, I find that the sky above has taken on a foreboding shade of gray."
    mc eyesclosed "UGH!...Fine!!"
    mc judge "(I SO don’t have the time for this... )"
    mc "(...But I also don’t think I can just go home after remembering this... )"
    z "And so without wasting another moment, I begin running through the rain, back towards the building where the job fair is being held."

    scene bg_job
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
        "Had brown-black hair, brown-black eyes, brown-black jacket...":
            jump Uncertain_Choice
        "(Describe situation in which you encountered him since it drew attention)":
            jump Uncertain_Choice

    label Uncertain_Choice:
    mc "He had brown-black hair."
    mc "Uh, maybe brown-black eyes..."
    mc sad "A brown-black jacket..."
    mc "...."
    z "The look the woman is giving me doesn't seem to be inspiring any confidence."
    mc "I think he was also... uh... tall-?"
    z "Suddenly, I am interrupted as a voice speaks up behind me."
    na "He was tall! Dashing! Handsome! I could fall in love...actually I already have."
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
    z "His tone might be mistaken for playful joking under different circumstances, however the pointed stare he directs at me tells an entirely different story."
    mc shock "(....)"
    show Hen smile with poof
    z "He smiles at me, it is absolutely not reassuring."
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
    mc "(It doesn’t look like he’s going to help me out and make the first move here... )"

    #menu:
        #"You're feeling slightly petty, walk faster":
        #"Stop, tell him that was uncalled for, you were trying to find him after all.":
        #"Stop. Ask him what he wants.":
        #"Stop, tell him you'd like to make amends.":

    z "A safe distance away from prying ears, I come to a stop, as does he."
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
    mc "Okay fine, whatever."
    mc "I came back to apologize about your phone, so I’m sorry about that…a-and running off afterwards."
    mc "I’d like to make it up to you somehow."
    h "Hmmm... ?"
    h smile "And how are you going to do that?"
    mc "(How am I going to do that?)"
    mc "(I hadn’t actually thought that far ahead...)"
    mc "(Maybe I can tell him I’ll pay him for it when I get more money... )"
    mc "I'll pay-"
    show Hen neutral with poof
    mc "(Wait... wait–)"
    mc shock "(Didn’t he also say something earlier about it being worth $5000??)"
    mc "(That can’t possibly be true though... can it?!)"
    z "I look up to find him smiling at me."
    h smug "Ah, I did mention that it was worth $5000.00, didn’t I? Brand new, customized, engraved... I almost forgot to mention all that work I probably lost by not being able to access my email."
    h smile "I’d love to know what you have in mind."
    mc "I... Uhm... "
    mc judge "...."

    menu:
        "You don't know how to make it up to him, but you want to try":
            jump Want_To_Try
        "Tell him you'll pay him when you have money (You don't know you will).":
            jump Pay_Him
        "Tell him to get lost, it wasn't your fault":
            jump Get_Lost

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
    mc shock "(Ah crap! what am I doing just standing here?!)"
    z "I quickly wrestle my phone from my pocket to check the time."
    mc "(I knew it... it’s already 6:30PM... I’m totally going to be late now!)"
    z "I quickly begin making my way towards the nearest exit."
    mc sad "(I hope dad won’t be too upset... )"
    mc neutral "(I should probably move faster-)"
    z "And so, I did, beginning my journey home."


    return
