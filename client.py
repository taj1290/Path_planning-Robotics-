#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 14:20:37 2023

@author: cr
"""

import pygame
import numpy as np
import socket
import sys

serverIP="127.0.0.1"
serverPort="33333"

tcpSocket   = socket.socket();
try:
    tcpSocket.connect((serverIP, serverPort));
    

except Exception as Ex:

    print("Exception Occurred: %s"%Ex);

 

    # Close the socket upon an exception

    tcpSocket.close();
