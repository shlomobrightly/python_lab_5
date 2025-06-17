def main():
    try_num  = 0
    num = int(input("Enter a natural number:"))
    
    for i in range(num + 1):
       try_num += i
    print("The triangle number in location %d is: %d" %(num, try_num))
    
    
main()
    
    
    
    
    
