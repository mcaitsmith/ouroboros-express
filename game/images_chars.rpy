# Define images for character sprites.

label images_chars:

    # define silhouette images
    image ava silhouette = "images/characters/ava/ava silhouette.png"
    image darius silhouette = "images/characters/darius/darius silhouette.png"
    image susurha silhouette = "images/characters/susurha/susurha silhouette.png"

    # define expression VFX
    transform ex_neutral:
        zoom 1.0
    transform ex_neutral_blush:
        zoom 1.02
    transform ex_happy:
        zoom 1.02 yoffset 10
        linear 0.1 yoffset 0
        linear 0.2 yoffset 5
    transform ex_sad:
        zoom 1.02
        linear 0.5 yoffset 10
    transform ex_angry:
        zoom 1.02
        linear 0.1 xoffset -2
        linear 0.1 xoffset 2
        linear 0.1 xoffset -2
        linear 0.1 xoffset 2
    transform ex_surprised:
        zoom 1.02 yoffset 20
        linear 0.2 yoffset 0

    # define default fullbody status for each character
    define ava_fullbody = False
    define darius_fullbody = False
    define urshu_fullbody = False
    define susurha_fullbody = False
    define vivi_fullbody= False

    ### define NPC expression and blush layered images

    # AVA
    layeredimage ava neutral:
        at [sprite_highlight('ava'),ex_neutral]
        if ava_fullbody:
            'images/characters/ava/ava f_neutral.png'
        else:
            'images/characters/ava/ava_face_neutral.png'
    layeredimage ava neutral blush:
        at [sprite_highlight('ava'),ex_neutral_blush]
        if ava_fullbody:
            'images/characters/ava/ava f_neutral blush.png'
        else:
            'images/characters/ava/ava_face_neutral.png'
        if not ava_fullbody:
            'images/characters/ava/ava_overlay_blush.png'
    layeredimage ava happy:
        at [sprite_highlight('ava'),ex_happy]
        if ava_fullbody:
            'images/characters/ava/ava f_happy.png'
        else:
            'images/characters/ava/ava_face_happy.png'
    layeredimage ava happy blush:
        at [sprite_highlight('ava'),ex_happy]
        if ava_fullbody:
            'images/characters/ava/ava f_happy blush.png'
        else:
            'images/characters/ava/ava_face_happy.png'
        if not ava_fullbody:
            'images/characters/ava/ava_overlay_blush.png'
    layeredimage ava sad:
        at [sprite_highlight('ava'),ex_sad]
        if ava_fullbody:
            'images/characters/ava/ava f_sad.png'
        else:
            'images/characters/ava/ava_face_sad.png'
    layeredimage ava sad blush:
        at [sprite_highlight('ava'),ex_sad]
        if ava_fullbody:
            'images/characters/ava/ava f_sad blush.png'
        else:
            'images/characters/ava/ava_face_sad.png'
        if not ava_fullbody:
            'images/characters/ava/ava_overlay_blush.png'
    layeredimage ava angry:
        at [sprite_highlight('ava'),ex_angry]
        if ava_fullbody:
            'images/characters/ava/ava f_angry.png'
        else:
            'images/characters/ava/ava_face_angry.png'
    layeredimage ava angry blush:
        at [sprite_highlight('ava'),ex_angry]
        if ava_fullbody:
            'images/characters/ava/ava f_angry blush.png'
        else:
            'images/characters/ava/ava_face_angry.png'
        if not ava_fullbody:
            'images/characters/ava/ava_overlay_blush.png'
    layeredimage ava surprised:
        at [sprite_highlight('ava'),ex_surprised]
        if ava_fullbody:
            'images/characters/ava/ava f_surprised.png'
        else:
            'images/characters/ava/ava_face_surprised.png'
    layeredimage ava surprised blush:
        at [sprite_highlight('ava'),ex_surprised]
        if ava_fullbody:
            'images/characters/ava/ava f_surprised blush.png'
        else:
            'images/characters/ava/ava_face_surprised.png'
        if not ava_fullbody:
            'images/characters/ava/ava_overlay_blush.png'

    # DARIUS
    layeredimage darius neutral:
        at [sprite_highlight('darius'),ex_neutral]
        if darius_fullbody:
            'images/characters/darius/darius f_neutral.png'
        else:
            'images/characters/darius/darius_face_neutral.png'
    layeredimage darius neutral blush:
        at [sprite_highlight('darius'),ex_neutral_blush]
        if darius_fullbody:
            'images/characters/darius/darius f_neutral blush.png'
        else:
            'images/characters/darius/darius_face_neutral.png'
        if not darius_fullbody:
            'images/characters/darius/darius_overlay_blush.png'
    layeredimage darius happy:
        at [sprite_highlight('darius'),ex_happy]
        if darius_fullbody:
            'images/characters/darius/darius f_happy.png'
        else:
            'images/characters/darius/darius_face_happy.png'
    layeredimage darius happy blush:
        at [sprite_highlight('darius'),ex_happy]
        if darius_fullbody:
            'images/characters/darius/darius f_happy blush.png'
        else:
            'images/characters/darius/darius_face_happy.png'
        if not darius_fullbody:
            'images/characters/darius/darius_overlay_blush.png'
    layeredimage darius sad:
        at [sprite_highlight('darius'),ex_sad]
        if darius_fullbody:
            'images/characters/darius/darius f_sad.png'
        else:
            'images/characters/darius/darius_face_sad.png'
    layeredimage darius sad blush:
        at [sprite_highlight('darius'),ex_sad]
        if darius_fullbody:
            'images/characters/darius/darius f_sad blush.png'
        else:
            'images/characters/darius/darius_face_sad.png'
        if not darius_fullbody:
            'images/characters/darius/darius_overlay_blush.png'
    layeredimage darius angry:
        at [sprite_highlight('darius'),ex_angry]
        if darius_fullbody:
            'images/characters/darius/darius f_angry.png'
        else:
            'images/characters/darius/darius_face_angry.png'
    layeredimage darius angry blush:
        at [sprite_highlight('darius'),ex_angry]
        if darius_fullbody:
            'images/characters/darius/darius f_angry blush.png'
        else:
            'images/characters/darius/darius_face_angry.png'
        if not darius_fullbody:
            'images/characters/darius/darius_overlay_blush.png'
    layeredimage darius surprised:
        at [sprite_highlight('darius'),ex_surprised]
        if darius_fullbody:
            'images/characters/darius/darius f_surprised.png'
        else:
            'images/characters/darius/darius_face_surprised.png'
    layeredimage darius surprised blush:
        at [sprite_highlight('darius'),ex_surprised]
        if darius_fullbody:
            'images/characters/darius/darius f_surprised blush.png'
        else:
            'images/characters/darius/darius_face_surprised.png'
        if not darius_fullbody:
            'images/characters/darius/darius_overlay_blush.png'

    # SUSURHA
    layeredimage susurha neutral:
        at [sprite_highlight('susurha'),ex_neutral]
        if susurha_fullbody:
            'images/characters/susurha/susurha f_neutral.png'
        else:
            'images/characters/susurha/susurha_face_neutral.png'
    layeredimage susurha neutral blush:
        at [sprite_highlight('susurha'),ex_neutral_blush]
        if susurha_fullbody:
            'images/characters/susurha/susurha f_neutral blush.png'
        else:
            'images/characters/susurha/susurha_face_neutral.png'
        if not susurha_fullbody:
            'images/characters/susurha/susurha_overlay_blush.png'
    layeredimage susurha happy:
        at [sprite_highlight('susurha'),ex_happy]
        if susurha_fullbody:
            'images/characters/susurha/susurha f_happy.png'
        else:
            'images/characters/susurha/susurha_face_happy.png'
    layeredimage susurha happy blush:
        at [sprite_highlight('susurha'),ex_happy]
        if susurha_fullbody:
            'images/characters/susurha/susurha f_happy blush.png'
        else:
            'images/characters/susurha/susurha_face_happy.png'
        if not susurha_fullbody:
            'images/characters/susurha/susurha_overlay_blush.png'
    layeredimage susurha sad:
        at [sprite_highlight('susurha'),ex_sad]
        if susurha_fullbody:
            'images/characters/susurha/susurha f_sad.png'
        else:
            'images/characters/susurha/susurha_face_sad.png'
    layeredimage susurha sad blush:
        at [sprite_highlight('susurha'),ex_sad]
        if susurha_fullbody:
            'images/characters/susurha/susurha f_sad blush.png'
        else:
            'images/characters/susurha/susurha_face_sad.png'
        if not susurha_fullbody:
            'images/characters/susurha/susurha_overlay_blush.png'
    layeredimage susurha angry:
        at [sprite_highlight('susurha'),ex_angry]
        if susurha_fullbody:
            'images/characters/susurha/susurha f_angry.png'
        else:
            'images/characters/susurha/susurha_face_angry.png'
    layeredimage susurha angry blush:
        at [sprite_highlight('susurha'),ex_angry]
        if susurha_fullbody:
            'images/characters/susurha/susurha f_angry blush.png'
        else:
            'images/characters/susurha/susurha_face_angry.png'
        if not susurha_fullbody:
            'images/characters/susurha/susurha_overlay_blush.png'
    layeredimage susurha surprised:
        at [sprite_highlight('susurha'),ex_surprised]
        if susurha_fullbody:
            'images/characters/susurha/susurha f_surprised.png'
        else:
            'images/characters/susurha/susurha_face_surprised.png'
    layeredimage susurha surprised blush:
        at [sprite_highlight('susurha'),ex_surprised]
        if susurha_fullbody:
            'images/characters/susurha/susurha f_surprised blush.png'
        else:
            'images/characters/susurha/susurha_face_surprised.png'
        if not susurha_fullbody:
            'images/characters/susurha/susurha_overlay_blush.png'

    # URSHU
    layeredimage urshu neutral:
        at [sprite_highlight('urshu'),ex_neutral]
        if urshu_fullbody:
            'images/characters/urshu/urshu f_neutral.png'
        else:
            'images/characters/urshu/urshu_face_neutral.png'
    layeredimage urshu neutral blush:
        at [sprite_highlight('urshu'),ex_neutral_blush]
        if urshu_fullbody:
            'images/characters/urshu/urshu f_neutral blush.png'
        else:
            'images/characters/urshu/urshu_face_neutral.png'
        if not urshu_fullbody:
            'images/characters/urshu/urshu_overlay_blush.png'
    layeredimage urshu happy:
        at [sprite_highlight('urshu'),ex_happy]
        if urshu_fullbody:
            'images/characters/urshu/urshu f_happy.png'
        else:
            'images/characters/urshu/urshu_face_happy.png'
    layeredimage urshu happy blush:
        at [sprite_highlight('urshu'),ex_happy]
        if urshu_fullbody:
            'images/characters/urshu/urshu f_happy blush.png'
        else:
            'images/characters/urshu/urshu_face_happy.png'
        if not urshu_fullbody:
            'images/characters/urshu/urshu_overlay_blush.png'
    layeredimage urshu sad:
        at [sprite_highlight('urshu'),ex_sad]
        if urshu_fullbody:
            'images/characters/urshu/urshu f_sad.png'
        else:
            'images/characters/urshu/urshu_face_sad.png'
    layeredimage urshu sad blush:
        at [sprite_highlight('urshu'),ex_sad]
        if urshu_fullbody:
            'images/characters/urshu/urshu f_sad blush.png'
        else:
            'images/characters/urshu/urshu_face_sad.png'
        if not urshu_fullbody:
            'images/characters/urshu/urshu_overlay_blush.png'
    layeredimage urshu angry:
        at [sprite_highlight('urshu'),ex_angry]
        if urshu_fullbody:
            'images/characters/urshu/urshu f_angry.png'
        else:
            'images/characters/urshu/urshu_face_angry.png'
    layeredimage urshu angry blush:
        at [sprite_highlight('urshu'),ex_angry]
        if urshu_fullbody:
            'images/characters/urshu/urshu f_angry blush.png'
        else:
            'images/characters/urshu/urshu_face_angry.png'
        if not urshu_fullbody:
            'images/characters/urshu/urshu_overlay_blush.png'
    layeredimage urshu surprised:
        at [sprite_highlight('urshu'),ex_surprised]
        if urshu_fullbody:
            'images/characters/urshu/urshu f_surprised.png'
        else:
            'images/characters/urshu/urshu_face_surprised.png'
    layeredimage urshu surprised blush:
        at [sprite_highlight('urshu'),ex_surprised]
        if urshu_fullbody:
            'images/characters/urshu/urshu f_surprised blush.png'
        else:
            'images/characters/urshu/urshu_face_surprised.png'
        if not urshu_fullbody:
            'images/characters/urshu/urshu_overlay_blush.png'

    # define vivi sprite images
    init python:
        def vivi_return_image(expression):
            if vivi_fullbody:
                return 'images/characters/vivi/vivi f_'+expression+'.png'
            else:
                return 'images/characters/vivi/vivi '+expression+'.png'
    image vivi neutral:
        At(vivi_return_image('neutral'), sprite_highlight('vivi'))
        zoom 1.0
    image vivi happy:
        At(vivi_return_image('happy'), sprite_highlight('vivi'))
        zoom 1.01 yoffset 10
        linear 0.1 yoffset 0
        linear 0.2 yoffset 5
    image vivi sad:
        At(vivi_return_image('sad'), sprite_highlight('vivi'))
        zoom 1.01
        linear 0.5 yoffset 10
    image vivi angry:
        At(vivi_return_image('angry'), sprite_highlight('vivi'))
        zoom 1.01
        linear 0.1 xoffset -2
        linear 0.1 xoffset 2
        linear 0.1 xoffset -2
        linear 0.1 xoffset 2
    image vivi surprised:
        At(vivi_return_image('surprised'), sprite_highlight('vivi'))
        zoom 1.01 yoffset 20
        linear 0.2 yoffset 0
    image vivi neutral blush:
        At(vivi_return_image('neutral blush'), sprite_highlight('vivi'))
        zoom 1.01
    image vivi happy blush:
        At(vivi_return_image('happy blush'), sprite_highlight('vivi'))
        zoom 1.01 yoffset 10
        linear 0.1 yoffset 0
        linear 0.2 yoffset 5
    image vivi sad blush:
        At(vivi_return_image('sad blush'), sprite_highlight('vivi'))
        zoom 1.01
        linear 0.5 yoffset 10
    image vivi angry blush:
        At(vivi_return_image('angry blush'), sprite_highlight('vivi'))
        zoom 1.01
        linear 0.1 xoffset -2
        linear 0.1 xoffset 2
        linear 0.1 xoffset -2
        linear 0.1 xoffset 2
    image vivi surprised blush:
        At(vivi_return_image('surprised blush'), sprite_highlight('vivi'))
        zoom 1.01 yoffset 20
        linear 0.2 yoffset 0
    image vivi floating_surprised = At('images/characters/vivi/vivi_floating/vivi floating_surprised.png', sprite_highlight('vivi'))
    image vivi floating_surprised blush = At('images/characters/vivi/vivi_floating/vivi floating_surprised blush.png', sprite_highlight('vivi'))
    image vivi floating_happy = At('images/characters/vivi/vivi_floating/vivi floating_happy.png', sprite_highlight('vivi'))
    image vivi floating_happy blush = At('images/characters/vivi/vivi_floating/vivi floating_happy blush.png', sprite_highlight('vivi'))
    image vivi floating_angry = At('images/characters/vivi/vivi_floating/vivi floating_angry.png', sprite_highlight('vivi'))
    image vivi floating_angry blush = At('images/characters/vivi/vivi_floating/vivi floating_angry blush.png', sprite_highlight('vivi'))
    image vivi floating_sad = At('images/characters/vivi/vivi_floating/vivi floating_sad.png', sprite_highlight('vivi'))
    image vivi floating_sad blush = At('images/characters/vivi/vivi_floating/vivi floating_sad blush.png', sprite_highlight('vivi'))
    image vivi floating_neutral = At('images/characters/vivi/vivi_floating/vivi floating_neutral.png', sprite_highlight('vivi'))
    image vivi floating_neutral blush = At('images/characters/vivi/vivi_floating/vivi floating_neutral blush.png', sprite_highlight('vivi'))
    image vivi jump_surprised = At('images/characters/vivi/vivi_jump/vivi j_surprised.png', sprite_highlight('vivi'))
    image vivi_conductor neutral:
        At('images/characters/vivi/vivi_conductor/vivi_conductor neutral.png', sprite_highlight('vivi'))
        zoom 1.0
    image vivi_conductor happy:
        At('images/characters/vivi/vivi_conductor/vivi_conductor happy.png', sprite_highlight('vivi'))
        zoom 1.01 yoffset 10
        linear 0.1 yoffset 0
        linear 0.2 yoffset 5
    image vivi_conductor surprised:
        At('images/characters/vivi/vivi_conductor/vivi_conductor surprised.png', sprite_highlight('vivi'))
        zoom 1.01 yoffset 20
        linear 0.2 yoffset 0

    # define urshu dining images
    image urshudining neutral = At('images/characters/urshu/urshu dining/urshu_neutral_table.png', sprite_highlight('urshudining'))
    image urshudining happy = At('images/characters/urshu/urshu dining/urshu_happy_table.png', sprite_highlight('urshudining'))
    image urshudining sad = At('images/characters/urshu/urshu dining/urshu_sad_table.png', sprite_highlight('urshudining'))
    image urshudining angry = At('images/characters/urshu/urshu dining/urshu_angry_table.png', sprite_highlight('urshudining'))
    image urshudining surprised = At('images/characters/urshu/urshu dining/urshu_surprised_table.png', sprite_highlight('urshudining'))
    image urshudining neutral blush = At('images/characters/urshu/urshu dining/urshu_neutral_table_blush.png', sprite_highlight('urshudining'))
    image urshudining happy blush = At('images/characters/urshu/urshu dining/urshu_happy_table_blush.png', sprite_highlight('urshudining'))
    image urshudining sad blush = At('images/characters/urshu/urshu dining/urshu_sad_table_blush.png', sprite_highlight('urshudining'))
    image urshudining angry blush = At('images/characters/urshu/urshu dining/urshu_angry_table_blush.png', sprite_highlight('urshudining'))
    image urshudining surprised blush = At('images/characters/urshu/urshu dining/urshu_surprised_table_blush.png', sprite_highlight('urshudining'))


    return
