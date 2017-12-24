#!/usr/bin/python

   
import Image  
import os.path  
import glob  
  
 
def jpg2pgm( jpg_file , pgm_dir ):  
	
	jpg = Image.open( jpg_file )  
	 
	jpg = jpg.resize( (200,250) , Image.BILINEAR )  
	
	name =(str)(os.path.join( pgm_dir , os.path.splitext( os.path.basename(jpg_file) )[0] ))+".pgm"  
	
	jpg.save( name )  
  
 
for jpg_file in glob.glob("./*.jpg"):  
	jpg2pgm( jpg_file , "/home/sam/pgm/" )  