import random
from telex import plugin
from telex.callbacks.msgreceived import command, expand
        
class RollPlugin(plugin.TelexPlugin):
    def __init__(self):
        self.well_fed = True

    @command('botsnack')
    @expand("^(\S+)")
    def feeding(self, *, bot, msg):
        response = ["Yum","Tasty"]
        if self.well_fed:
           self.respond_to_msg(msg,(random.choice(response)))
           self.well_fed = False
