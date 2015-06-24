from telex import plugin
from telex.callbacks.msgreceived import command, expand
        
class MyinfoPlugin(plugin.TelexPlugin):       
    @command('myinfo')
    @expand("^(\S+)")
    def test_callback(self, *, bot, msg):
        response = "blah"
        self.respond_to_msg(msg,response)
