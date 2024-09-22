import subprocess
import Links
import sys

class BrowserCommand:
    def __init__(self):
        self.cmd = "brave-browser"
        self.parameters = ["--new-window"]
        self.link_groups = []

    def setup_link_groups(self):
        json_string = Links.read_json_file(full_file_path)
        json_object = Links.get_json_as_object(json_string)
        
        list_of_link_groups = Links.parse_json_object(json_object)

        self.link_groups = list_of_link_groups

    def get_args(self):
        for i in range(1, len(sys.argv)):
            print(sys.argv[i])
    
    def get_command(self):
        bash_commands = [self.cmd, self.parameters]
        for link in self.get_links():
            bash_commands.append(link)
        
        subprocess.run(bash_commands)