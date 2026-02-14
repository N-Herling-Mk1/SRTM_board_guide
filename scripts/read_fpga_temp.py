#!/usr/bin/python3
"""
SRTM FPGA Temperature Reader
Reads FPGA temperature from the SRTM board via OPC UA.

Usage:
    /usr/bin/python3 read_fpga_temp.py
"""

from opcua import Client
import time

OPCUA_URL = "opc.tcp://192.168.0.117:4841"
NODE_ID = "ns=2;s=SRTM.FPGA_temp"
PING_TIME = 10  # seconds

# DEFAULT = SecurityPolicy None, Anonymous
client = Client(OPCUA_URL)

print("------->>")
print(f">> pinging [{NODE_ID}] >> | for {PING_TIME} seconds..")
print("--------->>>")

try:
    client.connect()
    print("Connected to OPC UA server")
    node = client.get_node(NODE_ID)
    
    for i in range(PING_TIME):
        value = node.get_value()
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{ts} | FPGA_temp = {value}")
        time.sleep(1)

except Exception as e:
    print("ERROR:", e)

finally:
    try:
        client.disconnect()
    except Exception:
        pass
    print("Disconnected")

print(">>Program Finished>>>\n")
