screen routvcg:
    tag menu

    add gui.routvcg_background


    vbox:
        xalign 0.975
        yalign 0.93

        spacing 5
        textbutton "RETURN" action Return()

    imagebutton auto "gui/galo%s.png" xpos 19 ypos 445 action ShowMenu("finkacg")
    imagebutton auto "gui/gal%s.png" xpos 1819 ypos 445 action ShowMenu("fintvcg")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
