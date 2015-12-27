#Super Waifu Wars Demo
#Coder: BQ -- Brandon Quan
#Guy Who's Randomly Putting Stuff In: SZ -- Seilai Zhao
#script.rpy

#Since we're not using git or dropbox, I'm going to put dates here to illustrate 
#what changed I've done to the source code so you can follow what I've done to the
#code more easier. Ctrl + F the date and you should be able to find what I've made
#changes to.

#Also added a few spacing comments to make stuff a bit more organized. :P Feel free to
#remove it if you think it's unnecessary.
#26/05/2015 -- Added blipping sound. Made the default in the configuration of text
#display speed to 50 character's per second.
#26/05/2015 -- BQ: added sound effects and music to scenes
#05/06/2015 -- BQ: added the rest of the script, but no assets to accompany
#18/06/2015 -- BQ: to Seilai - Ctrl + F "note to Seilai" for tasks you can work on
#18/06/2015 -- SZ: Finished, left the notes there if you want to see how it's been done. Otherwise, nothing much else edited.

#--------------------------DECLARATIONS--------------------------#

#------------------------------IMAGE-----------------------------#

# BACKGROUND IMAGES
image bg black = "blackbg.jpg"
image bg white = "whitebg.jpg"
image bg hubble = "hubble.jpg"
image bg space = "space.jpg"

image bg cockpit = "cockpit-blend8.png"
image bg cockpit2 = "cockpit-blend7.png"
image bg cockpit3 = "cockpit-blend6.png"
# 19/06/2015 -- BQ: changed the cockpit images into more up-to-date looking ones

image bg simroom = "simulator-room-001.png"
image bg hallway = "hall-way_001.jpg"
image bg engineroom = "engine-room-002.png"
image bg mediaroom = "media-room-005.png"
image bg airlock = "airlock-room-001.png"

image bg husbando_ext = "husbando-exterior-005.png"
image bg husbando_int = "husbando-interior-001.png"
image bg husbando_cryo = "cryosleep-room-001.png"
image bg husbando_cryo_close = "cryosleep-room(close_up)-001.png"

# CHARACTER IMAGES

# AI-Sempai
image ai = "ai_neutral.png"
image ai blush = "ai_blush.png"  # same as ai smile
image ai happy = "ai_happy.png"
image ai sad = "ai_sad.png"
image ai serious = "ai_serious.png"
image ai smile = "ai_smile.png"
image ai tearful = "ai_tearful.png"

image hs = "hs_neutral.png"
image hs confused = "hs_confused.png"
image hs halfeye = "hs_halfeye.png"
image hs sleep = "hs_sleep.png"

image gc = "gc_neutral.png"
image gc bored = "gc_bored.png"
image gc disoriented = "gc_disoriented.png"
image gc upset = "gc_upset.png"

image kq = "dinosaur.png"
# Default display:
#show ai at center:
#        yalign 0.0
#        zoom 0.4

#26/05/2015 -- Character Callback function here. This is where the blippy voice is defined.
#26/05/2015 -- BQ: Commented out this function, but keeping it here in case we want to use it later.
#-- Made a new "character", 'nn', to change the say function for narrator without having the whole nvl narrator going off.
#----------------------------Character Callback F'n------------------------------#
#init python:
#    def placeHolderVoice(event, interact=True, **kwargs):
#        if not interact:
#            return
        
#        if event == "show_done":
#            renpy.sound.play("beep.mp3", loop=True)
#        elif event == "slow_done":
#            renpy.sound.stop()


#26/05/2015 -- callbacks placed for chars.
#------------------------CHAR DECLARATIONS------------------------#
# MAIN CHARACTERS
define mc = Character('Hiroo Onoda', color="#c8ffc8")
       # Working Name: MC-kun
define ai = Character('AI-Sempai', color="#c8c8ff", image="ai")
       # Working Name: AI-Sempai
define gc = Character('Girl-chan', color="#ffc8c8", image="gc")
       # Working Name: Girl-chan
define ha = Character('Hoshiko Akagami', color="#ffc8c8", image="gc")
       # Girl-chan's name after her name reveal
define hs = Character('Husbando-sama',color="#c8c8c8", image="hs")
       # Working Name: Husbando-sama


define n = Character(None, kind=nvl, what_prefix = "{i}", what_suffix = "{/i}")
        # NVL Narrator
#26/05/2015
       # Non-NVL Narrator
define nn = Character('', what_prefix = "{i}", what_suffix = "{/i}")

# MINOR CHARACTERS
define s1a = Character('???', color="#c8c8c8")
       # MC-kun's opponent in the very first scene
define s6a = Character('???', color="#c8c8c8")
       # Husbando-sama before his name is known

# DINOSAUR ENDING CHARACTERS
define kq = Character('Kanserous Quiboo', color="#eeeec8", image="kq")
        # Need to change word color
        # Need to add images
define um = Character('Uncle Minh', color="#c8eeee")
define uk = Character('???', color="#c8eeee")
        # Uncle Minh before his name is known

#------------------------------CONFIG------------------------------#

# NVL CONFIGURATION
init python:
    #26/05/2015
#    config.all_character_callbacks = [placeHolderVoice]
    
    n_menu = nvl_menu
    
    # The color of a menu choice when it isn't hovered.
    style.nvl_menu_choice.idle_color = "#ccccccff"

    # The color of a menu choice when it is hovered.
    style.nvl_menu_choice.hover_color = "#ffffffff"

    # The color of the background of a menu choice, when it isn't
    # hovered.
    style.nvl_menu_choice_button.idle_background = "#00000000"

    # The color of the background of a menu choice, when it is
    # hovered.
    style.nvl_menu_choice_button.hover_background = "#ff000044"

    # How far from the left menu choices should be indented.
    style.nvl_menu_choice_button.left_margin = 20

    style.nvl_window.background = "nvl_window.png"
    style.nvl_window.xpadding = 55
    style.nvl_window.ypadding = 55
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve

# OTHER DECLARATIONS

define chardissolve = Dissolve(0.4)

init python:
    renpy.music.register_channel("sound2","sfx",False)


#----------------------------SCRIPT------------------------------#

# The game starts here.
label start:
    $ hero_pts = 0
    $ girl_pts = 0
    $ trap = False # boolean that changes scene 6 -- possibly set to true in scene 5
    $ annoyed = False # boolean that changes scene 7, possibly set to true in scene 7
    $ thirsty = False # boolean that changes scene 8, possibly set to true in scene 7
    
#-------------------------------------  COMMON ROUTE  -------------------------------------#

#---------------------------- SCENE 1: Inside the Simulator----------------------------#

    stop music fadeout 1.0
    scene bg black
    with fade
    pause 1.0
    scene bg cockpit at truecenter
    with fade
    pause 1.0
    play music "music_Indended.mp3"
    ai "Unit strength at 75\%, fuel at 10\%, recommending retreat."
    mc "Fool, I haven’t even used your new missiles yet. What fun are implants if you never get to play with them?"
    play sound "sfx_missilelaunch.mp3"
    nn "I pressed the button, unleashing a stream of hundreds of missiles at the enemy armada."
    play sound2 "sfx_grenade.mp3"
    scene bg cockpit2 at truecenter
    with dissolve
    pause 1.0
    scene bg cockpit at truecenter
    with dissolve
    nn "They locked onto their targets, destroying those ugly L0li-type mecha."
    mc "Besides, real men don’t give up. Never retreat, never surrender. Only a true warrior can understand that."
    mc "I’ll show them that they were fools to challenge me and my wAIfu."
    ai "You’re so adorable when you eliminate the enemy ships."
    play sound "sfx_alienmachinegun.mp3"
    play sound2 "sfx_comet.mp3"
    nn "Several beams of light erupted from the smaller fighters’ cannons. On reflex, I weaved through them."
    mc "If we run away, they’ll attack someone else. I have to protect others like me. I have to prove myself as a man."
    mc "Calculate the range vectors for their movement, and fire the T.T. when they get in range."
    ai "Calculating. Resolved. Will you say it?"
    nn "I smiled."
    mc "T.T. TWISTER, YELLOW DISCHARGE!" # this line was changed 05/06/2015
    play sound "sfx_lasercannon.mp3"
    nn"Her left chest cavity opened up, and fired a spiraling plasma beam at a squad of l0li-types."
    play sound2 "sfx_grenade.mp3"
    scene bg cockpit2 at truecenter
    with dissolve
    pause 1.0
    scene bg cockpit at truecenter
    with dissolve
    nn"Only for a moment, the blackness of space was lit up by balls of fire."
    scene bg cockpit at Shake((0.49, 1.08, 0.5, 1.0), 1.0, dist=8)
    play sound "sfx_blast.mp3"
    pause 1.0
#    "The cockpit shook." # We can take out this line and just have the cockpit shake.
    ai "Left arm damaged."
    s1a "You put up a good fight, but you’re finished now. Surrender now, and maybe I’ll allow you to join the 08th L0li-type Raiders."
    mc "You’re all sick, you’ve perverted your Waifu-ships for war, and yet they still can’t stand on the same pedestal as mine."
    mc "They may be more compact, but they’re cheaply designed ugly pieces of junkyard garbage."
    mc "I fight to protect my property, and the welfare of others. You have no honour, and I look forward to ending this operation of yours, along with yo—"
    scene bg cockpit at Shake((0.51, 1.1, 0.5, 1.0), 1.0, dist=10)
    play sound "sfx_blast.mp3"
    pause 1.0
#    "PLAKOOM. The cockpit shook" # We can take out this line and just have the cockpit shake.
    ai "Main gun damaged. Weapons systems offline."
    mc "Full power to shields and engines. You would fire at me in the middle of my negotiation speech?"
    s1a "Of course. We have no honour."
    mc "AI-sempai, prime the engines and ammunition storage for detonation. I’ll fly us into their recovery ship."
    ai "Are you sure?"
    mc "I’m always 100\% sure. There’s no need to question it."
    play sound "sfx_alienmachinegun.mp3"
    play sound2 "sfx_comet.mp3"
    nn"My ship flew at full speed, dodging several units firing from behind. Through precise and careful movements, AI-sempai moved to dodge each shot."
    scene bg cockpit at Shake((0.48, 1.07, 0.5, 1.0), 1.0, dist=12)
    play sound "sfx_blast.mp3"
    pause 1.0
    nn"Most of them, anyway."
    nn"This is it. I’ve devoted my life to protect others. There is no shame in how I live. I’ll give all that I can to fight evil, so that others can be safe."
    nn"Sayonara."
    scene bg cockpit3 at Shake((0.52, 1.11, 0.5, 1.0), 3.0, dist=15)
    play sound "sfx_grenadeexplosion.mp3"
    stop music fadeout 2.0
    pause 2.0

#---------------------------- SCENE 2: Outside the Simulator ----------------------------#
    scene bg white
    with dissolve
    pause 2.0
    play sound "sfx_appear.mp3"
    pause 2.0
    scene bg simroom
    with dissolve
    nn"The capsule opened, and I was bombarded with lights."
    mc "Just like my real entrance into Valhalla."
    show ai at center:
        yalign 0.0
        zoom 0.4
    with dissolve
    play music "music_Orderly.mp3"
    ai "You did excellent today. I’m so lucky to have such a strong man protecting me."
    show ai sad
    with chardissolve
    ai "But do you always have to kill yourself at the end of our simulations? You’re beginning to worry me."
    mc "I have to be prepared to defend myself and others. If I have to die in order to save others, I’ll do it. That’s what defines me as a human being."
    show ai
    with chardissolve
    ai "Also, while you were in the simulator, I took a hit from space debris. I was wondering if you’d repair me? It’s in an area I can’t reach."
    mc "Of course, muffin. But you should take more evasive maneuvers, unless you want me to take care of you forever."
    show ai happy
    with chardissolve
    ai "Tee-hee, that wouldn’t be too bad, being in your magic hands."
    nn"This is the third time this week that she needs repairing, and the space debris is getting more common."
    nn"Maybe we’re headed to the remains of a battle. Maybe we should plot a better course."

menu:
    "We should head towards it, perhaps there are people in danger.":
        $ hero_pts += 1
        jump preparation
    "It’s unlikely that a fleet would remain in the same place as a battle for long.":
        $ hero_pts -= 1
        jump preparation

#---------------------------- SCENE 3: Preparation for Repairs ----------------------------#

label preparation:
    mc "It’s been a while since we’ve seen any human civilization. Maybe you need an upgrade to your guidance systems."
    show ai sad
    with chardissolve
    ai "I’m offended, are you saying I’m st-stupid?"
    nn"She’s so cute when she acts offended. Sometimes I’m tempted to insult her, just to see the look on her face."
    mc "Alright, so where’s the damage? It’s not on the exterior, is it?"
    show ai
    with chardissolve
    ai "No, it’s inside of me. It shouldn’t take too long. Just a six minute walk."
    mc "A six minute walk?! Can’t you use robotic arms or something to carry me?"
    ai "Sorry sweetie, it was the robotic arms control console that was damaged."
    mc "Oh shit. I better get it fixed then."
    mc "I don’t want to risk choking or putting too much food in my mouth when I rewatch ‘Advanced Soldier Mobile Taskforce: Millenium Ghost of the 30th Seed Destiny’."
    stop music fadeout 2.0
    scene bg hallway
    with CropMove(0.5, "wiperight")
    window show
    with dissolve
    n "As much as I don’t like it, I have to put my body to it’s limits in order to help the ones I love."
    n "Life is a struggle between the living and the dead. Those who wish to achieve and those who give into hopeless despair."
    n "I laugh at fate, and make my own destiny with my own two hands. I fight because I am alive, and because the alternative is to lie still and die."
    n "I will never give up, I will continue to crawl forward until my last breath."
    nvl clear
    window hide
    with dissolve
    # jump end_demo
    play music "music_DarkRock.mp3"
    nn"Ugh. This walking, it’s too brisk for me."
    ai "Hiroo! Are you okay?!" # change to "Hiroo"? It's kind of awkward that she's using his full name. That, and simply using "Hiroo" shows a close relationship between the two.
    mc "Heh, of course."
    ai "Why don’t you just take a break? You’re almost there, just up that ladder."
    
    if hero_pts < 0:
        jump choice2
    else:
        jump repairs

label choice2:
# The choice that can lead to dino ending.
menu:
    "Take a break.":
        jump end_dino
    "Press on.":
        $ hero_pts += 1
        jump repairs

#---------------------------- SCENE 4: Repairs ----------------------------#

label repairs:
    nn"I can’t stop panting, but I won’t let her see."
    nn"For those around me, I always have to be strong."
    nn"I can never show weakness, or else others will lose hope."
    nn"I have to be a shining light in the darkness that all those who cower can look to as a glorious example."
    nn"I will press on."
    mc "AI-sempai."
    ai "What is it, honey?"
    mc "I change my mind. After I repair you, I’m going to watch ‘Doki-Doki Smile: Heart Prefecture’. I’ve earned it."
    ai "Okay, I’ll set it up for you. Anything else?"
    mc "Yeah, get the choco-pockets and kiwi chips ready."
    nn"With each rung, I climb closer to my goal."
    nn"With each breath I take I gain momentum."
    nn"Nothing can stop me."
    scene bg engineroom
    with CropMove(0.5, "wiperight")
    ai "Now that you’re inside the room, all you need to do i—"
    mc "I know what I’m doing. I just attach the wires in the correct sequence. It’s all colour coded."
    ai "You’re so smart."
    scene bg black
    with dissolve
    stop music fadeout 2.0
    pause 2.0
    jump post_repairs

#---------------------------- SCENE 5: After the Repairs ----------------------------#

label post_repairs:
    scene bg engineroom
    with dissolve
    nn"As soon as I plug the wires into the correct sockets, an arm pats me on the back."
    show ai happy at center:
        yalign 0.0
        zoom 0.4
    with dissolve
    ai "Oh baby, thanks for helping me. I have no idea what I’d do without you."
    nn"She’d probably be blown to smithereens. Or maybe she’d be safe on Earth."
    nn"Maybe she would be stolen and loaded with weapons by those damn terrorists of the Fourteenth Lolitanian Convention, or the Oppanian Union."
    mc "Alright, I’ve done enough for today. Time for anime. Carry me to my place."
    scene bg hallway
    with CropMove(0.5, "wiperight")
    nn"For nearly two minutes, I’m slowly and carefully carried to my place by massive, loving robot arms."
    scene bg mediaroom
    with CropMove(0.5, "wiperight")
    nn"They carry me to my place, my throne."
    mc "Excellent. Now, commence feeding."
    play sound "sfx_strawslurp.mp3"
    nn"I open my mouth, and food is placed into my mouth as ‘Doki-Doki Smile: Heart Prefecture’ begins."
    play music "music_Fenster.mp3"
    nn"I’m filled with melted chocolate, fried fruit slices and salted dough, which I chew as quickly as possible to make room for more."
    show ai at center:
        yalign 0.0
        xalign 0.7
        zoom 0.4
    with dissolve
    mc "How much is left?"
    ai "70\% of today’s food intake consumed."
    nn"Damn. It’s all gone so fast."
    nn"I need to keep my strength and energy up in case of an emergency."
    nn"If I’m unreliable, I’m putting human lives at risk."
    mc "Continue. By the way, your cooking is still delicious. You do so well for having a limited foodprinter."
    show ai happy
    with dissolve
    nn"I try to savour the rest of my food, but it just tastes so good in my gullet."
    nn"Nothing like filling an empty stomach after a hard day’s work."
    stop music fadeout 2.0
    nn"Within seconds, it’s all gone."
    show ai serious
    with dissolve
    ai "Hiroo, emergency. I’ve detected a damaged solo pleasure ship nearby, a husband-class vessel. It’s name is registered as ‘Alien Cigarette’." # removed "-kun"; probably best to keep naming consistent between these two, and no honorific means closer relationship

menu:
    "Head to it, there could be someone in need of help.":
        jump boarding
    "It’s a trap. All the more reason why I should go.":
        $ hero_pts += 1
        $ trap = True
        jump boarding

#---------------------------- SCENE 6: Boarding the Husbando Ship ----------------------------#

label boarding:
    if trap == True:
        mc "It’s an obvious trap. Probably raiders or pirates who want to take advantage of people who want to rescue others."
        mc "That’s why we have to go towards it."
        mc "If we take the bait, I’ll take the risk in combat."
        mc "I’ll destroy them, or I’ll damage them to the point where they won’t be strong enough to ambush anyone again."
    else:
        mc "We should head towards it. There may be someone in danger, so we have to rescue them."
    ai "Aye, aye Captain."
    play music "music_PlansInMotion.mp3"
    mc "Ready the weapons. What’s functional?"
    ai "The flak and disruption guns."
    mc "Alright, keep a lookout for any type of radiation."
    hide ai
    with dissolve
##################This one looks kind of ugly, so I'm going to leave the original code here if you want to juxtapose them.
#    scene bg airlock
#    with CropMove(0.5, "wiperight")
#    show ai at center:
#        yalign 0.0
#        xalign -0.2
#        zoom 0.4
#    with dissolve

############ BQ: I found a way to do this, but I decided it didn't make sense for AI-Sempai's body to be in the airlock (I'm thinking she can talk over comm or something), so I took her out. For reference, this is what I did:
#    scene bg airlock
#    show ai at center:
#        yalign 0.0
#        xalign -0.2
#        zoom 0.4
#    with CropMove(0.5, "wiperight")

    nn"Now we wait."
    nn"..."
    nn"..."
    nn"..."
    scene bg black
    with dissolve
    pause 1.0
    scene bg mediaroom
    with dissolve
    mc "Are we there yet?"
    ai "Yes, we’ve been here for ten minutes."
    ai "I’m not picking up any signs of radiation. If ships are here, they’re hiding it well."
    mc "It’s possible. It’s also possible they have stealth ships, or that you’re outdated. Are you completely certain?"
    ai "Of course, I would never put you in danger if I wasn’t 100\% certain."
    mc "Fly around for a bit. Investigate any large spaces that a ship could fit into."
    ai "Alright Captain. Searching nearby space for spaces."
    mc "Belay that order. I’m going into that derelict ship."
    scene bg hallway
    with CropMove(0.5, "wiperight")
    pause 1.0
    scene bg airlock
    with CropMove(0.5, "wiperight")
    mc "Sometimes you just have to go with your gut, especially when you’re uncertain."
    mc "If I die, kill the people that killed me, or save whoever I’m going in that ship to save. Either is fine."
    ai "Aye-aye, Captain."
    stop music fadeout 2.0
    play sound "sfx_chamber.mp3"
    scene bg husbando_ext
    with irisout
    pause 1.0
    play music "music_SpacialWinds.mp3"
    nn"After suiting up, I enter the derelict ship. A large hole is in it’s center. So this is the source of that space debris."
    nn"I continue to float into the ship."
    nn"Doesn’t look like major damage. Aside from the big hole, it doesn’t look like the engines or anything important was broken."
    nn"I open a bulkhead, and air blasts me backwards."
    nn"Luckily, my back collided with the steel wall behind me, and not empty space."
    scene bg husbando_int
    with CropMove(0.5, "wiperight")
    nn"After the air is sucked out, I enter the room and close the door behind me."
    nn"Artificial gravity is working. The room is reoxygenating. Is there an AI here?"
    show hs at center:
        yalign 0.0
        zoom 0.2
    with dissolve
    play sound "sfx_robotblip.mp3"
    s6a "Greetings. I am Husbando-sama."
    hs "Currently I am damaged, and my Captain is located in a cryogenic room on Level-A."
    play sound2 "sfx_robotblip2.mp3"
    hs "Please take care of her for me. I can only take automated actions until I am repaired."
    nn"Right, some ships have computer processing built throughout the ship’s walls in order to maximize living space."
    scene bg husbando_cryo
    with CropMove(0.5, "wiperight")
    nn"I follow the directions until I find it. A girl in a cryogenic case."
    scene bg husbando_cryo_close
    with dissolve
    nn"I make sure all the bulkheads are sealed and the room is oxygenated before opening it."
    play sound "sfx_chamber.mp3"
    nn"It opens, and I see her."
    nn"She’s chubby, but her skin is very pale. Her hair is red with pink highlights."
    nn"Pretty trashy, but she’s a human being. If this is what I fight to protect, then so be it."
    scene bg husbando_cryo
    with dissolve
    nn"She opens her eyes, and looks at me."
    stop music fadeout 0.5
    show gc disoriented at center:
        yalign 0.0
        zoom 0.4
    with dissolve
    pause 1.0
    gc "Fuck, my head hurts. Thanks for saving me though."
    mc "I’m just glad I got to you before raiders, scuttlers or pirates."
    mc "Or who knows, a stray torpedo or laser beam could cut through this thing like softwads."
    mc "Let’s get to my ship, the Kryptonite Phantom."
    gc "Torpedoes? How long was I out?"
    mc "Who knows? The war’s been going on for nearly five years."
    mc "But we should get you to safety. I’ll see if AI-sempai can repair your ship."

#---------------------------- SCENE 7: Back on the Waifu Vessel ----------------------------#
    
    scene bg husbando_int
    with CropMove(0.5, "wiperight")
    nn"She suits up, and we exit the Alien Cigarette."
    scene bg husbando_ext
    with dissolve
    nn"She grabs my arm and we float out together into space, and into the entrance of AI-sempai."
    play sound "sfx_chamber.mp3"
    scene bg airlock
    with irisin
    nn"Her robotic arms gently guide us into the airlock, and together we enter. The door closes behind us."
#xalign - float (taken from the documentation)
#Equivalent to setting xpos and xanchor to the same value. This has the effect of placing the displayable at
#a relative location on the screen, with 0.0 being the left side, 0.5 the center, and 1.0 being the right side.

    show gc at center: # note to Seilai: X alignment fixed-- read the above to see how to do it.
        yalign 0.0 
        xalign 0.5
        zoom 0.4
    with dissolve
    play music "music_RapChill.mp3"
    gc "So there’s a war going on?"
    mc "How long have you been out? The war started almost ten years ago."
    gc "I don’t know. What year is it?"
    mc "AI-sempai?"
    show gc at left: # note to Seilai: X alignment fixed-- read the above to see how to do it.
        yalign 0.0 
        xalign 0.1
        zoom 0.4
    with move
    show ai at right:
        yalign 0.0
        xalign 0.9
        zoom 0.4
    with dissolve
    ai "It is 2118."
    show gc upset
    with dissolve
    gc "2118? And you say it’s been going on for a decade?"
    mc "Of course, do I need to repeat myself?"
    gc "Weird."
    mc "AI-sempai, assess the damage to Alien Cigarette and see if you can repair it."
    ai "Assessing, assessing, assessed."
    ai "Damage appears minimal, and there seems to be enough supplies to repair it. It should only take three and a half hours."
    stop music fadeout 2.0
    hide ai
    with dissolve
    show gc upset at center: # note to Seilai: X alignment fixed-- read the above to see how to do it.
        yalign 0.0 
        xalign 0.5
        zoom 0.4
    with move
    mc "Well, I’m going to watch anime. See you."
    show gc
    with dissolve
    gc "You watch anime? Me too. Mind if I join you?"
    
menu:
    "She’s obviously very thirsty, despite being frozen for who knows how long. I might as well reap the rewards of being a hero.":
        $ hero_pts += 1
        $ thirsty = True
        jump dokidoki
    "Maybe that won’t be so bad.":
        $ girl_pts += 1
        jump dokidoki
    "She’s just going to annoy me.":
        $ annoyed = True
        jump dokidoki

label dokidoki:
    if annoyed == True:
        mc "Fine. I’m rewatching ‘Doki-Doki Smile: Heart Prefecture’."
    else:
        mc "Sure. I’m rewatching ‘Doki-Doki Smile: Heart Prefecture’."
    gc "That’s the one where the anthropomorphized hearts that look like schoolgirls fall in love right?"
    mc "You’ve seen it? I thought it was really obscure."
    play music "music_RockingJazzhands.mp3"
    mc "It only came out a few years ago, and it’s basically a metaphor or reflection on how all the ‘bleeding hearts’ within the greater solar systems are ignoring more important problems in order to focus on education and older values."
    gc "I th—"
    mc "Aorta-chan is essentially a deconstruction of neo-yuri and shonen tropes. Instead of going directly after other hearts, using subtle displays of affection she slowly makes them all fall in love with her."
    mc "Not to mention the excellent animation, writing and soundtrack. I listen to the ED, ‘Butterfly Cute’ on a daily basis, and every once in a while AI-sempai will dress up in a heart costume for me."
    mc "Overall, I’d have to say it was my pick for anime of the year and #4 in my top nine after ‘Chocoloids’, ‘Dead Battle Zero’, and ‘Yuri Yuri Mechriders: Knights of the Millenial Spiral’."
    show gc upset
    with chardissolve
    gc "I still can’t believe you like ‘Doki-Doki Heart Prefecture’."
    gc "I thought it was just overly sappy middle school bullshit that fetishizes little girls and internal organs in the most boring way."
    gc "The characters, especially Ayase were as flat as their own chests."
    gc "Worst of all, it had a terrible message. The fact that Aorta gets to string along a dozen other kids because she doesn’t care about them pisses me off."
    mc "What? You totally missed the point of the series if you think that."
    mc "It was essentially a uhh deconstruction, and Aorta’s behaviour is supposed to be uhh, a uhh, just totally innocent and accurate display of kids because they’re young and they can make selfish decisions. That’s why it’s realistic, unlike many other shows."
    mc "Aorta subverted the ultra-loli trope by being so carefree. She actually shows many emotions throughout the series, unlike a lot of the characters in the other anime I’ve watched."
    gc "Just because someone emotes doesn’t mean they’re a dynamic character."
    gc "They’re all pretty much the same as they were before, except now they’re all basically slaves to Aorta."
    mc "I’m going to stop talking about this before I forget that I’m supposed to be protecting humanity."
    gc "You’re protecting humanity? Against what?"
    stop music fadeout 1.0
    mc "..."
    mc "From itself. Yeah, that’s right."
    mc "I still haven’t explained the war, have I? Yeah, the war. Where to begin?"
    mc "You see, a group of zealots that believed that technology was to blame for suicide, loneliness and suffering in society rose up."
    mc "They wanted people to return to a more idyllic time when labour was necessary, where no one felt like they were a burden."
    mc "But others like me see them for what they are, cruel slavers who only desire power, not the welfare of the human race."
    mc "There were many people like me, who got the news as they were drifting in space with their waifus."
    mc "Some have chosen to ignore them, but I know that when the time comes, I will fight them."
    ai "Entertainment is ready, Hiroo."
    mc "Sweet."

#---------------------------- SCENE 8: Watching Anime with Girl-chan ----------------------------#

    scene bg mediaroom
    with CropMove(0.5, "wiperight")
    show gc at center:
        yalign 0.0
        xalign 0.7
        zoom 0.4
    with dissolve
    if thirsty == True:
        nn"I lead her to my pleasure chamber."
    else:
        nn"I lead her to the media room."
    mc "Here is my seat. As you can see, it’s made to be perfect for my body."
    mc "I don’t have a second one, so you’ll have to sit on the floor."
    show gc upset
    with dissolve
    play sound "sfx_strawslurp.mp3"
    nn"I grabbed my nutrtition tube from the ceiling and sucked. Warm chocolate and fried tortilla slid into my mouth."
    play music "music_Fenster.mp3"
    gc "Fuck, do you really eat from a tube?"
    mc "Of course. It’s much more efficient."
    mc "For one thing, the ship doesn’t have to waste energy cleaning dishes. These dishes can also be used as flak if it comes down to it, since they’re not being used."
    gc "That’s still disgusting."
    nn"Whatever. You wish you were half as cute as Aorta-chan."
    show gc bored
    with dissolve
    gc "Oh god, we’re actually watching this."
    mc "What?"
    nn"She’s silent. Bored. Does she even understand what we’re watching?"
    mc "Well excuse me. I risked my life to save you, and then I allowed you to stay in my ship, even showing you my favourite anime. The least you could do is show me some respect, you bitch."
    mc "I could have sold you into slavery if I wanted to, but I did the selfless thing. You know why? Because I’m a good person."
    gc "Look, I’m s—"
    stop music
    mc "I PUT MYSELF OUT THERE. I TOOK THE RISK, I WELCOMED YOU INTO MY LIFE AND YOU INSULT ME AND CALL ME A FREAK?!"
    ai "Hiroo, please breathe. Your heart rate is enormously high, and you’re putting yourself at risk."
    nn"I breathed. She’s right. My life is too valuable to be wasted here."
    mc "Just hurry the repairs."
    mc "Girl-chan, watch what you’d like. I’ll be in the simulator if you need me."
    
#---------------------------- SCENE 9: Simulator Revisited ----------------------------#

    scene bg simroom
    with CropMove(0.5, "wiperight")
    nn"I walked to the simulator. It felt good to be away from her, even if I had to give up my reward."
    mc "Sometimes I wonder why I fight if people are going to behave like that."
    ai "Maybe it’s because you enjoy it. You’ve loved mecha since your parents purchased me."
    mc "Before, actually. I remember building models with Dad when I was only six. Good times."
    play music "music_HexxitDRAVE.mp3"
    nn"I wish I could see him again. All of them. Midori, Mom, even Uncle Minh. It hurts to think that they could be in danger."
    nn"I entered the simulator." # note to Seilai: Finished it with a bit of easy copy-pasting.
    scene bg black
    with dissolve
    pause 1.0
    scene bg cockpit at truecenter
    with dissolve
    mc "Alright you bastards, die! Die! Die! Die! Die! Die!"
    play sound "sfx_missilelaunch.mp3"
    nn"I blasted each mech, one by one."
    # 19/06/2015: BQ - Removed the explosion here, since I don't think we need two in a row. Tweaked it somewhat.
    nn"I picked off the ones in the rear of formation first, then the middle, and finally the front. These squads are no match against the heroic might of Hiroo Onoda!"
    play sound2 "sfx_grenade.mp3"
    scene bg cockpit2 at truecenter
    with dissolve
    pause 1.0
    scene bg cockpit at truecenter
    with dissolve
    nn"A new mech appeared, this one was clad in blue armour. A special unit, maybe the leader."
    play sound "sfx_comet.mp3"
    nn"It darted quickly, faster than I could lock on. Looked like it was trying to run."
    mc "Fire the flak gun to limit his maneuvering. I’ll take the final shot."
    play sound "sfx_grenade.mp3"
    nn"Flak flew to the mech’s left, and it changed course to the right, right into the right position."
    play sound2 "sfx_lasercannon.mp3"
    mc "T.T. TWISTER!"
    play sound "sfx_blast.mp3"
    scene bg cockpit2 at truecenter
    with dissolve
    pause 1.0
    scene bg cockpit at truecenter
    nn"The mech exploded."
    mc "Can’t evade that, can you?!"
    ai "More enemy mecha and ships detected. Appears to be two groups of mecha supported by several longer ranged craft, and a repair vessel."
    mc "Alright. Here’s the plan. I’ll make the first group scatter by closing in and firing missiles at point blank, manually. You’ll fire the other weapons once the squad breaks."
    play sound "sfx_alienmachinegun.mp3"
    play sound2 "sfx_comet.mp3"
    nn"I flew her directly into enemy fire. Others may think I’m reckless, but I’m not a coward. I see something I want, and I close in on it. I act. I am a hero."
    # rumble effects + beeping
    scene bg cockpit at Shake((0.48, 1.07, 0.5, 1.0), 1.0, dist=12)
    play sound "sfx_smokealarm.mp3"
    play sound2 "sfx_blast.mp3"
    ai "Evasion failed. I am 45\% damaged."
    mc "FIRE!"
    play sound2 "sfx_missilelaunch.mp3"
    nn"Not close enough. They evaded them too easily."
    mc "Fuck, they’re circling me. They’re surrounding us! Full power to thrusters!"
    scene bg cockpit3 at Shake((0.52, 1.11, 0.5, 1.0), 3.0, dist=15)
    play sound "sfx_grenadeexplosion.mp3"
    ai "Taking heavy damage. Emergency eject!"
    mc "No, a Captain always goes down with his wAIfu. St—"
    scene bg black
    stop music fadeout 0.1
    nn"It all went dark."
    
#---------------------------- SCENE 10: The Revelation ----------------------------#
    scene bg white
    with dissolve
    pause 2.0
    play sound "sfx_appear.mp3"
    pause 2.0
    scene bg simroom
    with dissolve
    nn"Light again. Valhalla."
    nn"Wait. She’s here."
    show gc at center:
        yalign 0.0
        zoom 0.4
    with dissolve
    gc "Hiroo, I’m sorry for what I said, but I need to talk to you."
    nn"She would only apologize if she needed something. Selfish, typical bitch."
    mc "What is it? What do you want from me?"
    gc "Can we go somewhere private? Somewhere without AI-sempai’s prying eyes?"
    nn"She’s actually kind of cute. I don’t want to walk all the way to the bedroom though."
    mc "AI-sempai, cut all power to this room."
    ai "Of course."
    play sound "sfx_button.mp3"
    scene bg black
    nn"The lights went out. We were in pitch darkness, at least until my eyes adjusted."
    gc "Hiroo, there is no war. The last time I was awake was two months ago, and there was no war then."
    gc "Think about it, how would I know about ‘Doki-Doki Prefecture’ if I’d fallen asleep before the war?"
    mc "What? Are you saying AI-sempai would lie to me?"
    gc "Either she lied, or she’s misinformed."
    mc "But it would be against her programming to put me in danger. Why would she make me feel like I’m in danger?"
    mc "She’s programmed to love and take care of me, physically, mentally, emotionally and sexually. Whatever you’re saying makes no sense."
    gc "Look, I have no reason to lie to you. I’m leaving soon, and you can come with me. I don’t want you in the hands of a dangerous AI."
menu:
    "She must be a Lolicon agent here to enslave me.":
        $ hero_pts += 1
        jump end_demo # or scene 11
    "I can’t trust AI-sempai any longer.":
        $ girl_pts += 1
        jump end_trustgc

#-------------------------------------  BRANCH A: END OF DECEPTION  -------------------------------------#

label branch_a:
    # will put stuff here later
    jump end_demo
    
#-------------------------------------  BRANCH B: TOO FAR GONE  -------------------------------------#

label branch_b:
    # will put stuff here later
    jump end_demo

#---------------------------------------------  ENDINGS ---------------------------------------------#

#---------------------------- ENDING 4: Trust Girl-chan Ending ----------------------------#
label end_trustgc:
    mc "I think you’re right."
    gc "I’m sorry, what?"
    nn"It makes sense. I haven’t left the Kryptonite Phantom in years, and AI-sempai takes care of the automated supply runs. I can’t know for sure what’s going on out there."
    nn"If what she says is true, then—"
    gc "Well, what do you know? You actually do have a brain under that mound of lard on your shoulders."
    mc "Alright bitch, if you insult me ONE MORE FUCKING TIME, I SWEAR I’M GOING TO—"
    gc "Calm down, I was just joking."
    mc "I DON’T THINK IT’S A GOOD TIME FOR JOKES RIGHT NOW!"
    gc "You know what? You’re right about that."
    gc "But before we talk about what we’re going to, you should take a few deep breaths and calm down."
    nn"I do as she says. After all, a hero must never lose his composure."
    pause 1.0
    nn"I speak again when I’ve had about a minute to cool down."
    mc "Let’s see... Since I can’t trust AI-sempai anymore, it looks like we’ll have to abandon my ship."
    nn"As much as I hate it, it looks like we’ll have to cooperate from now on. I just have to get used to it."
    gc "Luckily for us, it seems AI-sempai connected the airlocks of our ships while she was making the repairs."
    mc "Well, that’s convenient. How do you know?"
    gc "I walked by the airlock while you were doing whatever it was you were doing here. At any rate, that’s our ticket out of here."
    gc "Come on. We should hurry."
    mc "But... I can’t really walk. AI-sempai is responsible for bringing me around the ship."
    gc "Figures. Well, that complicates things."
    mc "Hang on. I have an idea."
    gc "You? Really?"
    mc "Just shut up and listen. You must have a pretty decent sized anime collection on your ship, don’t you?"
    gc "Okay, what the fuck does that have to do with anything?"
    mc "I could just tell AI-sempai that I’m visiting your ship to check out what you have. Its repairs must be almost finished by now, so it should be safe."
    gc "You do know that anybody can just download stuff from the Futanet for free, right? She’d wonder why you don’t just do that."
    nn"Damn, she’s actually right. What, then?"
    mc "Well, it has to be something that’s actually on the ship. She did survey it, after all."
    mc "Do you have something that might interest me? Something you can’t download. Like, physical objects or some shit like that?"
    gc "Well, um, there is something..."
    
    scene bg hallway
    show gc at center:
        yalign 0.0
        zoom 0.4
    with CropMove(0.5, "wiperight")
    nn"She helps me out of the simulator room, and out to the hallway."
    nn"The door was still functioning. I suppose AI-sempai didn’t intend to trap us in there. I can be certain now that she didn’t hear us."
    mc "AI-sempai, restore power to the simulator room."
    ai "Yes, Captain."
    mc "And can you transport me to the airlock? I want to visit Girl-chan’s ship."
    mc "She says she’s got a huge collection of ‘Super Sexy Swimsuit Soldiers’ figures in her display room."
    show gc bored
    with chardissolve
    gc "Oh god."
    ai "I’ll gladly carry out your request, but I never saw you as a fan of that series."
    mc "It’s the figures. The craftsmanship. I want to see how they compare to my mecha."
    ai "Certainly."
    nn"Her loving mechanical arms pick me up and take me across the hallways of the ship while Girl-chan walks by my side."
    nn"AI-sempai doesn’t suspect a thing."
    
    scene bg airlock
    show gc at center:
        yalign 0.0
        zoom 0.4
    with CropMove(0.5, "wiperight")
    ai "Since I’m connected to the Alien Cigarette, you don’t require any space suits on the way in."
    ai "And Hiroo, it seems there is a wheelchair in its airlock’s storage compartment."
    gc "That’s my grandmother’s old wheelchair. He can use that."
    ai "Splendid. Have a nice visit, Hiroo."
    nn"The airlock door opens, leading directly into the Alien Cigarette. Girl-chan opens the storage compartment, and removes the wheelchair. I carefully take a seat."
    gc "Ugh, it’s sagging a little. I hope you don’t break it."
    nn"Even in a dire situation such as this, she still manages to infuriate me. But I suppress my reaction."
    nn"My life, defined by the need to save others, is in danger. I can’t die for any reason besides that."
    nn"And so I must keep calm and press forward, so I can live to save lives someday."
    
    # need husbando interior repaired version, if handy
    jump end_demo

#---------------------------- ENDING 7: Dinosaur Ending ----------------------------#
label end_dino:
    stop music fadeout 1.0
    mc "I don’t remember the hallway being this far..."
    mc "I have to make it to the engine room."
    
    play sound "sfx_trex2.mp3"
    pause 1.0
    
    mc "It can’t be..."
    
    play sound "sfx_trex1.mp3"
    pause 1.5
    
    show kq at center:
        yalign 0.0
        xalign 1.4
        zoom 0.7
    with dissolve
    play music "music_MassiveCoronary.mp3"
    
    kq "‘Tis I, Kanserous Quiboo the tyrannosaurus rex! I have come to end thy Kanserous existence."

    show kq at center:
        yalign 0.0
        xalign 2.8
        zoom 0.9
    with chardissolve
    mc "I don’t even know you and this is crazy. Why would you even end me if you and I are both Kanserous?"

    show kq at center:
        yalign 0.0
        xalign 0.0
        zoom 1.2
    with chardissolve
    kq "‘Tis because we are both Kanserous that we must fight."
    show kq at center:
        yalign 0.0
        zoom 1.6
    with chardissolve
    kq "Have at thee!"
    
    play sound "sfx_woosh.mp3"
    show bg hallway at Shake((0.51, 1.08, 0.5, 1.0), 1.0, dist=4)
    show kq at Shake((0.51, 1.08, 0.5, 1.0), 1.0, dist=4)
    nn"I dodge left to avoid the hook."
    show bg hallway at Shake((0.51, 1.08, 0.5, 1.0), 1.0, dist=2)
    show kq at Shake((0.51, 1.08, 0.5, 1.0), 1.0, dist=8)
    play sound "sfx_bite.mp3"
    nn"But I fail. The Quiboo severs my right arm, splashing blood into my eyes."
    
    scene bg white with dissolve
    uk "I didn’t remember this part in the Vietnam War, what the hell happened? Back then I fight soldiers, not monster. This ain’t Monster Hunter."

    mc "Who are you?"

    um "I am your Uncle Minh from the Vietnam War."
    um "Hiroo, why is it that you try so hard to live? Look at your missing arm and burning eyes, the pain you are enduring is worse than death itself."

    mc "I’m not gonna listen to some Vietnamese Uncle about whether I should live or die!"
    
    scene bg hallway with dissolve:
        xalign 1.0
        zoom 1.2
    nn"As I bleed out, I try to run."
    scene bg hallway at Shake((-0.2, 0.5, 0.5, 1.0), 1.0, dist=8):
        zoom 1.8
    play sound "sfx_bounce.mp3"
    nn"But I slip on my blood and trip over a wire coming out of the broken walls."
    play sound "sfx_bonecrush.mp3"
    nn"My left leg snaps."

    mc "ARGGHH!!!"
    
    nn"Why must I die here? Having accomplished nothing."
    
    scene bg white with dissolve
    um "Hiroo, why do you fear death? If you are afraid of the scene before you, crash your head onto the iron wall."
    um "Whether it’s hell or heaven, it can’t be worse than here."

    ai "Hiroo, your mental state is unstable. Calm down and carefully find a way out of this situation."

    mc "The dinosaur is too big. In such a confined space, it can effortlessly crush the shit out of me."
    
    um "Billion years ago, the Dinosaurs on our home planet but they were all wiped out by a meteor."
    um "Us human stand no chance when it comes to the great forces in this universe. We are dusts inside a planet of the size of a dust in this universe."
    um "Humanity has progressed far enough into space with you as their representative. There is no greater glory in this."
    scene bg hallway with dissolve:
        xalign 1.0
        yalign 0.5
        zoom 1.8
    
    mc "Perhaps I will die today by a mystery that has not yet been solved by the human race, and tomorrow someone will honor me by solving the mystery."
    mc "When I think about it, my death isn’t at all meaningless."
    
    scene bg hallway:
        xalign 0.9
        yalign 0.6
        zoom 2.5
    show kq at center:
        yalign 0.9
        zoom 2.5
    with dissolve
    nn"And yet I find myself crawling into a dead end. I see the shadow of the behemoth towering above me."
    scene bg hallway:
        xalign 1.0
        yalign 0.3
        zoom 2.5
    show kq at center:
        xalign 0.8
        yalign 0.3
        zoom 2.5
    with dissolve
    nn"But when I see a broken wire coming out the wall, sparks flying, I look him in face and crack smile."

    mc "Bingo."
    
    scene bg white with dissolve
    um "I love the way you think, Hiroo. I still remember seeing those eyes in the Vietnam War, the eyes of a kamikaze."
    um "How many Vietnamese children strap bomb around themselves and bravely run toward the enemy base."

    mc "But I’m not all that brave, I didn’t fight on the frontline. I’m a coward who hides in his spaceship when a battle breaks out."

    um "But you are a kamikaze now. Bear that title proudly, suicider."
    
    scene bg hallway:
        xalign 0.9
        yalign 0.6
        zoom 2.5
    show kq at center:
        yalign 0.9
        zoom 2.5
    with dissolve
    nn"I grip the sparking wire and stick it to the dinosaur."

    mc "EAT THIS BIATCH!"
    
    play sound "sfx_fizzle.mp3"
    nn"But the dinosaur’s skin is too thick. The electricity has no effect."

    kq "Fool! Didst thou really think silly wires would hurt me?"

    mc "Dammit! Maybe if I can get to the engine room..."
    
    scene bg white with dissolve
    um "Ohohoho, making your own ship blows up."

    mc "Yeah old man, I always wondered what a sinking space ship looks like from the inside."

    um "If Vietnamese soldiers get to kamikaze with bombs that has the same destructive power as a space ship engine, maybe they won’t get to use as many soldiers."
    
    scene bg hallway with dissolve
    nn"I struggle to my feet. Hopefully I can make it to the engine room before the dinosaur catches on."
    
    show ai serious:
        yalign 0.0
        xalign 0.95
        zoom 0.4
    with dissolve
    ai "Why are you running toward the engine room? Are you planning to make this ship self-destruct? Don’t make such a selfish decision!"

    mc "Look, you stupid computer, I’m about to claim glory by killing a dinosaur and that isn’t something a robot like you can comprehend."
    
    hide ai with dissolve
    scene bg hallway with dissolve:
        xalign 1.0
        yalign 0.4
        zoom 1.8
    nn"I limp towards the engine room, somehow managing to outrun the dinosaur."

    scene bg engineroom with CropMove(0.5, "wiperight")
    
    nn"But just as I open the engine room door..."

    show kq at center:
        xalign 0.8
        yalign 0.3
        zoom 2.2
    with dissolve
    kq "I will end you before you can blow up the ship!"
    
    show kq at Shake((-0.4, 0.7, 0.5, 1.0), 1.0, dist=8)
    play sound "sfx_trex1.mp3"
    pause 1.5
    play sound2 "sfx_crash.mp3"
    scene bg black
    stop music fadeout 0.1
    pause 1.5
    nn"The dinosaur charges at me, flinging me towards the engine."
    play music "sfx_fireplace.mp3" fadein 0.5
    nn"I begin to melt from its searing heat."
    nn"First the flesh. Then the nerve and muscle tissue. Then my bones and internal organs."
    nn"The insides of my body drive the engine wild."
    nn"That should be enough to cause a nuclear explosion."
    nn"Before I lose the remaining life left in me, I hear her last words."

    show ai tearful at center:
        yalign 0.0
        zoom 0.4
    with dissolve
    ai "This is why I don’t understand humans..."
    stop music fadeout 1.0
    scene black with dissolve
    pause 1.0
    scene bg space with fade

    window show
    with dissolve
    play music "music_HexxitDRAVE.mp3"
    n "After the incident, Hiroo’s ship, the Kryptonite Phantom, was reported as missing to the general public."
    n "It wasn’t until several eons later that scientists managed to find and recover the AI’s data."
    n "Inside the hard drive, they discovered the records of Hiroo’s final moments fighting against Kanserous Quiboo and his heroic self-sacrifice."
    n "He was the only man to ever slay a dinosaur and save humanity."
    n "As word about his achievement spread, the name Hiroo Onoda the Dinosaur Slayer became renowned across the galaxy."
    nvl clear
    window hide
    with dissolve
    
    jump credits

#---------------------------- CREDITS ----------------------------#
#26/05/2015: Added credits, which should appear at all endings. Will probably make them nicer looking later.
label credits:
    window show
    with dissolve
    n "3D Graphics and Backgrounds by: Muggy Ate"
    n "Project Manager: Brandon Decena"
    n "2D Sprites by: Henri Dela Cruz"
    n "Writing by:"
    n "Austin Jamieson - Storyline and Common Route"
    n "Brandon Quan - Branching Routes and Miscellaneous Revisions"
    n "Minh Tran and Brandon Decena - Dinosaur Ending"
    n "Basic Programming by: Brandon Quan"
    n "Additional Programming by: Brandon Decena and Seilai Zhao"
    n "Music by: Peter Gresser, Kevin MacLeod, Frank Nora, and Johannes Schroll from FreePD.com"
    n "Sound Effects by: Mike Koenig, Matt Cutillo, Kibblesbob, Marianne Gagnon, Mark DiAngelo, and Public Domain from SoundBible.com"
    window hide
    with dissolve
    stop music fadeout 1.0
    scene bg black
    with fade
    pause 1.0
    
    return

# NOTE: THE BELOW LABEL IS TEMPORARY AND ONLY FOR THE DEMO.
label end_demo:
    nn"The end. Thanks for playing!"
    nn"You ended with [hero_pts] hero points."
    jump credits

#-------------------------------- FUNCTIONS -----------------------------------#

# Shake effect function from: http://www.renpy.org/wiki/renpy/doc/cookbook/Shake_effect
init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)