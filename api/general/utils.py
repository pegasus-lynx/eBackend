import os
import json

def get_result(result_token):
    result_file_name = result_token + ".json"
    print(result_file_name)
    result_file = open('/home/parzival3219/recommender/Barc-modified/result/' +result_file_name, "r")
    data = json.load(result_file)
    result_file.close()

    return data

def get_result_token(obj):
    ind = obj.pk
    token = "barc_"+obj.created.strftime("_%Y_%m_%d_%H_%M_%S")
    return token