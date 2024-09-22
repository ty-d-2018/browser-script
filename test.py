import Links

def setup_link_groups(full_file_path):
    json_string = Links.read_json_file(full_file_path)
    json_object = Links.get_json_as_object(json_string)
    
    list_of_link_groups = Links.parse_json_object(json_object)

    return list_of_link_groups

def test():
    list_of_link_groups = setup_link_groups("example.json")

    templates = list_of_link_groups[0].templates

    for t_key in templates.keys():
        temp = templates[t_key]
        print(temp.name)