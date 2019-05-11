import re
from config import *

def anonymizeSkype(text):
	subs = "skype:" + cfg["Skype"]["MaskingSign"]
	text = re.sub("skype:[a-zA-Z1-9]+", subs, text, flags=re.IGNORECASE)


	return text
