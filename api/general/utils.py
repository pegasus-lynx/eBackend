import os
import json

def get_result(result_token):
    result_file_name = "output_" + result_token + ".json"
    result_file = open(result_file_name, "r")
    data = json.load(result_file)
    result_file.close()

    return data