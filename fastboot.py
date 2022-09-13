import fastbootpy
from fastbootpy import *
from fastbootpy import FastbootDevice, FastbootManager
from ppadb.command import serial


def main() :
    fastboot_devices = FastbootManager.devices()
    #serial = fastboot_devices[0]
    device = FastbootDevice.connect(serial)
    result = device.getvar("all")
    print("result:", result)


main()
