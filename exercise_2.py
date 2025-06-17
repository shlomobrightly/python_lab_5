def main():
    
    num = int(input("Enter a natural number:"))
    list_div =""
    if num < 0 or num%1 != 0:
        print("Input is not a natural number")
    else:
        amount_of_divs = 0
        for i in range (1, num +1):
            if num%i == 0:
                amount_of_divs +=1
                list_div += str(i) + " "
        print("The list of natural divisors of %d is %s" %(num,list_div))
        print("The amount of divisors is: %d" %(amount_of_divs))
    
    
main()
    
