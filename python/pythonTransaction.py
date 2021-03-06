import algosdk
import base64
# Transaction bytes string encoded in base64, as generated by the JS into the blob field
tx_base64 = None #"gqNzaWfEQAk..." 
if tx_base64:
    try:
        tx = algosdk.encoding.msgpack_decode(tx_base64)
        print(f'Signature: {tx.signature}')
        print(f'Transaction: {tx.transaction.__dict__}')
    except:
        print('Error decoding the base 64 transaction.')
else:
    print('Base 64 transaction not defined.')