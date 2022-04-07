from bluepy import btle
from switchbot import SwitchbotScanDelegate

scanner = btle.Scanner().withDelegate(SwitchbotScanDelegate('E0:AA:3D:44:81:A0'))
scanner.scan(5.0)
print(scanner.delegate.sensorValue)