from random import randint
from telex import plugin
from telex.callbacks.msgreceived import command, expand
        
class RollPlugin(plugin.TelexPlugin):       
    @command('roll')
    @expand("^(\S+ ?(?P<dice>\d+)?d?(?P<sides>\d+)?)")
    def test_callback(self, dice, sides, *, bot, msg):
        if dice:
            dice = 10 if int(dice) > 10 else int(dice)
            sides = 100 if int(sides) > 100 else int(sides)
            dicelist = [randint(0,sides) for x in range(dice)]
            totalroll = sum(dicelist)
            self.respond_to_msg(msg,"You rolled "+str(dice)+" dice with "+str(sides)+" sides.\nResults: "+str(dicelist)+"\nTotal: "+str(totalroll)+".")
        if not dice:
            dice = 1
            sides = 100   
            self.respond_to_msg(msg,"You rolled "+str(randint(0,sides))+".")
