#!/usr/bin/python

import os
from PIL import Image

def get_imlist(path,fmt_input):
	""" Return a list of filenames for all bmp images in a directory."""
	return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(fmt_input)]

def convert_image_fmt(path, fmt_input,fmt_output):
	im_list = get_imlist(path,fmt_input)
	for infile in im_list:
		outfile=os.path.splitext(infile)[0]+fmt_output
		if infile != outfile:
			try:
				Image.open(infile).save(outfile)
			except IOError:
					print "cannot convert", infile