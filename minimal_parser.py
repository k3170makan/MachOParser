#!/usr/bin/python
import struct
import sys
class MachOHeader:
	def __init__(self,raw_file):
		self.raw_file = raw_file
		self.magic_number = struct.unpack("BBBB",raw_file[:4])
		self.cpu_type = struct.unpack("bbbb",raw_file[4:8]) #cputype fields are signed
		self.cpu_sub_type = struct.unpack("bbbb",raw_file[8:12])
		self.filetype = struct.unpack("BBBB",raw_file[12:16])
		self.ncmds = struct.unpack(">I",raw_file[16:20])
		self.sizeofcmds = struct.unpack(">I",raw_file[20:24])
		self.flags = struct.unpack("bbbb",raw_file[24:28])	
		self.attrs = {"Magic Number":self.magic_number,
						   "CPU Type":self.cpu_type,
							"CPU Sub Type":self.cpu_sub_type,
							"File Type":self.filetype ,
							"Number of Load Commands":self.ncmds ,
							"Size of Load Command Field":self.sizeofcmds,
										  "Flags":self.flags} 
		self.repr_attrs = dict()
		for attr in self.attrs:
			try:
				if attr == "Size of Load Command Field" or attr == "Number of Load Commands":
					self.repr_attrs[attr] = self.attrs[attr]
				else:
					self.repr_attrs[attr] = [hex(i)[2:] for i in self.attrs[attr]]
			except KeyError:
				pass	
	def __repr__(self):
		repr_string = ""
		for attr in self.repr_attrs:
			repr_string += "[*] %s:%s\n" % (attr,self.repr_attrs[attr])
		return repr_string
if __name__=="__main__":

	if len(sys.argv) <= 1:
		sys.exit(1)
	#grab the file and do a rough pull of the header properties
	raw_file = open(sys.argv[1],'rb').read()
	macho_header = MachOHeader(raw_file)
	print macho_header

