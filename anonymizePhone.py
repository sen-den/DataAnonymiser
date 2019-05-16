import re
from config import *

def anonymizePhone(text):

	subsLength = cfg["Phone"]["DigitsToHide"]
	subsSign = cfg["Phone"]["MaskingSign"]

	# could be underfull: 0 chars before most left space
	firstGroupLength = subsLength % 3

	subsFullGroupsCount = subsLength // 3
	
	# each 3-chars group adds one space char
	subsCharCount = subsLength + subsFullGroupsCount

	# {0-2} substitute chars followed by the space separated groups of it
	subs = subsSign*firstGroupLength + (" " + subsSign*3) * subsFullGroupsCount


	# replace each phone by its cutted version followed by masked chars
	text = re.sub(r'(\+[\d]+(\ [\d]{3}){3})'
		, lambda match: match.group(1)[:-subsCharCount] + subs
		, text)

	return text
