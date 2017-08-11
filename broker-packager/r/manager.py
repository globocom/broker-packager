import rpy2.robjects.packages as rpackages

class RManager(object):

    def __init__(self):
        self.devtools = rpackages.importr('devtools')
        self.utils = rpackages.importr("utils")
    
    def install_version(self, package, version):
        self.devtools.install_version(package, version=version)
    
    def install(self, package):
        self.utils.install_packages(package)
    
    def install_git(self, repo):
        self.devtools.install_git(repo)
    
    def install_list(self, package_list):
        for package_item in package_list:
            package = package_item.get('name')
            version = package_item.get('version')
            git = package_item.get('git')
            if package:
                if git:
                    self.install_git(package)
                elif version:
                    self.install_version(package, version)                    
                else:
                    self.install(package)