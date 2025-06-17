def main():
    
    a1 = int(input("Enter the first element in a geometric sequence:"))
    q = int(input("Enter the quotient of a geometric sequence:"))
    n = int(input("Enter an index / position in a sequence - a natural number:"))
    
    f_seq = str(a1) + " "
    
    for i in range (1,n):
        a1*= q
        f_seq += str(a1) + " "
        
    
    
    
    print("the first %d elements in the sequence are: %s" %(n,f_seq))
main()
    

