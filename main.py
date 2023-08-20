# Function for hex to binary conversion and vice versa
def hex_bin(key, typ):
  h_b = {'0': "0000", '1': "0001", '2': "0010", '3': "0011", '4': "0100",'5': "0101",'6': "0110",'7': "0111",
         '8': "1000", '9': "1001", 'A': "1010", 'B': "1011", 'C': "1100",'D': "1101",'E': "1110",'F': "1111"}

  b_h = {'0000': '0','0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
         '1000': '8','1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

  K = ''
  # Converts hex to binary
  if typ.lower() == 'b':
    for i in key:
        K += h_b[i]
        
  # Converts binary to hex
  else:
    for i in range(0, len(key), 4):
      x = key[i:i+4]
      K += b_h[x]

  return K

# Func to perfom XOR operation on binary numbers stored in a string
def xor(a, b):
    ans = ""

    for i in range(len(a)):
        if (a[i] == b[i]):
            ans += "0"
        else:
            ans += "1"
            
    return ans

# Function to perform RotWord operation
def RotWord(key):
  x = key[:2]
  key = key[2:] + x
  
  return key

# Function to perform SubWord operation
def SubWord(key):
  co_ord = {'A' : 10, 'B' : 11, 'C' : 12, 'D': 13, 'E': 14, 'F': 15}

  sBox = [['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'],
          ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'],
          ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'],
          ['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'],
          ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'],
          ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'],
          ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'],
          ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'],
          ['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'],
          ['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'],
          ['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'],
          ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'],
          ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'],
          ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'],
          ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'],
          ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']]
  
  k = ''

  for i in range(0, len(key), 2):
    j = key[i:i+2]
    x, y = j[0], j[1]

    if ord(x) >= 65:
      x = co_ord[x]
    else:
      x = int(x)

    if ord(y) >= 65:
      y = co_ord[y]
    else:
      y = int(y)
      
    k += sBox[x][y]

  return k

# Generating 44 words of key using calculated value for temporary words
rcon = ['01000000', '02000000', '04000000', '08000000', '10000000',
        '20000000', '40000000', '80000000', '1B000000', '36000000']

ciph_key = '2475A2B33475568831E2120013AA5487'

w = [ciph_key[i:i+8] for i in range(0, 32, 8)]

r = 0
for i in range(40):
  if (i+4)%4 == 0:
    # Calc 't' value for each round
    t = hex_bin(xor(hex_bin(SubWord(RotWord(w[i+3])), 'b'), hex_bin(rcon[r], 'b')), 'h')

    w.append(hex_bin(xor(hex_bin(t, 'b'), hex_bin(w[i], 'b')), 'h'))
    
    r+=1
    
  else:
    w.append(hex_bin(xor(hex_bin(w[i+3], 'b'), hex_bin(w[i], 'b')), 'h'))

for i in range(len(w)):
  print(f'W{i}: \t{w[i]}')