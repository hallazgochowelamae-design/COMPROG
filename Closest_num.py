
number = 300

def find_closest_number():

   n1 = int(input("Enter your first number: "))
   n2 = int(input("Enter your second number: "))
   n3 = int(input("Enter your third number: "))


   my_list= [n1,n2,n3]
   
   if n1 == n2 ==n3:
       print(f"A is {n1}, B is {n2}, and C is {n3}. All numbers are equal, so all are closest to 300.")
       return n1
   else:
       closest_num = min(my_list, key=lambda x: abs (x - number))
       print(f"The closest number to {number} is {closest_num}")
       return closest_num
       
find_closest_number()       