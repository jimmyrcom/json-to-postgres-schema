#!/usr/bin/python3
# Created by Jimmy Ruska under GPL 3 (JimmyR.com)
import os,re,platform,sys
import  json

def psql_type(x):
    if isinstance(x, dict):
        return "jsonb"
    elif isinstance(x, float):
        return "float8"
    elif isinstance(x, int):
        return "int"
    elif isinstance(x, str):
        return "text"
    elif isinstance(x, bool):
        return "bool"
    elif isinstance(x, list):
        return "jsonb"
    else: return "text"

def psql_json(history, obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            change = history + "->'{}'".format(key)
            print(change+"::{}".format(psql_type(value)))
            psql_json(change, value)

def main():
    with open(sys.argv[1], 'r') as f:
        line = f.readline().rstrip('\n')
    data = json.loads(line)
    psql_json('data',data)


if __name__ == '__main__':
    main()
