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

default protag_name = "April"

define f = Character("Faine", image="Faine")
define h = Character("Hen", image="MC")
define mc = Character("[protag_name]", image="MC")
define na = Character("???")
define p = Character("[protag_name]")
define b1 = Character("Recruiter 1")
define b2 = Character("Recruiter 5")
define b3 = Character("Recruiter 12")

image mini_cg_1 = "memory.png"

define flash = Fade(0.1, 0.0, 0.5, color="#666")

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
    show Faine at migi2
    mc "If that's how you want to be."
    show Faine at mannaka with poof
    f "It's just how I am."
    show Faine Small with poof
    mc sad "You don't have to be so harsh about it."
    f anxious "Oh."
    f thoughtful "Sorry about that. I didn't mean to be."
    "Faine takes a small step towards you."
    show Faine Big with poof
    f "I am big now."
    hide Faine Big
    show Faine
    with poof
    "To be continued..."
    hide bg thatplace
    hide Faine
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

    label mell_cheat:

    scene bg black

    "I'll leave Faine in your capable hands, Alright? --Alright. I gotta go or I'll lose the duck!"
    p "Wha- you can’t-..."
    p "And he’s already gone..."
    p "...-Figures."
    p "...We come all the way here and he abandons you to go on a literal wild goose chase...Hey Faine, you okay with this?"
    f "A duck chase."
    p "What?"
    f "I think it was a wild duck chase."
    p "A du-....That's so not the point here."
    f "What is the point then?"
    p "...Nevermind...-- You don't have a camera right? Are you just using your phone or something?"
    f "I’m okay without anything. I'll just watch you."
    "*FLASH*" with flash
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
    f "You’ll do amazing!"
    p "...."
    f "...."
    p "What if I said I wanted to be a T-rex?"
    f "...I heard they sell those blow up dinosaur costumes in the next town over?"
    p "Ah geeez…"
    hide mini_cg_1 with dissolve

    scene bg_job
    with fade
    na "Miss [protag_name]...?"
    na "Miss [protag_name]...?"
    mc shock "...Huh?"
    b1 "Are you alright?"
    mc "(Ah…stupid, why am I daydreaming at a time like this?!)"
    menu:
        mc "I-"
        "Apologize, ask him to repeat himself.":
            jump choice_apologize_repeat
        "Pretend you were listening.":
            jump choice_pretend_listen
        "Ask him who he is.":
            jump choice_who_is_he

    label choice_apologize_repeat:
    mc neutral "Sorry, could you please repeat yourself?"
    b1 "As I was saying, we currently can’t afford to invest in anyone without at least 3 years of relevant work experience."
    "The man vaguely flips through my portfolio, it’s clear based on how quickly he turns each page that he’s barely taking anything in."
    b1 "Now, that isn’t to say your work isn’t good; you might even be a good fit for our company once you get some experience."
    b1 "But unfortunately, 3 years of personal social media work isn’t quite our standard for “experience”."
    mc sad "...I understand."

    hide bg_job
    show bg_job
    with fade

    b2 "I’m not really a stickler for a set amount of work experience, and I’d be quite happy to give you a chance despite your bland portfolio."
    b2 "But you need to want it, to have a passion for it!"
    b2 "Our biggest clients all want tasteful, cultured, body shots of themselves and we are a discreet studio dedicated to ART."
    mc judge "...."
    b2 "You’re just not convincing me right now with all this social media nonsense…"
    b2 "We just can’t take on someone who’s done nothing but play around online over the last few years."
    b2 "If you’re that good, you should start figuring out how to get some solid marketable skills or add some culture to your portfolio."
    mc "(No thanks...)"

    hide bg_job
    show bg_job
    with fade

    b3 "Wow, your portfolio is excellent!"
    mc shock "(Wait, what?!)"
    b3 "Mhm, Mhm…yes…I think we could definitely offer you a place on our internship program."
    mc "...Really-!?"
    b3 "We can’t pay you of course, but you’ll get a whole lot of exposure and work experience!"
    mc judge "(.......Should have known.)"
    b3 "So how about it!? I’m sure we can make it worth your while!"
    mc "(*Sigh*)"
    mc sad "I'll give it some thought...thanks."

    hide bg mc room
    jump all_rejections

    label all_rejections:

    scene bg mc room
    with fade

    mc eyesclosed "(No, no, no, no. Nothing but rejections.)"
    mc sad "(I was told applying at job fairs was supposed to be easier but that’s not true at all. At least email rejections aren’t as brutal.)"
    mc "(This was such a waste of time…)"
    mc judge "(...I should just put as much distance between myself and Mr. “cultured photos” as possible for now.)"
    mc sad "Hahhh..."
    mc "(I wonder what that boy would think of me now...)"
    mc "(Would he still tell me that I can make it?)"
    mc "(There’s probably not much point in thinking about it.)"
    mc "(Now that I think about it, even though I remember what he said, I can’t remember his name…)"

    scene bg mc room
    with fade

    "Barely evading a few more startled passers-by, I made my way towards the place where I’d last spotted him, occasionally catching a glimpse of blue hair."
    "I ended up finding myself at the venue exit."
    mc shock "Ha…Ha…How is he so slippery!?"
    "Despite the fact I had been running he seemed to have already vanished in the direction of the park."

    scene bg park
    with fade

    mc sad "(Finally…)"
    mc shock "(....Wait, where did he go?)"
    "The park appears to be empty."
    "Or so it seems…"
    "…Until I spot movement beneath a wooden picnic table, as what seems to be a head peeks out over the bench."
    "Our eyes meet for just a moment."
    mc "Faine...?"
    "The boy quickly startled up, a short thump could be heard as the table wobbled slightly." with vpunch
    na "“Ouch–!! ….Ouch…ouch…."
    "Clasping his head he seemed to flinch for a moment before attempting to clumsily scramble out from under the table."
    mc judge "(What was he even doing down there…)"
    mc "(Is he trying to hide?)"
    mc neutral "Are you okay?"
    "Carefully, I make my way around the table - perhaps he needs help. But seemingly in response to my advance, the boy hastens his scramble to get to his feet."
    na "I'm fine-"
    mc shock "Uh..."
    "There’s an unexpected level of coldness to his tone."
    mc sad "(Could I have made a mistake?)"
    mc neutral "(No…I'm sure it has to be him. He even reacted when I said his name!)"
    mc "You are…Faine, right?"
    show Faine mixed with Dissolve(0.5)
    f "That's me."
    f "So?"
    "His hands and knees covered in dirt, he now stood upright, eyeing me with an uncharacteristically wary look on his face."
    mc shock "(Well that's…direct…)"
    mc "I-..."
    mc sad "..."
    mc "(I really should have thought of something to say before talking to him.)"
    mc "(He probably doesn’t even know who I am…)"
    mc neutral "Uh...do you remember me?"
    "Faine seems to tense up further at my question and for a moment it looks like he’ll answer me."
    f anxious "...."
    "But instead, he continues to avoid my gaze as he fiddles nervously with the camera hanging from his neck."
    mc judge "(Well, this isn’t awkward at all.)"
    mc neutral "It’s me, [protag_name]. You know, that person you met at photography camp that one summer?"
    mc "We spent the week paired up?"
    "Not even a flicker of emotion or recognition appears with my words."
    mc "(He clearly doesn’t remember me much.)"
    show Faine unhappy with poof
    f "…What do you want?"
    mc shock "...."
    mc sad "(Actually… What do I even want? I scrambled through a crowd for him…so what now?)"
    mc "Honestly I'm not really sure. I just saw you… and then…-"
    mc neutral "...Well I just kind of ran after you without thinking I guess."
    show Faine neutral with poof
    "He seems to study me carefully as I speak."
    mc "I've been out of town for a while and I don't really know anyone here anymore, so I guess I thought it might be nice to talk to you again?"
    mc sad "But…it's okay if you don't want to."
    "Though his posture remains tense, something seems to give in his expression as he looks away once more, his mouth remaining closed in a thin line for a moment."
    f anxious "It's not that I don't want to..."
    f "I just..."
    "He looked down at his camera nervously for a moment."
    show Faine eyesclosed with poof
    mc neutral "(Maybe he's feeling shy?)"
    mc "If you don't want to talk right now, how about giving me your social media? Or…I guess I could give you mine."
    show Faine neutral with poof
    "He looks back up at me carefully."
    mc shock "You don't need to message me or anything, I probably won't really have the time to talk much anyway."
    mc "It'd just be nice to not lose contact again, you know?"
    mc sad "Well…I guess this probably seems kind of weird to you since you don't remember and all..."
    mc "(What am I even saying at this point...)"
    mc "(I barely have time for myself, let alone for reviving forgotten friendships.)"
    "He looks at me thoughtfully."
    show Faine thoughtful with poof
    "Before beginning to search his pockets and clumsily digging out a rather beat up looking smartphone."
    mc shock "(...!)"
    "He takes a minute to search for something..."
    "Finally, he points the screen at me, a profile page open."
    f anxious "Here. I don't know how to do this."
    mc "Ah- just a sec."
    "Digging out my own phone, I note his profile name."
    mc neutral "Faine...6...3...50...1..."
    mc neutral "Right, got it, thanks."
    show Faine neutral with poof
    "He hesitantly pockets the phone again, continuing to awkwardly stare at me for a bit before finally muttering."
    f "...I’m late for work."
    "Faine raises a single stiff hand in what can only be assumed to be a greeting gesture."
    f "Okay."
    f "Bye."
    hide Faine with Dissolve(0.3)
    "And without another word he scrambles off toward the other park entrance."
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
    "The numbers are still there no matter how much I look at the post."
    mc "(This makes no sense. He might have just reposted something, right?)"
    mc "(This makes even less sense than before.)"
    mc "*Stomach Gurgles*"
    mc eyesclosed "(It’s late though, I can think about this later.)"
    #put away Faine's profile
    mc neutral "(I should probably get home before it starts raining anyways...)"
    mc sad "(Mom isn’t going to be happy if I’m late either...)"


    return
