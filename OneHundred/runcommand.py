#!/usr/bin/env python
import subprocess

__author__ = 'RongbingMiao'

class RunCmd(object):
    def cmd_run(self,cmd):
        self.cmd = cmd
        subprocess.call(self.cmd, shell=True)


a = RunCmd()
a.cmd_run('ifconfig -a')