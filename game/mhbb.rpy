screen mhbg:
    tag menu

    if persistent.mkhs == True:
        add gui.mhbb_background
    else:
        add gui.generic_background

    vbox:
        xalign 0.975
        yalign 0.93

        spacing 5
        textbutton "RETURN" action Return()


    imagebutton auto "gui/gal%s.png" xpos 1819 ypos 445 action ShowMenu("mybg")
    imagebutton auto "gui/galo%s.png" xpos 19 ypos 445 action ShowMenu("njbg")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
