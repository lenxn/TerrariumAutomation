# temperature_controller.py
# Author: Stefan Lengauer
import os

FILE_NAME = 'w1_slave'
FILE_PATH = './'
MIN_TEMPERATURE = 25.0
MAX_TEMPERATURE = 27.0

def getTemp():
  file_handle = open(FILE_PATH + FILE_NAME)
  text = file_handle.read()
  file_handle.close()
  second_line = text.split("\n")[1]
  temperature_data = second_line.split(" ")[9]
  temperature = float(temperature_data[2:])
  temperature = temperature / 1000
  return temperature

def turnOnHeating():
  print("[+] Turning on Heating.")
  os.system("/home/pi/raspberry-remote/send 11011 1 1")

def turnOffHeating():
  print("[+] Turning off Heating.")
  os.system("/home/pi/raspberry-remote/send 11011 1 0"

def writeToDataLog():
  # [YYYY-MM-DD:HH:MM:SS][tmp1, tmp2, tmp3][hum1, hum2] <starting heating>

def writeToErrorLog():
  # [YYYY-MM-DD:HH:MM:SS] Temperature Sensor 1 exceeding Limits (TT)
  

def main():
  temp = getTemp()
  print("[*] Temperature: " + str(temp))
  if(temp < MIN_TEMPERATURE):
    turnOnHeating()
  if(temp > MAX_TEMPERATURE):
    turnOffHeating()
  
if __name__ == '__main__':
  main()