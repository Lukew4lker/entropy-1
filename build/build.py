#! /usr/bin/env python3.3

import os, platform, sys, random

def addexeh(code):
        pass

def build(f, outname="", le=True):
	if outname == "":
		outname = f[f.rfind("/")+1:f.rfind(".")] + ".bin"
	print("Building: ", outname)
	c = ""
	if platform.system() != "Windows":
		c += "mono ../tools/Organic.exe ../src/"
	else:
                c += "..\\tools\\Organic.exe ../src/"
	c += f +  " ../bin/" + outname
	c += " --working-directory ../src/" + f[:f.rfind("/")+1]
	if le:
		c += " --little-endian"
	os.system(c)
	return outname

def waitkey():
	input("Press Enter to continue...")

def inttobytes(int, minbytes=0):
	result = []
	while int > 0 or minbytes > 0:
		minbytes -= 1
		result.append(int & 255)
		int >>= 8
	return bytes(result)

def makedte(num):
	if num > 30:
		return b""
	result = b""
	name = includes[num]
	name = name[:name.rfind(".")]
	name = name[:name.rfind(".")]
	name = bytes(name, "utf-8")[:8]
	result += name #name
	result += bytes(8 - len(result)) #name padding
	ext = bytes(includes[num], "utf-8")[9:12]
	result += ext #extension
	if ext == b"bin":
		result += inttobytes(64) #flags
	else:
		result += bytes(1) #flags
	result += bytes(12) #times
	result += inttobytes(sizes[num], 4) #file size
	result += inttobytes(firstsectors[num], 2) #first sector
	result += bytes(2) #reserved
	result = result[1:2] + result[0:1] + result[3:4] + result [2:3] + \
			result [5:6] + result[4:5] + result[7:8] + result[6:7] + \
			result[9:10] + result[8:9] + result[11:12] + result[10:11] + \
			result[12:24] + result[26:28] + result[24:26] + result[28:]
	return result
	
try:
	build("Bootloader/main.dasm", "bootloader.bin", False)
	build("Kernel/main.dasm", "entropy.bin")
	build("Kernel/diskdata.dasm", "diskdata.bin")
	with open("buildlist.txt", "r") as f:
		builds = f.readlines()
	includes = [build(x) for x in builds]
	with open("includelist.txt", "r") as f:
		includes += f.readlines()
	filedata = []
	for i in includes:
		with open("../bin/" + i, "rb") as f:
			filedata.append(f.read())
	sizes = [len(x)//2 for x in filedata]
	with open("../bin/bootloader.bin", "rb") as f:
		bootloader = f.read()
	with open("../bin/diskdata.bin", "rb") as f:
		diskdata = f.read()
	with open("../bin/entropy.bin", "rb") as f:
		f.seek(32)
		entropy = f.read()
	sizes2 = [((a - 1) >> 9) + 1 for a in sizes]
	reservedsectors = ((len(entropy) + 32) >> 10) + 1
	bytesout = bytes.fromhex("82c3") #bootflag
	bytesout += bytes.fromhex("164a") #filesystem descriptor
	bytesout += bytes("nErtpo\0y\0\0\0\0", "utf-8") #disk name
	bytesout += inttobytes(reservedsectors, 2) #reserved sectors
	bytesout += inttobytes(1, 2) #FAT tables
	bytesout += inttobytes(512, 2) #words per sector
	bytesout += inttobytes(1440, 2) #number of sectors on disk
	bytesout += inttobytes(random.randint(0, 2 ** 64 - 1), 4) #random ID
	bytesout += entropy #entropy code
	bytesout += bytes(1024 * reservedsectors - len(bytesout)) #filler
	bytesout += diskdata
	if len(diskdata) % 1024 != 0:
		bytesout += bytes(1024 - (len(diskdata) % 1024))
	for d in range(len(filedata)):
		bytesout += filedata[d]
		bytesout += bytes(2 * (sizes2[d] * 512 - sizes[d]))
	with open("../bin/entropy.img", "wb") as f:
		f.write(bytesout)
	print("\n====== BUILD SUCCESS ======\n")
except:
	print("\n====== BUILD FAILED ======\n")
	waitkey()
	raise

waitkey()
