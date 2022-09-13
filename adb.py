
from ppadb.client import Client as AdbClient
host = '127.0.0.1'
port=5037
def connect():
    client = AdbClient(host,port)
    device=client.devices()
    device.

