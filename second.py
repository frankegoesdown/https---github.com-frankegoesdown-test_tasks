# coding: utf-8
__author__ = 'a.chernikov'

#first
def check_login(login):
	flag = False
	if 0 < len(login) <= 20:
		from re import match

		if match(r'^[a-zA-Z]([-.\w]*\w)?$', login):
			flag = True
	return flag


#second
a = ord("a")
z = ord("z")
n0 = ord("0")
n9 = ord("9")
dot = ord(".")
t = ord("-")


def isChar(ch):
	num = ord(ch)
	return a <= num and num <= z


def isNumberOrChar(ch):
	num = ord(ch)
	return (a <= num and num <= z) or \
		   (n0 <= num and num <= n9)


def isValidChar(ch):
	num = ord(ch)
	return (a <= num and num <= z) or \
		   ( n0 <= num and num <= n9) or \
		   num == dot or num == t


def parse(str):
	len_str = len(str)
	if (len_str == 0 or len_str > 20):
		return False
	elif (len_str == 1):
		return isChar(str)
	for i, ch in enumerate(str):
		if i == 0 and not isChar(ch):
			return False
		elif i + 1 == len_str and not isNumberOrChar(ch):
			return False
		elif not isValidChar(ch):
			return False
	return True


def test_parse(str):
	res = parse(str)
	if res:
		return True
	return False

print check_login('a2.53253333')
print test_parse('a2.53253333')
