# def main(x):
#     """
#     Given an integer x, return true if x is palindrome integer.
#     An integer is a palindrome when it reads the same backward as forward.

#     Args:
#         x(int): parameter x
#     Returns:
#         bool: answer
#     """

#     return

n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")