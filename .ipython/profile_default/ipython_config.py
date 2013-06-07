# Configuration file for ipython.

c = get_config()

c.InteractiveShell.autoindent = True
c.InteractiveShell.confirm_exit = False
c.TerminalIPythonApp.display_banner = False
c.InteractiveShell.colors = 'Linux'
c.InteractiveShell.editor = 'subl -n -w'

c.PromptManager.in_template = '[\#] >>> '
c.PromptManager.in2_template = '   .\D.: '
c.PromptManager.out_template = '[\#]   : '
c.PromptManager.justify = True

# Logging
import os
import time

logdir = os.path.expanduser(time.strftime("~/Dropbox/history/ipython/%Y/%m/"))
logfile = os.path.join(logdir, time.strftime("%d.log"))
if not os.path.exists(logdir):
    os.makedirs(logdir)
c.InteractiveShellApp.exec_lines = ["%%logstart %s append" % logfile]
