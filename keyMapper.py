import os
import sys
import time
import json
import yaml
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('JsonFile', help= "Json File to read key from.")
parser.add_argument('YamlFile', help= "Yaml File to read key from.")
parser.add_argument('MappingFile', help= "Text File to read Key Mapping from.")
args = parser.parse_args()

with open(args.JsonFile, 'r+') as fileJson:
    print("Reading Json File...")
    json_data = json.loads(fileJson.read())
    time.sleep(1)

with open(args.YamlFile, 'r+') as fileYaml:
    print("Reading Yaml File...")
    yaml_data = yaml.load(fileYaml, Loader= yaml.FullLoader)
    time.sleep(1)

def key_search(key_list, file_dict):
    """
    key_search performs efficient search in dictionaries to search for given key : value pairs.

    Arguments:
        key_list {list} -- Arguments takes a list of keywords to search.
        file_dict {dict} -- Argument takes a dictionary to search keywords in it.

    Returns:
        result_dict -- Returns selected key:value pair mapping in file_dict.
    """

    # TODO: Functionality to process Json file directly to be added.
    result_dict = {}

    # * Remove input descripencies
    if type(key_list) != type([]):
        key_list = [key_list]
    
    if type(file_dict) == type(dict()):
        for key in key_list:
            if key in file_dict.keys():
                result_dict[key] = file_dict[key]
                
            elif len(file_dict.keys()) > 0:
                for key in file_dict.keys():
                    result = key_search(key, file_dict[key])
                    if result:
                        for k, v in result.items():
                            result_dict[k] = v

    
    elif type(file_dict) == type([]):
        for node in file_dict:
            result = key_search(key_list, node)
            if result:
                for k, v in result.items():
                    result_dict[k] = v
    
    return result_dict

with open(args.MappingFile, 'r+') as txt_file:
    print("Reading Mapping File... ")
    time.sleep(1)
    print("Begining Value Matching\n")

    for line in txt_file:
        line = str(line)
        line1, line2 = line.split(" : ", maxsplit= 2)
        line2 = line2.rstrip()
        time.sleep(2)

        type(line1)
        print("________________________________________________________\n")
        print(" Json Mapping : %s, and Yaml Mapping : %s "
                    % (key_search([line1], json_data).get(line1), 
                            key_search([line2], yaml_data).get(line2)))


        # TODO : Uncomment line 77 : 79 to enable Pretty print of output. 
        # *print("\033[0;33;40m Json Mapping : %s, and Yaml Mapping : %s \033[0m"
        # *            % (key_search([line1], json_data).get(line1), 
        # *                    key_search([line2], yaml_data).get(line2)))


        if (key_search([line1], json_data).get(line1)) is (key_search([line2], yaml_data).get(line2)) : 
            print(" String Match \n")
            # *Print Pretty
            # *print("\033[1;32;40m String Match \033[0m \n")

        else:
            print(" String Mismatch \n")
            # *Print Pretty
            # *print("\033[1;49;31;40m String Mismatch \033[0m \n")
