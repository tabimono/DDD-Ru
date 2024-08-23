screen kanata:
    tag menu

    add gui.kan_background


    vbox:
        xalign 0.97
        yalign 0.95

        spacing 5
        textbutton "RETURN" action Return()

    vbox:
        xalign 0.099
        yalign 0.228

        spacing 30
        textbutton "{i}Arika{/i}" action ShowMenu("arika")
        textbutton "{i}Kizaki{/i}" action ShowMenu("kizaki")

    vbox:
        xalign 0.099
        yalign 0.418

        spacing 30
        textbutton "{i}Fusou{/i}" action ShowMenu("fusou")
        textbutton "{i}Mato{/i}" action ShowMenu("mato")

    vbox:
        xalign 0.099
        yalign 0.662

        spacing 30
        textbutton "{i}Makina{/i}" action ShowMenu("makina")
        textbutton "{i}Kaie{/i}" action ShowMenu("kaie")
        textbutton "{i}Kanata{/i}" action ShowMenu("kanata")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
