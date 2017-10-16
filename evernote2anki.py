# coding: utf8

import sys
import xml.etree.ElementTree as ET

def main(argv):
	if (len(argv) != 1):
		print "evernote2anki.py <inputFile>"
		sys.exit(2)
	inputFile = argv[0]
	tree = ET.parse(inputFile)
	root = tree.getroot()

	outputFile = './note.txt'
	f = open(outputFile, 'w')

	for note in root:
		noteTitle = note[0]
		noteContent = note[1]
		contentTree = ET.fromstring(noteContent.text.encode('utf8'))
		f.write(noteTitle.text.replace(' ', '_').encode('utf8'))
		f.write('\t')
		allDivs = contentTree.findall('div')
		divStrings = []
		for div in allDivs:
			divStrings.append(ET.tostring(div, encoding='utf8', method='xml'))
		for s in divStrings:
			newString = s[37:].replace('\n','')
			f.write(newString)
		f.write('\n')
		f.write('\n')
	f.close()

if __name__ == '__main__':
	main(sys.argv[1:])