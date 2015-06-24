from telex import plugin
from telex.callbacks.msgreceived import command, expand
        
class MyinfoPlugin(plugin.TelexPlugin):       
    @command('myinfo')
    @expand("^(\S+) (?P<cmd>\S+) (?P<set>\S+)")
    def Myinfo(self, cmd, set, *, bot, msg):
        cmd_list = ["Location", "Name"]
        if cmd in cmd_list:
            Myinfocb(cmd, set)
        response = ("Set "+cmd+" to "+set)
        self.respond_to_msg(msg,str(response))
    def Myinfocb(self, cmd, set)
        cmd(set)
        Return True
