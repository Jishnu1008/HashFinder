import sys
import time
import pyfiglet
from rich.console import Console
from Crypto.Hash import (
    MD2, MD4, MD5,
    SHA1, SHA224, SHA256, SHA384, SHA512,
    SHA3_224, SHA3_256, SHA3_384, SHA3_512,
    BLAKE2b, BLAKE2s,
    RIPEMD
)
console = Console()
hash_length = {
    32: ["MD5", "MD4", "MD2"],
    40: ["SHA1", "RIPEMD_160"],
    56: ["SHA224", "SHA3_224"],
    64: ["SHA256", "SHA3_256", "BLAKE2S"],
    96: ["SHA384", "SHA3_384"],
    128: ["SHA512", "SHA3_512", "BLAKE2B"]
}
try:
    def MD(hash,hash_name):
        for rel_hash in hash_name:
            if rel_hash == 'MD5':
             with open("rockyou.txt",'r',encoding='latin-1') as file:
                for line in file:
                    line=line.strip()
                    hasher=MD5.new(line.encode()).hexdigest()
                    if hasher == hash:
                        console.print(f"[green][+] The original text is '{line}' and it uses MD5 Hashing algorithm.[/green]")
                        exit()
             console.print("[red][-] Not an MD5 hash[/red]")
            elif rel_hash == 'MD4':
                with open("rockyou.txt",'r',encoding='latin-1') as file:
                    for line in file:
                        line=line.strip()
                        hasher=MD4.new(line.encode()).hexdigest()
                        if hasher == hash:
                            console.print(f"[green][+] The original text is '{line}' and it uses MD4 Hashing algorithm.[/green]")
                            exit()
                console.print("[red][-] Not an MD4 hash[/red]")
            else:
                with open("rockyou.txt",'r',encoding='latin-1') as file:
                    for line in file:
                        line=line.strip()
                        hasher=MD2.new(line.encode()).hexdigest()
                        if hasher == hash:
                            console.print(f"[green][+] The original text is '{line}' and it uses MD2 Hashing algorithm.[/green]")
                            exit()
                console.print("[red][-] Not an MD2 hash\n[-] May be someother MD hash.[/red]")
            
    def Sha_40(hash,hash_name):
        for rel_hash in hash_name:
            if rel_hash == 'SHA1':
             with open("rockyou.txt",'r',encoding='latin-1') as file:
                for line in file:
                    line=line.strip()
                    hasher=SHA1.new(line.encode()).hexdigest()
                    if hasher == hash:
                        console.print(f"[green][+] The original text is '{line}' and it uses SHA1 Hashing algorithm.[/green]")
                        exit()
             console.print("[/red][-] Not an SHA1 hash[/red]")
            else:
                with open("rockyou.txt",'r',encoding='latin-1') as file:
                    for line in file:
                        line=line.strip()
                        hasher=RIPEMD.new(line.encode()).hexdigest()
                        if hasher == hash:
                            console.print(f"[green][+] The original text is '{line}' and it uses RIPEMD_160 Hashing algorithm.[/green]")
                            exit()
                console.print("[red][-] Not an RIPEMD_160 hash\n[-] May be someother hash.[/red]")

    def Sha_56(hash,hash_name):
        for rel_hash in hash_name:
            if rel_hash == 'SHA224':
             with open("rockyou.txt",'r',encoding='latin-1') as file:
                for line in file:
                    line=line.strip()
                    hasher=SHA224.new(line.encode()).hexdigest()
                    if hasher == hash:
                        console.print(f"[green][+] The original text is '{line}' and it uses SHA224 Hashing algorithm.[/green]")
                        exit()
             console.print("[red][-] Not an SHA224 hash[/red]")
            else:
                with open("rockyou.txt",'r',encoding='latin-1') as file:
                    for line in file:
                        line=line.strip()
                        hasher=SHA3_224.new(line.encode()).hexdigest()
                        if hasher == hash:
                            console.print(f"[green][+] The original text is '{line}' and it uses SHA3_224 Hashing algorithm.[/green]")
                            exit()
                console.print("[red][-] Not an SHA3_224 hash\n[-] May be someother hash.[/red]")
            
    def Sha_64(hash,hash_name):
        for rel_hash in hash_name:
            if rel_hash == 'SHA256':
                with open("rockyou.txt",'r',encoding='latin-1') as file:
                    for line in file:
                        line=line.strip()
                        hasher=SHA256.new(line.encode()).hexdigest()
                        if hasher == hash:
                            console.print(f"[green][+] The original text is '{line}' and it uses SHA256 Hashing algorithm.[/green]")
                            exit()
                console.print("[red][-] Not an SHA256 hash[/red]")
            elif rel_hash == 'SHA3_256':
                with open("rockyou.txt",'r',encoding='latin-1') as file:
                    for line in file:
                        line=line.strip()
                        hasher=SHA3_256.new(line.encode()).hexdigest()
                        if hasher == hash:
                            console.print(f"[green][+] The original text is '{line}' and it uses SHA3_256 Hashing algorithm.[/green]")
                            exit()
                console.print("[red][-] Not an SHA3_256 hash[/red]")
            else:
                with open("rockyou.txt",'r',encoding='latin-1') as file:
                    for line in file:
                        line=line.strip()
                        hasher=BLAKE2s.new(data=line.encode()).hexdigest()
                        if hasher == hash:
                            console.print(f"[green][+] The original text is '{line}' and it uses BLAKE2S Hashing algorithm.[/green]")
                            exit()
                console.print("[red][-] Not an BLAKE2S hash\n[-] May be someother hash.[/red]")

    def Sha_96(hash,hash_name):
        for rel_hash in hash_name:
            if rel_hash == 'SHA384':
             with open("rockyou.txt",'r',encoding='latin-1') as file:
                for line in file:
                    line=line.strip()
                    hasher=SHA384.new(line.encode()).hexdigest()
                    if hasher == hash:
                        console.print(f"[green][+] The original text is '{line}' and it uses SHA384 Hashing algorithm.[/green]")
                        exit()
             console.print("[red][-] Not an SHA384 hash[/red]")
            else:
                with open("rockyou.txt",'r',encoding='latin-1') as file:
                    for line in file:
                        line=line.strip()
                        hasher=SHA3_384.new(line.encode()).hexdigest()
                        if hasher == hash:
                            console.print(f"[green][+] The original text is '{line}' and it uses SHA3_384 Hashing algorithm.[/green]")
                            exit()
                console.print("[red][-] Not an SHA3_384 hash\n[-] May be someother hash.[/red]")

    def Sha_128(hash,hash_name):
        for rel_hash in hash_name:
            if rel_hash == 'SHA512':
             with open("rockyou.txt",'r',encoding='latin-1') as file:
                for line in file:
                    line=line.strip()
                    hasher=SHA512.new(line.encode()).hexdigest()
                    if hasher == hash:
                        console.print(f"[green][+] The original text is '{line}' and it uses SHA512 Hashing algorithm.[/green]")
                        exit()
             console.print("[red][-] Not an SHA512 hash[/red]")
            elif rel_hash == 'SHA3_512':
                with open("rockyou.txt",'r',encoding='latin-1') as file:
                    for line in file:
                        line=line.strip()
                        hasher=SHA3_512.new(line.encode()).hexdigest()
                        if hasher == hash:
                            console.print(f"[green][+] The original text is '{line}' and it uses SHA3_512 Hashing algorithm.[/green]")
                            exit()
                console.print("[red][-] Not an SHA3_512 hash[/red]")
            else:
                with open("rockyou.txt",'r',encoding='latin-1') as file:
                    for line in file:
                        line=line.strip()
                        hasher=BLAKE2b.new(data=line.encode()).hexdigest()
                        if hasher == hash:
                            console.print(f"[green][+] The original text is '{line}' and it uses BLAKE2b Hashing algorithm.[/green]")
                            exit()
                console.print("[red][-] Not an BLAKE2b hash\n[-] May be someother MD hash.[/red]")
    
    def HashID(hash):
        given_hash_length = len(hash)
        for val in hash_length:
            if given_hash_length == val:
                hash_name = hash_length[val]
                break

        console.print(f"[yellow][+] Possible hash used is {hash_name}[/yellow]")
        time.sleep(2)
        condition = console.input("[white][+] Shall I find the word for the given hash? (Y or N) [/white]")
        while(True):
         if condition.lower() == 'y':
            time.sleep(0.5)
            if len(hash)==32:
                MD(hash,hash_name)
            elif len(hash)==40:
                Sha_40(hash,hash_name)
            elif len(hash)==56:
                Sha_56(hash,hash_name)
            elif len(hash)==64:
                Sha_64(hash,hash_name)
            elif len(hash)==96:
                Sha_96(hash,hash_name)
            else:
                Sha_128(hash,hash_name)
            exit()
         elif condition.lower() == 'n':
                exit()
         else:
            console.print("[red][!] Please give a valid answer. [/red]")
            time.sleep(1)
            condition=input("[+] Y or N ") 
    if len(sys.argv)==3:
        mode = sys.argv[1]
        if mode == "-i":
            console.print(pyfiglet.figlet_format("HashFinder",font="slant"))
            hash = sys.argv[2]
            HashID(hash)
        else:
            console.print("[red][!] Please run the command 'hasher.py -h' to get help and it displays the relevant options to use the commands.[/red]")
    elif len(sys.argv)==2:
        if sys.argv[1] == "-h":
            console.print("[yellow][+] Usage: hasher.py -i <hash>[/yellow]\n[yellow][+] Options:\n  [+] -i <hash> : To find the hash type and the original text for the given hash.[/yellow]")
        else:
            console.print("[red][!] Please run the command 'hasher.py -h' to get help and it displays the relevant options to use the commands.[/red]")
    elif  len(sys.argv)>3:
        console.print("[red][!] Need two arguments only.[/red]\n[red][!] Please run the command 'hasher.py -h' to get help and it displays the relevant options to use the commands.[/red]")
    else:
        console.print("[red][!] Need two arguments to run.[/red]\n[red][!] Please run the command 'hasher.py -h' to get help and it displays the relevant options to use the commands.[/red]")
except KeyboardInterrupt:
    print("Keyboard Interrupt detected! Exiting program.")
    time.sleep(2)
