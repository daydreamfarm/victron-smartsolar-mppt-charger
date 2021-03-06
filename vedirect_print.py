#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse, os
from vedirect import Vedirect
# from vedirect import Smartsolar

def print_data_callback(packet):
    print(packet)
#    print(":".join("{:02x}".format(ord(c)) for c in packet))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process VE.Direct protocol')
    parser.add_argument('--port', help='Serial port')
    parser.add_argument('--timeout', help='Serial port read timeout', type=int, default='60')
    args = parser.parse_args()
    ve = Vedirect(args.port, args.timeout)
    print("FINAL RESULT = ",ve.send_command('7F7ED00'))
    # print(ve.read_frame())
    # raw_data = ve.read_data_single()
    # print_data_callback(raw_data)
    #print(ve.read_data_callback(print_data_callback))
    # print(ve.send_command(':7F7ED00'))
    # print("Oct:",ve.send_command(':1'))
    # ss = Smartsolar(args.port, args.timeout)
    # print(ss.readText())
    # ver = ss.pingDevice()
    # print("Ver: " + ver)
    # print(ss.getParam("BatteryFloatVoltage"))
    # print(ss.getParam("BatteryAbsorptionVoltage"))
    # print(ss.getParam("SystemTotal"))
    # print(ss.appVersion())
