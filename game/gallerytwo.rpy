screen gallerytwo:
    tag menu

    add gui.galltwo_background


    vbox:
        xalign 0.975
        yalign 0.93

        spacing 5
        textbutton "RETURN" action Return()

    imagebutton auto "gui/galo%s.png" xpos 19 ypos 445 action ShowMenu("gallery")

    imagebutton auto "gui/gal%s.png" xpos 1819 ypos 445 action ShowMenu("gallerythree")

    imagebutton auto "images/bg/Bismark-1_1_35%s.png" xpos 1010 ypos 242 action ShowMenu("covfin")

    imagebutton auto "images/bg/cogv%s.png" xpos 223 ypos 242 action ShowMenu("covrou")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
