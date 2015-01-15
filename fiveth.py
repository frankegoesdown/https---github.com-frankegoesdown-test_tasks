# coding: utf-8

#1st method
import urllib2
from xml.dom import minidom

source = urllib2.urlopen("http://www.cbr.ru/scripts/XML_daily.asp")
xmldoc = minidom.parse(source)
list_ids = ['R01235', 'R01239']
valutes = xmldoc.getElementsByTagName("Valute")
for valute in valutes:
	id = valute.getAttribute("ID")
	value = valute.getElementsByTagName("Value")[0]
	char_code = valute.getElementsByTagName("CharCode")[0]
	if id in list_ids:
		print ("exchange rate:%s, char code:%s" %
			  (value.firstChild.data, char_code.firstChild.data))

#2nd method
from xml.etree import ElementTree as etree
from contextlib import closing

def find_val_and_char(id):
	with closing(urllib2.urlopen("http://www.cbr.ru/scripts/XML_daily.asp")) as r:
		for country in etree.parse(r).findall('Valute[@ID="%s"]'%(id)):
			value = country.find('Value').text
			char_code = country.find('CharCode').text
			print ("exchange rate:%s, char code:%s" %
			  (value,char_code))

find_val_and_char("R01235")
find_val_and_char("R01239")