import random
from telex import plugin
from telex.callbacks.msgreceived import command, expand
        
class RollPlugin(plugin.TelexPlugin):       
    @command('botsnack')
    @expand("^(\S+)")
    def feeding(self, *, bot, msg):
        response = ["Yum","Tasty"]
        self.respond_to_msg(msg,(random.choice(response)))
