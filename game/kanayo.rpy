screen kobg:
    tag menu

    add gui.kobb_background


    vbox:
        xalign 0.975
        yalign 0.93

        spacing 5
        textbutton "RETURN" action Return()


    imagebutton auto "gui/gal%s.png" xpos 1819 ypos 445 action ShowMenu("ytbg")
    imagebutton auto "gui/galo%s.png" xpos 19 ypos 445 action ShowMenu("arbb")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
