screen gallery:
    tag menu

    add gui.gall_background


    vbox:
        xalign 0.975
        yalign 0.93

        spacing 5
        textbutton "RETURN" action Return()

    imagebutton auto "gui/gal%s.png" xpos 1819 ypos 445 action ShowMenu("gallerytwo")

    imagebutton auto "gui/galo%s.png" xpos 19 ypos 445 action ShowMenu("gallerythree")

    if persistent.yungkan == True:
        imagebutton auto "images/bg/smallkat%s.png" xpos 96 ypos 72 action ShowMenu("kobg")

    if persistent.ykth == True:
        imagebutton auto "images/bg/fusou%s.png" xpos 322 ypos 20 action ShowMenu("ytbg")

    if persistent.kzat == True:
        imagebutton auto "images/bg/kizaki%s.png" xpos 590 ypos 50 action ShowMenu("kzbg")

    if persistent.tsur == True:
        imagebutton auto "images/bg/tsur%s.png" xpos 1120 ypos 50 action ShowMenu("tsbg")

    if persistent.ykft == True:
        imagebutton auto "images/bg/lfus%s.png" xpos 1645 ypos 50 action ShowMenu("yfbg")

    if persistent.dcdl == True:
        imagebutton auto "images/bg/doc%s.png" xpos 337 ypos 386 action ShowMenu("dlbg")

    if persistent.arikahosgal == True:
        imagebutton auto "images/bg/arikagalbut_%s.png" xpos 610 ypos 374 action ShowMenu("arhos")

    if persistent.knta == True:
        imagebutton auto "images/bg/okan%s.png" xpos 870 ypos 386 action ShowMenu("kdbg")

    if persistent.niij == True:
        imagebutton auto "images/bg/niij%s.png" xpos 1110 ypos 386 action ShowMenu("njbg")

    if persistent.mkhs == True:
        imagebutton auto "images/bg/mkhs%s.png" xpos 1370 ypos 386 action ShowMenu("mhbg")

    if persistent.myyo == True:
        imagebutton auto "images/bg/myyo%s.png" xpos 337 ypos 708 action ShowMenu("mybg")

    if persistent.mkst == True:
        imagebutton auto "images/bg/mkst%s.png" xpos 594 ypos 739 action ShowMenu("mrbg")

    if persistent.msmi == True:
        imagebutton auto "images/bg/msmi%s.png" xpos 852 ypos 739 action ShowMenu("msbg")

    if persistent.kiri == True:
        imagebutton auto "images/bg/kiri%s.png" xpos 1116 ypos 722 action ShowMenu("krbg")

    if persistent.arikabb == True:
        imagebutton auto "images/bg/arikabb%s.png" xpos 1387 ypos 726 action ShowMenu("arbb")

    if persistent.mato == True:
        imagebutton auto "images/bg/mato%s.png" xpos 1377 ypos 50 action ShowMenu("mtbg")

    if persistent.kaie == True:
        imagebutton auto "images/bg/kaie%s.png" xpos 867 ypos 105 action ShowMenu("kibg")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
