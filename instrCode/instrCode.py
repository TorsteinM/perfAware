

opCode ={"mov": 136}
reg = {"ax": 0,"bx": 1,"cx": 2,"dx": 3,}
width = 32


def lineDecode(asmLine):
    print("decoding: ", asmLine,end='')
    (operator, dest, source) = asmLine.split(' ')
    firstByte = opCode[operator]
    
    # Set DW fields
    if( True ):
        firstByte += 3 ## Default to wide and Dest in REG field

    secondByte = 0
    ## MOD
    if( True ):
        secondByte += 128 + 64 ## Default to register-register mode

    ## REG
    if( True ):
        secondByte += reg[dest[:2]] * 8 ## Add dest register to REG field

    ## R/M
    if( True ):
        secondByte += reg[source[:2]]

    return (firstByte, secondByte)

def updateWidth(w):
    global width
    width = w

## Open asm file
ifDir = r'C:\Users\torst\perfAware\computer_enhance\perfaware\part1'
ifName = r'listing_0037_single_register_mov.asm'
ifile = open(ifDir +'\\'+ ifName, 'r')


## Open/Create machine code file
ofDir = r'C:\Users\torst\perfAware\instrCode'
ofName = ifName.split('.')[0]

ofile = open(ofDir +'\\'+ ofName, 'wb', buffering=0)
## Create machine code

for line in ifile.readlines():
    ## Skip empty and comments
    if line[0] == ';' or len(line)<=1:
        continue

    ## Handle width setting
    if line[:4] == 'bits':
        newBits = int(line.split(' ')[1])
        if width != newBits:
            print("Width updated from ", width, end='')
            updateWidth(newBits)
            print(" to ", width," bits width.")
        continue

    ## Decode assembly instruction
    res = 0
    for num in lineDecode(line):
        res += ofile.write(num.to_bytes(1,byteorder='big'))

print(f'Wrote {res} bytes to {ofile}.')