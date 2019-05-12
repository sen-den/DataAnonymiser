import re
from config import *

def anonymizeSkype(text):
	replace = "skype:[a-zA-Z1-9]+"
	subs = "skype:" + cfg["Skype"]["MaskingSign"]
	text = re.sub(replace, subs, text, flags=re.IGNORECASE)

	return text
