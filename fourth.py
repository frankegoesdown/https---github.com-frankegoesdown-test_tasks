# coding: utf-8

#first
def get_stat(filename):
	"""
	:filename - путь до файла
	"""
	stat = dict()
	with open(filename) as f:
		for line in f:
			chunk = line.split(" ")
			if len(chunk) > 0:
				ip = chunk[0]
			stat[ip] = stat.get(ip, 0) + 1
	return stat


import sys


def main():
	if len(sys.argv) > 1:
		path = sys.argv[1]
	else:
		path = "access.log"

	if len(sys.argv) > 2:
		try:
			limit = int(sys.argv[2])
		except Exception:
			limit = 5
	else:
		limit = 5

	stat = get_stat(path).items()
	stat = sorted(
		stat,
		key=lambda x: x[0]
	)
	for result in stat[:limit]:
		print("%s %s" % (result[1], result[0]))

#second
import re
from collections import Counter
regex = '^(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})'
ip_list = []
for line in open('access.log'):
	ip_list.append(re.match(regex, line).group())



main()
print Counter(ip_list).most_common(5)