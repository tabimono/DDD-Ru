













define config.name = _("DDD_UNC")





define gui.show_name = False




define config.version = "1.0"





define gui.about = _p("""
""")






define build.name = "DDD_UNC"








define config.has_sound = True
define config.has_music = True
define config.has_voice = True













define config.main_menu_music = "audio/Nctrnm - Concern.mp3"

define config.mouse = { 'default' : [('gui/dot.png', 0, 0)]}










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None

define config.default_text_cps = 50














define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 50





default preferences.afm_time = 4
















define config.save_directory = "DDD-1664308705"






define config.window_icon = "gui/window_icon.png"

define config.default_fullscreen = True






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)









    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
