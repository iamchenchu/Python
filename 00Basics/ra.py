try:
  list1 = [10, 100, 20, 0, 'Hello', 4]

  for val in list1:
    print(10/val)
    

except ZeroDivisionError as e:
  print(f"Exception : {e}")
  pass