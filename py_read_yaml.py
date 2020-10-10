import yaml
import argparse
import json
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='filename', help="Full path of the file")
args = parser.parse_args()

filename = args.filename

with open(filename, 'r') as f:
    py_object = yaml.load(f, Loader=yaml.FullLoader)
    # pprint(py_object)

print(json.dumps(py_object, indent=4))