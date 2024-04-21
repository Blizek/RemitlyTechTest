import json
import sys

"""
    A function that checks whether the "Resource" JSON field contains a single asterisk (returns False) or not (returns True).
    The function takes the "file" argument, which is the path to the file being checked. First we try to get "file_to_json". 
    If the file does not exists, we return False. Otherwise, we will try to use the json library to get this data as a 
    Python dictionary. Then we try to get to the fields "Policy Document" and "Statement". The "Extract" field is a list, 
    so we take the first value from it. Then we check field type "Resource" as it can be a string or a list. 
    If it is a string, check if it contains a single asterisk. If so, return False. Otherwise, return True
"""
def check_policy_resource(file):
    try:
        # checking if file exists and opening it
        f = open(file, "r")

        # loading file text to python dictionary and readable data
        file_to_json = json.loads(f.read())

        # getting required data to check "Resource" field
        policy_statement = file_to_json['PolicyDocument']['Statement'][0]
        resource_type = type(policy_statement['Resource'])
        if resource_type == str:
            # if "Resource" field contains single asterisk return False
            if policy_statement['Resource'] == "*":
                return False

        # otherwise return True
        return True
    except FileNotFoundError:
        # if file doesn't exist raise exception and return False
        return False
    except json.JSONDecodeError:
        # if given file isn't a JSON file raise exception and return False
        return False
    except KeyError:
        # if JSON file doesn't contain required field raise exception and return False
        return False



if __name__ == "__main__":
    # if file was run "python check_resource.py" get file path via input
    if len(sys.argv) < 2:
        file_path = input("Please pass the file path: ")
    else:
        # otherwise get a file path as a first argument passed
        file_path = sys.argv[1]

        # if more than one file were passed use only the first one
        if len(sys.argv) > 2:
            print("Using only " + sys.argv[1] + " file")

    # print the result of check_policy_resource
    print(check_policy_resource(file_path))
