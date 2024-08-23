screen arbb:
    tag menu

    if persistent.arikabb == True:
        add gui.arbb_background
    else:
        add gui.generic_background


    vbox:
        xalign 0.975
        yalign 0.93

        spacing 5
        textbutton "RETURN" action Return()


    imagebutton auto "gui/gal%s.png" xpos 1819 ypos 445 action ShowMenu("kobg")
    imagebutton auto "gui/galo%s.png" xpos 19 ypos 445 action ShowMenu("krbg")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
