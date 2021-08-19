import json

import requests
from pyparsing import QuotedString, Suppress, Word, nums, printables
from requests.auth import HTTPBasicAuth

URL = 'https://api.dehashed.com/search'
PARAMS = {'query': 'domain_to_search.com', 'size': '1000'}
headers = {'Accept': 'application/json'}
user = 'user_login'
api_key = 'your_api_key'

string_to_parse = Suppress('{"balance":') + Suppress(Word(nums + ',')) + Suppress('"entries":') + \
                  QuotedString('[', endQuoteChar='],') + Suppress('"success":') + Suppress('true,') +\
                  Suppress('"took":') + Suppress(Word(printables)) + Suppress('"total":') + Suppress(Word(printables))


def result_string_parsing(s):
    result_string = string_to_parse
    parsed_data = result_string.parseString(s).asList()
    return parsed_data


if __name__ == '__main__':
    f = open(r"file_with_results.json", 'w')
    r = requests.get(url=URL, headers=headers, params=PARAMS, auth=HTTPBasicAuth(user, api_key))
    print(r.json())
    jsonString = json.dumps(r.json())
    data_to_write = result_string_parsing(jsonString)
    f.write('[')
    for x in range(len(data_to_write)):
        f.write(data_to_write[x])
    f.write(']')
    f.close()
    
