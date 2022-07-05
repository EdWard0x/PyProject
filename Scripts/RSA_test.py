import base64
import rsa
pubkey, privkey = rsa.newkeys(1024)

pub = pubkey.save_pkcs1()
pri = privkey.save_pkcs1('PEM')

with open("pubkey.pem", mode='wb') as f,open('privkey.pem', mode='wb') as f1:
    f.write(pub)
    f1.write(pri)

with open("pubkey.pem", mode='rb') as f,open('privkey.pem', mode='rb') as f1:
    pub = f.read()
    pri = f1.read()
    pubkey = rsa.PublicKey.load_pkcs1(pub)
    privkey = rsa.PrivateKey.load_pkcs1(pri)

message = 'rsa加密测试'

info = rsa.encrypt(message.encode('utf-8'), pubkey)
msg = rsa.decrypt(info, privkey)
print(msg)
print(msg.decode('utf-8'))