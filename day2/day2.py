def s1():
    list_h_d = [0,0]
    print("## STARTING ##")
    file = open('day2/data.txt', 'r')
    lines = file.readlines()
    
    for index, line in enumerate(lines):
      current = line.split(" ")
      if current[0] == "forward":
        list_h_d[0] += int(current[1])
      elif current[0] == "down":
        list_h_d[1] += int(current[1])
      else: #UP
        list_h_d[1] -= int(current[1])

    file.close()
    print("## RESULT ##")
    print(list_h_d)
    print((list_h_d[0]*list_h_d[1]))
    print("## TERMINATE ##")

def s2():
    list_h_d_a = [0,0,0]
    print("## STARTING ##")
    file = open('day2/data.txt', 'r')
    lines = file.readlines()
    
    for index, line in enumerate(lines):
      current = line.split(" ")
      if current[0] == "forward":
        list_h_d_a[0] += int(current[1])
        list_h_d_a[1] += (list_h_d_a[2] * int(current[1]))
      elif current[0] == "down":
        list_h_d_a[2] += int(current[1])
      else: #UP
        list_h_d_a[2] -= int(current[1])

    file.close()
    print("## RESULT ##")
    print(list_h_d_a)
    print((list_h_d_a[0]*list_h_d_a[1]))
    print("## TERMINATE ##")