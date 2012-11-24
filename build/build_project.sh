#!/bin/sh
mkdir ../bin/
echo -------------------
echo Building Bootloader
echo -------------------
mono Organic.exe ../src/Bootloader/main.dasm ../bin/bootloader.bin --working-directory ../src/Bootloader/
echo -------------------
echo Building Kernel
echo -------------------
mono Organic.exe ../src/Kernel/main.dasm ../bin/entropy.img --working-directory ../src/Kernel/ --little-endian
echo -------------------
echo Building Disk
echo -------------------
mono Organic.exe ../src/Kernel/disk_data.dasm ../bin/disk_data.tmp --little-endian
echo -------------------
echo Building Init.bin
echo -------------------
mono Organic.exe ../src/Kernel/init.bin.dasm ../bin/init.bin.tmp --little-endian
echo -------------------
echo Making disk
echo -------------------
..\bin\makedisk.py
echo -------------------
