from operator import itemgetter
import numpy as np

def binaryToDecimal(n):
    return int(n,2)

def createListFromFile ():
  file = open('day3/data.txt', 'r')
  lines = file.readlines()
  inputlist = [''] * len(lines)

  for index, line in enumerate(lines):
    inputlist[index] = list(line.strip('\n'))

  file.close()
  return inputlist

def s1():
    i = j = line_len = nb_line = count_0 = count_1 = 0
    gamma = epsilon = ""

    print("## STARTING S1 ##") 
    inputlist = createListFromFile()

    line_len = len(inputlist[0])
    nb_line = len(inputlist)

    while i < line_len:
      while j < nb_line:
        if (inputlist[j][i] == '0'):
          count_0 += 1
        else:
          count_1 += 1
        j += 1
      if (count_0 > count_1):
        gamma = gamma + "0"
        epsilon = epsilon + "1"
      else:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
      count_0 = count_1 = j = 0
      i += 1

    print("## RESULT S1 ##")
    # print("G:{}, E:{}".format(gamma, epsilon))
    print(binaryToDecimal(gamma) * binaryToDecimal(epsilon))
    print("## TERMINATE S1 ##")

def s2():
    i = line_len = count_0 = count_1 = 0

    print("## STARTING S2##") 
    inputlist = createListFromFile()
    line_len = len(inputlist[0])

    oxygen = inputlist.copy()
    co2 = inputlist

    while i < line_len:
      oxygen.sort(key=itemgetter(i), reverse=True)
      output = list(map(itemgetter(i), oxygen))
      count_1 = output.count('1')
      count_0 = output.count('0')
      if (count_1 >= count_0):
        del oxygen[(count_1):(count_1+count_0)]
      #  print("## DEL 0 ##")
      else:
        del oxygen[0:(count_1+1)]
      #  print("## DEL1 ##")
      #print(np.matrix(oxygen))
      if (len(oxygen) == 1):
        break
      count_0 = count_1 = 0
      i += 1

    i = 0
    while i < line_len:
      co2.sort(key=itemgetter(i), reverse=True)
      output = list(map(itemgetter(i), co2))
      #print("## BEFORE OUTPUT ## {}".format(i))
      #print(np.matrix(output))
      count_1 = output.count('1')
      count_0 = output.count('0')
      if (count_1 < count_0):
        del co2[(count_1):(count_1+count_0)]
        #print("## DEL 0 ## {} - {}".format(count_1, count_0))
      else:
        del co2[0:(count_1)]
        #print("## DEL 1 ##")
      if (len(co2) == 1):
        break
      count_0 = count_1 = 0
      i += 1
      #print(np.matrix(co2))

    print("## RESULT S2 ##")
    # print(binaryToDecimal(''.join(co2[0])))
    # print(binaryToDecimal(''.join(oxygen[0])))
    # print("G:{}, E:{}".format(gamma, epsilon))
    print(binaryToDecimal(''.join(co2[0])) * binaryToDecimal(''.join(oxygen[0])))
    print("## TERMINATE S2 ##")
