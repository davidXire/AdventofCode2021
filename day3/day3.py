def s1():
    i = 0
    j = 0
    line_len = 0
    count_0 = 0
    count_1 = 0
    gamma = ""
    epsilon = ""

    print("## STARTING ##") 
    file = open('day3/data.txt', 'r')
    lines = file.readlines()

    list_lines = [''] * len(lines)

    for index, line in enumerate(lines):
      list_lines[index] = list(line.strip('\n'))
    line_len = len(list_lines[0])

    #print (list_lines)
    while i < line_len:
      while j < len(lines):
        if (list_lines[j][i] == '0'):
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
      count_0 = 0
      count_1 = 0
      j = 0
      i += 1

    file.close()
    print("## RESULT ##")
    print("G:{}, E:{}".format(gamma, epsilon))
    print(binaryToDecimal(gamma) * binaryToDecimal(epsilon))
    print("## TERMINATE ##")

def binaryToDecimal(n):
    return int(n,2)