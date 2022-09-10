import fastbootpy
from fastbootpy import *
dev = fastbootpy.FastbootDevice

fastboot_devices = FastbootManager.devices()

def detct() :
    fastboot_devices = FastbootManager.devices()


def getVar():
        dev.getvar(fastboot_devices,"all")
getVar

