#!/bin/sh
sudo apt-get install nasm
nasm -f elf shellcode.asm
objdump -d shellcode.o
objcopy --dump-section .text=shellcode.bin shellcode.o
xxd shellcode.bin
