import pip

class PyManager(object):

    def install(self, package, *args):
        pip.main(['install', package, *args])
    
    def install_list(self, package_list):
        for package_item in package_list:
            package = package_item.get('name')
            version = package_item.get('version')
            git = package_item.get('git')
            if package:
                if git:
                    self.install('git+{}'.format(package))
                elif version:           
                    self.install('{}=={}'.format(package, version))
                else:
                    self.install('{}'.format(package), '-U')                                        