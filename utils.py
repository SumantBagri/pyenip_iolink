def bool2byte(bitdata):
    val = 0
    bytedata = bytearray()
    for index, bit in enumerate(bitdata):
        if bit:
            val += 1 << index
        if index == 7:
            bytedata.append(val)
            val = 0
    return bytedata

def byte2bool(bytedata, size):
    bitdata = bool(byte & (1 << s) for byte in bytedata for s in range(8))
    return bitdata[:size*8]

def mergeOutput(conn, devices, outputdata):
    while True:
        for device in devices:
            if device.IOtype == 2:
                continue
            device.mergeDeviceOutput()
            for i in device.portRange:
                outputdata[i] = device.outputbytes[i]
            outputdata[device.writeEnablePort]=1
        conn.outAssem = byte2bool(outputdata, conn.outputsize)
        time.sleep(0.0075)

 