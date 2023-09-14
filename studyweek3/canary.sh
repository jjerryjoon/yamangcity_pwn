#!/bin/sh
gcc -o canary canary.c -fstack-protector
gcc -o no_canary canary.c -fno-stack-protector
