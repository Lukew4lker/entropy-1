with open("../bin/entropy.img", "ab") as f:
    b = b"\0"
    while f.tell() < 2*8*512:
        f.write(b)
    with open("../bin/disk_data.tmp", "rb") as g:
        while b:
            b = g.read(1)
            f.write(b)
