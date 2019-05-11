import json

configFile = "config.json"

try:
	with open(configFile) as config:
		cfg = json.loads(config.read())
except FileNotFoundError:
	print("File not exist: ", configFile)

print(configFile, cfg)
