
encoding = 16
length = int(encoding/8)

#Hashtable for instruction and 
bitsToMnemonic = {136: "mov"}
reg = [['al', 'cl', 'dl', 'bl', 'ah','ch','dh','bh'],['ax','cx','dx','bx','sp','bp','si','di']]

## Open file
ifDir = r'C:\Users\torst\perfAware\computer_enhance\perfaware\part1'
#ifName = r'listing_0037_single_register_mov'
ifName = r'listing_0038_many_register_mov'

ofName = ifName + "_disasm.asm"
ofile = open(ofName, 'w')
ofile.write(f'\nbits {encoding}\n\n')

with open(ifDir +'\\'+ ifName, 'rb') as f:
    while (byte := f.read( length )):
        code = int.from_bytes(byte,"big")
        left = code >> 8

        ## Handle warnings/something is wrong.
        if(code & 192 != 192):   ## Only MOD == 11, Register mode implemented
            print("Not implemented.")
            break

        ## Set registers      
        source = reg[left & 1][(code>>3) % 8]
        dest = reg[left & 1][code % 8]

        
        ## Execute instruction 
        ofile.write(f'{bitsToMnemonic[left & 252]} {(dest,source)[left & 2]}, {(source,dest)[left & 2]}\n')
        
        print(f'{bitsToMnemonic[left & 252]} {(dest,source)[left & 2]}, {(source,dest)[left & 2]}\n', end='')
