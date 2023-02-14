def binary_To_Hexadecimal(n):
    
    #convert binary to int
    num = int(n, 2)
      
    # convert int to hexadecimal
    hex_num = format(num, 'x')
    if(hex_num =='a'):
        hex_num = '10'
    if(hex_num =='b'):
        hex_num = '11'
    if(hex_num =='c'):
        hex_num = '12'
    if(hex_num =='d'):
        hex_num = '13'
    if(hex_num =='e'):
        hex_num = '14'
    if(hex_num =='f'):
        hex_num = '15'
    return(int(hex_num))

#Reading the given P-C pairs
with open('256PC-pairs.txt') as f:
    lines = f.readlines()

a=[]
b=[]
count = [0]*256
plaintext = []
ciphertext = []
for i in range(0,len(lines)):
    
    a = lines[i].split(' ')
    plaintext.append(int(a[0]))
    b = a[3].split('\n')
    ciphertext.append(int(b[0]))



# print(plaintext)
# print(ciphertext)

#Initializing the S-box
S_Box = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7]

#Preparing S-box inverse to run the decoded ciphertexts back through the S-boxes
S_BoxInv =[0]*16
for i in S_Box:
    S_BoxInv[S_Box[i]] = S_Box.index(S_Box[i])

# print(S_BoxInv)
for (p,c) in zip(plaintext,ciphertext):
    for key in range(256):
        
        
        #decrypting the ciphertexts
        V3 = '{0:08b}'.format(key^c)
        
        #passing it backward through the S-box
        hx1 = binary_To_Hexadecimal(V3[0:4])
        hx2 = binary_To_Hexadecimal(V3[4:8])
        
        #Getting the U3 bits
        U31 = S_BoxInv[hx1]
        U32 = S_BoxInv[hx2]
        
        S1 = '{0:04b}'.format(U31)
        S2 = '{0:04b}'.format(U32)
        
    
        x = '{0:08b}'.format(p)

       #Checking the linear approximation using U3 bits and plaintext bits
        xor_val = int(x[0],2)^int(x[1],2)^int(x[2],2)^int(x[3],2)^int(S1[1],2)^int(S1[3],2)^int(S2[1],2)^int(S2[3],2)
        if(xor_val==0):
            count[key]+=1

maximum_count = -9999
for i in range(len(count)):
    count[i] = abs(count[i]-127)/256
    if(count[i]>maximum_count):
        maximum_count = count[i]
        k = '{0:08b}'.format(i)
        k14 = k[0:4]
        k58 = k[4:8]
        print('key = ', k,'bias = ',maximum_count)
print('K1-4 is ',k14)
print('K5-8 is ',k58)