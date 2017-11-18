alphabet = " abcdefghijklmnopqrstuvwxyz"
alphabet = list(alphabet)
AlphaToNum = {}
NumToAlpha = {}

for i in range(len(alphabet)):
    AlphaToNum[alphabet[i]] = i
    NumToAlpha[i] = alphabet[i]


cases = int(input())

for i in range(cases):
    value = []
    ip = input()
    ip = list(ip)
    task = ip[0]
    msg = ip[2:]

    if task == 'e':
        for j in msg:
            value.append(AlphaToNum[j])
        progressive = value[:]

        for k in range(1, len(value)):
            progressive[k] += progressive[k-1]
        modulus = []
        for x in progressive:
            modulus.append(x%27)
        encrypt = []
        for y in modulus:
            encrypt.append(NumToAlpha[y])

        print(''.join(encrypt))


    if task == 'd':
        for j in msg:
            value.append(AlphaToNum[j])
        deMod=[value[0]]
        for k in range(1,len(value)):
            deMod.append(deMod[-1] + (value[k] - deMod[-1])%27)

        degressive = deMod[:]

        for l in range(1, len(deMod)):
            degressive[l] = deMod[l] - deMod[l-1]
        decrypt = []
        for x in degressive:
            decrypt.append(NumToAlpha[x])
        print(''.join(decrypt))
