import re

a = re.sub('(\d+)(?=\.\w+$)', lambda match:'#'*len(match.group(1)), 'image.0010001.tiff')


print(a)
