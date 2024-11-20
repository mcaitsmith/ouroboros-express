label depression_asha_susurha:

    #LOCATION: lounge
    # call check_overlay from _call_check_overlay_24
    scene lounge with fade
    play ambience amb_lounge if_changed fadein 1.0
    $ susurha_fullbody = True
    $ ava_fullbody = True
    #SOUND: train
    pause 1.0
    play sound trainwhistle volume 0.5
    pause 5.0

    show vivi neutral at left : 
        xzoom -1

    vivi neutral "What's the commotion I'm hearing?"
    play music spymusic loop

    # hide vivi

    show ava neutral at right
    show susurha neutral at center :
        xzoom -1

    vivithinking "Oh! It's them! Don't want to interrupt."

    ava angry "You jest? Support the aristocrats? We did no such thing, druid. Those feckless, inbred royals knew nothing of statecraft, diplomacy, or sacrifice. We reviled them."

    susurha "Oh? And who taught you such things? The goddess you bear the name of?"

    ava angry "...No one. Certainly not the royals. We bore what we had to, learning from our instructors, looking ever forward towards a burgeoning sunrise. Alone."

    susurha sad "I merely ask, why do all of this to yourself when such disdain sings from your voice?"

    ava sad "Do this? We were offered no choice, Druid."

    susurha sad "Before you were an avatar, you were you, no?"

    ava angry "No! We have always been the Avatar of Asha, anointed at birth. We serve the goddess, our people, our planet. We know naught else of ourselves."

    susurha sad "Why not just run away? Stop them from keeping you in such suffocating chains?"

    ava angry "No Avatar ever had the luxury to abandon those who depend on us. Nor would we. The All is the One."

    ava neutral "You think yourself superior, Druid? That you are without shame? The shame of abandoning your people, religion, and yourself? You will never wash that stain away."

    susurha sad "..."

    susurha sad "Suppose I never will."

    susurha sad "That’s why we’re all here."

    ava sad "No, Druid. I am here because my people have sacrificed me. You sacrificed your family for your libidinous freedom. Your stain is indelible and brightened by shame."

    susurha angry "I’ve sacrificed no one, angel! I actively refused to."

    ava neutral "Of course. You know nothing of sacrifice. Only hedonistic delight in the pursuit of pleasure."

    susurha angry "Don’t lash out at me for trying what you haven’t dreamt of."

    ava sad "You speak to one who knows nothing of freedom or dreams. Those were for the aristocrats. Like you."
    stop music fadeout 5.0

    ava sad "..."

    susurha sad "..."

    hide susurha
    hide ava

    show vivi sad at left :
        xzoom -1

    vivithinking "This silence is killing me. I should leave."
    stop ambience fadeout 1.0

#JUMP TO Character Selector 2
    jump depression_cs2
