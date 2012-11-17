#!/bin/sh
mkdir ../bin/
echo -------------------
echo Building Bootloader
echo -------------------
mono Organic.exe ../src/Bootloader/main.dasm ../bin/bootloader.bin --working-directory ../src/Bootloader/
echo -------------------
echo Building Kernel
echo -------------------
mono Organic.exe ../src/Kernel/main.dasm ../bin/entropy.bin --working-directory ../src/Kernel/ --listing debug/entropy.lst
echo -------------------
