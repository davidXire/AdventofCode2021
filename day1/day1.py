def main():
    prev = 0
    current = 0
    count_inc = 0

    print("## STARTING ##")
    file = open('day1/data.txt', 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
      current = int(line)
      if index != 0:
        if current > prev:
          count_inc += 1
      prev = current
    
    file.close()
    print("## RESULT ##")
    print(count_inc)
    print("## TERMINATE ##")

def main_p2():
    prev_sum = 0
    sum = 0
    count_inc = 0
    position = 0
    index = 0

    print("## STARTING ##")
    file = open('day1/data.txt', 'r')
    lines = file.readlines()
    nb = len(lines)

    while index < nb:
      sum += int(lines[index])
      if position == 2:
        if sum > prev_sum:
          if (prev_sum != 0):
            count_inc += 1
            print ("{} (increased)".format(sum))
          else:
            print ("{} (N/A - no previous sum)".format(sum))
        else:
          print ("{} (decrease)".format(sum))
        prev_sum = sum
        sum = 0
        index -= 2
        position = -1
      position += 1
      index += 1
    
    file.close()
    print("## RESULT ##")
    print(count_inc)
    print("## TERMINATE ##")