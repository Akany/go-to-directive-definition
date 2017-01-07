from glob import glob
import re
import os

DIRECTIVES_PATTERN = '**/*.directive.js'
CONTENT_NAME_REG = '.directive\([\'"](\w+)[\'"]';

def read_directives(pattern):
	return glob(pattern)

def read_file(file):
	fo = open(file, 'r')
	content = fo.read()
	fo.close()

	return content

def find_directive_name(content):
	match = re.search(CONTENT_NAME_REG, content)

	if match:
		return match.group(1)

def cache(folders):
	for folder in folders:
		path = os.path.join(folder, DIRECTIVES_PATTERN)
		for file in read_directives(path):
			directive_name = find_directive_name(read_file(file))
			if directive_name:
				directives_map[directive_name] = file

def get(name):
	return directives_map.get(name);

directives_map = {}
