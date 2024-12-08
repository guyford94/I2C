
## Example Code for Pyboard Slave

#Here’s an example of how you could implement this protocol on the Pyboard (slave) side using MicroPython:


import machine
import time
from machine import I2C


def DataFromMaster():
    return i2c.recv(3,timeout=10).decode()


def DataToMaster(pymsg):
    i2c.send(pymsg)
   # print("Send to master: " + pymsg)


def checksum(msg):
    v = 21
    for c in msg:
        v ^= ord(c)
    return v


# Set up I2C
i2c = I2C(1)  # create Slave on bus 2 : Pyboard lite there are 1 for Bus X and 3 for Bus Y
    i2c.init(i2c.SLAVE, addr=0x48)  # init as a peripheral with given address
    Cheksum = 0
    BodyList = []
    Body = ""

    i=0
    while True:

        try:
            data = DataFromMaster()
            #print("Recived from master: " + data)
            # start conection whit master
            if (data == 'RTT'):
                DataToMaster("RTR")

		# Check of equipment
            elif (data == 'INI'):
                DataToMaster("OK_")

            # bigining of session
            elif (data == 'BGN'):
                DataToMaster("RDY")

            elif (data.isdigit()):
                MSL = int(data)
                DataToMaster("ACK")
                Body = i2c.recv(MSL).decode()
               # print(Body)
                DataToMaster("ACK")

            elif (data == 'CHK'):
                Cheksum = checksum(Body)
                # print(Cheksum)
                cheksumlen = len(str(Cheksum))
                # print(type(cheksumlen))
                # print(cheksumlen)
                if (cheksumlen == 1):
                    pymsg = "00" + str(Cheksum)
                    DataToMaster(pymsg)
                elif (cheksumlen == 2):
                    pymsg = "0" + str(Cheksum)
                    # print("o + Cheksum = " +pymsg)
                    DataToMaster(pymsg)
                elif (cheksumlen == 3):
                    pymsg = str(Cheksum)
                    DataToMaster(pymsg)


            elif (data == 'OK_'):
                DataToMaster("ACK")

            elif (data == 'ERR'):
                DataToMaster("ACK")

            elif (data == 'WFU'):
                # start update
                BodyList = Body.split("*")
                DataToMaster("EWF")

            elif (data == 'EOS'):
                DataToMaster("EOS")

            elif (data == 'END'):
                DataToMaster("ACK")
                return BodyList
        except:
            #print("No update" )
            return None
