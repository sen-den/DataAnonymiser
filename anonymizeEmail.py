import re
from config import *

def anonymizeEmail(text):

	subsSign = cfg["Mail"]["MaskingSign"]

	# replace each part between first and last character of valid email 
	# by same size string of substitute characters
	text = re.sub(r'(?<=[\w])([\w][\w\_\.\-\+]*)(?=[\w]\@[\w]+(\.[\w][\w\-\+]*[\w])+)'
		, lambda match: subsSign * len(match.group(1))
		, text)

	return text
