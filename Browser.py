import subprocess

class BrowserCommand:
    def __init__(self):
        self.cmd = "brave-browser"
        self.parameters = ["--new-window"]
        self.config_groups = []

    def add_link(self, link_full_url):
        self.links.append(link_full_url)
    def set_links(self, links):
        self.links = links
    def get_links(self):
        return self.links
    def set_config_groups(self, link_groups):
        self.config_groups = link_groups
    
    def get_command(self):
        bash_commands = [self.cmd, self.parameters]
        for link in self.get_links():
            bash_commands.append(link)
        
        subprocess.run(bash_commands)