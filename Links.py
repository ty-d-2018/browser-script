import json

def read_json_file(full_file_path):
    json_string = ""

    with open(full_file_path, 'r') as file:
        json_string = file.read()

    return json_string

def get_json_as_object(json_string):
    return json.loads(json_string)

class Link:
    def __init__(self, url):
        self.url = url
    
    def get_full_link(self):
        return self.url

class Template:
    def __init__(self, name):
        self.name = name
        self.key_link_numbers = []
    def set_key_link_numbers(self, keys):
        self.key_link_numbers = keys
    def get_key_link_numbers(self):
        return self.key_link_numbers

class LinkGroups:
    def __init__(self, name):
        self.name = name
        self.links = []
        self.templates = {}
    def add_template(self, new_template):
        self.templates[new_template.name] = new_template
    def get_template(self, key_name):
        return self.new_template[key_name]
    def choose_template_urls(self, key_name):
        template = self.get_template(key_name)
        self.urls = []
        for key_number in template.get_key_link_numbers:
            self.urls.append(self.links[key_number].get_full_link())
        
        return self.urls
    def set_links(self, links):
        self.links = links

def parse_json_object(json_object):
    groups = json_object["groups"]
    links = []
    link_groups = LinkGroups("")
    list_of_link_groups = []
    for key in groups.keys():
        link_groups = LinkGroups(key)
        for url in groups[key]["links"]:
            link = Link(url)
            links.append(link)
        link_groups.set_links(links)
        
        group_templates = groups[key]["sub_templates"]
        for temp_key in group_templates.keys():
            new_template = Template(temp_key)
            new_template.set_key_link_numbers(group_templates[temp_key])
            link_groups.add_template(new_template)
        
        list_of_link_groups.append(link_groups)

        links = []
    
    return list_of_link_groups

        
            