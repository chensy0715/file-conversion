#!/usr/bin/python

import sys 
import struct 
import os 

__author__ = 'chensy0715@gmail.com'
__date__ = 'Sept 19,2017'
__update__ = 'Sept 19,2011'
def geneHeadInfo(sampleRate,bits,sampleNum): 

	rHeadInfo = '\x52\x49\x46\x46'
	fileLength = struct.pack('i',sampleNum + 36) 
	rHeadInfo += fileLength 
	rHeadInfo += '\x57\x41\x56\x45\x66\x6D\x74\x20\x10\x00\x00\x00\x01\x00\x01\x00'
	rHeadInfo += struct.pack('i',sampleRate) 
	rHeadInfo += struct.pack('i',sampleRate * bits / 8) 
	rHeadInfo += '\x02\x00'
	rHeadInfo += struct.pack('H',bits) 
	rHeadInfo += '\x64\x61\x74\x61'
	rHeadInfo += struct.pack('i',sampleNum) 
	return rHeadInfo 
	
if __name__ == '__main__': 
	if len(sys.argv) != 5: 
		print "usage: python %s inFile sampleRate bits outFile" % sys.argv[0] 
		sys.exit(1) 
	fout = open(sys.argv[4],'wb') #用二进制的写入模式 

	fin = open(sys.argv[1],'rb') 
	Riff_flag, = struct.unpack('4s',fin.read(4)) 
	if Riff_flag == 'RIFF': 
		print "%s information" % sys.argv[1] 
		fin.close() 
		sys.exit(0) 
	else: 
		print "%s no header information" % sys.argv[1] 
		fin.close() 
		#采样率 
		sampleRate = int(sys.argv[2]) 
		#bit位 
		bits = int(sys.argv[3]) 
		fin = open(sys.argv[1],'rb') 
		startPos = fin.tell() 
		fin.seek(0,os.SEEK_END) 
		endPos = fin.tell() 
		sampleNum = (endPos - startPos) 
		print sampleNum 
		headInfo = geneHeadInfo(sampleRate,bits,sampleNum) 
		fout.write(headInfo) 
		fin.seek(os.SEEK_SET) 
		fout.write(fin.read()) 
		fin.close() 
		fout.close()