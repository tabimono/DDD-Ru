screen roukacg:
    tag menu

    if persistent.kacg == True:
        add gui.roukacg_background
    else:
        add gui.genericcg_background


    vbox:
        xalign 0.975
        yalign 0.93

        spacing 5
        textbutton "RETURN" action Return()

    imagebutton auto "gui/galo%s.png" xpos 19 ypos 445 action ShowMenu("finsscg")
    imagebutton auto "gui/gal%s.png" xpos 1819 ypos 445 action ShowMenu("finkacg")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
