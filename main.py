#!/usr/bin/env python3

from pyenip.ethernetip import EtherNetIP

HOSTNAME = "192.1682.120.200"
BROADCAST = "192.168.255.255"

BANNER_INPUT_SIZE = 456
BANNER_OUTPUT_SIZE = 456

DXM_TO_HOST_PLC_REGISTER_INSTANCE = 100
HOST_PLC_TO_DXM_REGISTER_INSTANCE = 112
CONFIG_REGISTER_INSTANCE = 128 # where does this come from ?

def main():
    enipManager = EtherNetIP(HOSTNAME)
    enipConn = enipManager.explicit_conn()
    
    print(f"Configure with {BANNER_INPUT_SIZE} input bytes and {BANNER_OUTPUT_SIZE} output bytes")

    enipManager.registerAssembly(enipManager.ENIP_IO_TYPE_INPUT, BANNER_INPUT_SIZE, DXM_TO_HOST_PLC_REGISTER_INSTANCE, enipConn)
    enipManager.registerAssembly(enipManager.ENIP_IO_TYPE_OUTPUT, BANNER_OUTPUT_SIZE, HOST_PLC_TO_DXM_REGISTER_INSTANCE, enipConn)

    enipManager.startIO()

    enipConn.registerSession()
    enipConn.sendFwdOpenReq(inputinst=DXM_TO_HOST_PLC_REGISTER_INSTANCE, outputinst=HOST_PLC_TO_DXM_REGISTER_INSTANCE, configinst=CONFIG_REGISTER_INSTANCE)
    enipConn.produce()



