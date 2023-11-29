import encrypt
message = "This is some sample text"
key = 'normal-message1'
enc = encrypt.encrypt(key,message)
dec = encrypt.decrypt(key,enc)
if message == dec :
    print('both are equal')
