import re
from config import *

def anonymizePhone(text):
	phoneReg = re.compile("(\+\d{1," +str(cfg["Phone"]["MaxCodeLength"])+ "}(\ \d{3}){3})")

	subsLength = cfg["Phone"]["DigitsToHide"]
	subsSign = cfg["Phone"]["MaskingSign"]

	# could be underfull: 0 chars before most left space
	firstGroupLength = subsLength % 3

	subsFullGroupsCount = subsLength // 3
	
	subsCharCount = subsLength + subsFullGroupsCount

	subs = subsSign*firstGroupLength + (" " + subsSign*3) * subsFullGroupsCount

	listToSubstitute = [phone[0] for phone in phoneReg.findall(text)]

	for phone in listToSubstitute:
		text = text.replace(phone, phone[:-subsCharCount] + subs)

	return text
