from python.manager import PyManager
from r.manager import RManager

class Installer(object):
    def __init__(self):
        self.managers = {'python': PyManager(), 'r': RManager()}

    def install(self, config):
        for manager_name in self.managers:
            manager = self.managers[manager_name]
            manager.install_list(config.get(manager_name, []))