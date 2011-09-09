import os

for filename in os.listdir('.'):
	if filename[-8:] == 'jpg_dl=1':
		os.rename(filename, filename[:-5])