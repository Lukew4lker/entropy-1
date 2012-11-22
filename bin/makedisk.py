with open("../bin/entropy.img", "ab") as f:
	size = f.tell()
	if size < 2 * 8 * 512:
		f.write(bytes(2 * 8 * 512 - size))
	with open("../bin/disk_data.tmp", "rb") as g:
		with open("../bin/init.bin.tmp", "rb") as h:
			size = h.seek(0, 2)
			h.seek(0)
			f.write(g.read(3130))
			f.write(bytes(((size & 255) // 2,)))
			g.seek(1,1)
			f.write(g.read(1989))
			f.write(h.read(size))
if size < 256:
	print("Disk build successful!")
else:
	print("ERROR: init.bin.dasm is too large.")
