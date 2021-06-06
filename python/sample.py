def main():
  
  print("Sample python program..")
  # Taking input from the user
  name = input("Enter your name: ")
  
  # Output
  print("Hello, " + name)
  
  # taking three inputs at a time
  x, y, z = input("Enter a three value: ").split()
  print("Total number of students: ", x)
  print("Number of boys is : ", y)
  print("Number of girls is : ", z)
  print()

  
  #Define multiple variables
  c1, c2, c3, c4  = 0, 0, 0, 0
  
  #Define multiple list
  alist, blist, clist, dlist, elist = ([] for i in range(5))
  
if __name__ == "__main__":
  
    main()
