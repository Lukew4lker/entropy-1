@echo off
mkdir ..\bin
echo -------------------
echo Building Bootloader
echo -------------------
organic.exe ../src/bootloader/main.dasm ../bin/bootloader.bin --working-directory ../src/bootloader/
echo -------------------
echo Building Kernel
echo -------------------
organic.exe ../src/kernel/main.dasm ../bin/entropy.img --working-directory ../src/kernel/ --little-endian
echo -------------------
echo Building Disk
echo -------------------
organic.exe ../src/kernel/disk_data.dasm ../bin/disk_data.tmp --little-endian
echo -------------------
echo Building Init.bin
echo -------------------
organic.exe ../src/kernel/init.bin.dasm ../bin/init.bin.tmp --little-endian
echo -------------------
echo Making disk
echo -------------------
..\bin\makedisk.py
echo -------------------
pause
@echo on