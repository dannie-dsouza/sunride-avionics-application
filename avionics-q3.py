# def TimeToBin(Time):
#   Binary_Time = (int((Time%1000)/100))
#   Binary_Time = bin(Binary_Time)[2:]
#   while len(Binary_Time) < 4:
#     Binary_Time = "0"+Binary_Time
#   return Binary_Time


def compression(Time: int,NO2: int,Baro: int,Temp: int,Accel: float):

  # Time compression into 4 bits
  
  # if Time%1000 == 0:
  #   Time_Bit = "0000"
  # else:
  #   Time_Bit = TimeToBin(Time)


  # NO2 compression into 1 bit

  # if Time%500 == 0: # Am I expecting new data?
  if NO2 == 23:
    NO2_Bit = "1"

  elif NO2 == 0:
    NO2_Bit = "0"

  else:
    NO2_Bit = "0" #Erroneus data but coded so does not break the data collection

  # else: # No new data
  #   NO2_Bit = "0"


  # Barometer conversion into 8 bits
  if Baro <= 120 and Baro >= 75: # Making sure sensor data is within expected range
    # if Time%1000 == 0 or Time%1000 == 500 or Time%1000 == 300 or Time%1000 == 800: # Am I expecting new data?
    Baro = round((120 - Baro) * 5.6667)
    Baro_Bin = bin(Baro)[2:]
    while len(Baro_Bin) < 8:
      Baro_Bin = "0"+Baro_Bin
  else:
    Baro_Bin = '00000000' if Baro > 75 else '11111111' # Cheeky Ternery statment 🥵, mums AI dosen't have the class to do ts


  # Temp conversion
  if Temp <= 150 and Temp >= -10: # Making sure temp is in the right range
    # if Time%1000 == 0: # Am I expecting a new value?
    Temp = round((Temp + 10) * (255 / 160))
    Temp_Bin = bin(Temp)[2:]
    while len(Temp_Bin) < 8:
      Temp_Bin = "0"+Temp_Bin
  else:
    Temp_Bin = '00000000' if Temp < -10 else '11111111'


# Assuming +-16g's which is "Typical of an IMU sensor" according to a quick google.

# Understand that the Karman sieries rocket is likley to exceed 16g's during lauch so will make sure to handle data > 16g's

  if Accel <= 16 and Accel >= -16:
    Accel = round(Accel * (16383 / 16))
    if Accel < 0:
      Accel += 32768

    Accel_Bin = bin(Accel)[2:]
    while len(Accel_Bin) < 15:
        Accel_Bin = "0"+Accel_Bin
  else:
    Accel_Bin = '100000000000001' if Accel < 16 else '011111111111111'


  return NO2_Bit+Baro_Bin+Temp_Bin+Accel_Bin
  


def decompression(sensor_data):
  if len(sensor_data) != 32:
    return False,'INVALID DATA'
  NO2_Bit = sensor_data[0:1]
  Baro_Bin = sensor_data[1:9]
  Temp_Bin = sensor_data[9:17]
  Accel_Bin = sensor_data[17:]

  if NO2_Bit == '0':
    NO2 = 0
  else:
    NO2 = 23

  Baro = round(120 - (int(Baro_Bin,2)/5.667))

  Temp = round((int(Temp_Bin,2)*(160/255)) - 10)

  Accel = int(Accel_Bin, 2)

  if Accel >= 16384:
      Accel -= 32768

  Accel = round(Accel / (16383 / 16), 3)

  return NO2, Baro, Temp, Accel
  


def temporal_decompression(whole_data):
  for i in range((len(whole_data)//32)):
    print(100*i,decompression(whole_data[32*i:32*(i+1)]))












# Whoever is evaluating my code put whatever you want in here to test if it works (or don't), do whatever you like xx

test_data = [
    # Time, NO2, Baro, Temp, Accel
    (0,     0,  101,  20,  0.00),
    (100,   0,  100,  20,  0.05),
    (200,   0,  100,  20,  0.10),
    (300,   0,   99,  21,  0.15),
    (400,   0,   99,  21,  0.20),
    (500,  23,   98,  21,  0.30),
    (600,  23,   98,  21,  0.50),
    (700,  23,   97,  22,  0.80),
    (800,  23,   96,  22,  1.20),
    (900,  23,   95,  22,  1.80),
    (1000, 23,   94,  23,  2.50),
    (1100, 0 ,   90,  27,  3.20),
]


compressed_data = ''
for i in test_data:  
  compressed_data += compression(i[0],i[1],i[2],i[3],i[4])


temporal_decompression(compressed_data)


    
