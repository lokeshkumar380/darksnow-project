import base64


def encrypt(session, secret, alias):
    client = session.client('kms', region_name='us-east-1')
    ciphertext = client.encrypt(
        KeyId=alias,
        Plaintext=bytes(secret, 'utf-8'),
    )
    base64bytes = base64.b64encode(ciphertext["CiphertextBlob"])
    return base64bytes.decode('utf-8')


def decrypt(session, secret):
    client = session.client('kms', region_name='us-east-1')
    plaintext = client.decrypt(
        CiphertextBlob=bytes(base64.b64decode(secret))
    )
    return plaintext["Plaintext"].decode('utf-8')
