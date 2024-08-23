screen arhos:
    tag menu

    if persistent.arikahosgal == True:
        add gui.arhos_background
    else:
        add gui.generic_background

    vbox:
        xalign 0.975
        yalign 0.93

        spacing 5
        textbutton "RETURN" action Return()


    imagebutton auto "gui/gal%s.png" xpos 1819 ypos 445 action ShowMenu("kdbg")
    imagebutton auto "gui/galo%s.png" xpos 19 ypos 445 action ShowMenu("dlbg")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
