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
pause
@echo on