import subprocess
import Links
import sys
import argparse

class BrowserCommand:
    def __init__(self, full_file_path):
        self.cmd = "brave-browser"
        self.parameters = ["--new-window"]
        self.link_groups = []
        self.arg_parser = argparse.ArgumentParser()
        self.parameter_options = None

        self.init_arg_parser()
        self.get_args()
        self.setup_link_groups(full_file_path)

    def setup_link_groups(self, full_file_path):
        json_string = Links.read_json_file(full_file_path)
        json_object = Links.get_json_as_object(json_string)
        
        list_of_link_groups = Links.parse_json_object(json_object)

        self.link_groups = list_of_link_groups

    def init_arg_parser(self):
        self.arg_parser.add_argument('--group', required=True)
        self.arg_parser.add_argument('--template', required=True)

    def get_args(self):
        self.parameter_options = self.arg_parser.parse_args(sys.argv[1:])
    
    
    
    def get_command(self):
        bash_commands = [self.cmd]
        for parameter in self.parameters:
            bash_commands.append(parameter)
        group = self.parameter_options.group
        template = self.parameter_options.template
        links = []
        for l_group in self.link_groups:
            if group == l_group.name:
                if template in l_group.templates:
                    links = l_group.choose_template_urls(template)
                    break
        
        for link in links:
            bash_commands.append(link)
        
        ##print(bash_commands)
        subprocess.run(bash_commands)