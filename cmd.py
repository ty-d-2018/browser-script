import Links

def setup_link_groups(full_file_path):
    json_string = Links.read_json_file(full_file_path)
    json_object = Links.get_json_as_object(json_string)
    
    list_of_link_groups = Links.parse_json_object(json_object)

    return list_of_link_groups

def run():
    list_of_link_groups = setup_link_groups("example.json")
    print("Hello James!")

run()