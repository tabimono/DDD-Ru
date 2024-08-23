screen gallerythree:
    tag menu

    add gui.gallthree_background


    vbox:
        xalign 0.975
        yalign 0.93

        spacing 5
        textbutton "RETURN" action Return()

    imagebutton auto "gui/galo%s.png" xpos 19 ypos 445 action ShowMenu("gallerytwo")

    imagebutton auto "gui/gal%s.png" xpos 1819 ypos 445 action ShowMenu("gallery")

    if persistent.tvcg == True:
        imagebutton auto "images/bg/romalone_1_50%s.png" xpos 66 ypos 74 action ShowMenu("routvcg")

    if persistent.sscg == True:
        imagebutton auto "images/bg/balconly_42%s.png" xpos 682 ypos 74 action ShowMenu("rousscg")

    if persistent.kacg == True:
        imagebutton auto "images/bg/kanatlone_42%s.png" xpos 1298 ypos 74 action ShowMenu("roukacg")

    if persistent.tvcg == True:
        imagebutton auto "images/bg/cgone_%s.png" xpos 56 ypos 573 action ShowMenu("fintvcg")

    if persistent.sscg == True:
        imagebutton auto "images/bg/cgtwo_%s.png" xpos 672 ypos 573 action ShowMenu("finsscg")

    if persistent.kacg == True:
        imagebutton auto "images/bg/cgthree_%s.png" xpos 1285 ypos 573 action ShowMenu("finkacg")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
