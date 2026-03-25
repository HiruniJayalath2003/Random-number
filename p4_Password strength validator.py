# 04-Password strength validator - Hiruni

print("\n=====PASSWORD VALIDATOR=====")
while True:
   password=input("\nEnter password :")

#check length
   if len(password)>=8:
      is_long=True
   else:
      is_long=False  

#check other requirements
   is_uppercase= False
   is_lowercase=False
   is_digit=False
   is_special=False
   special_character= ("!@#$%^&*")    

   for char in password:
      if char.isupper():
         is_uppercase= True
      elif char.islower():
         is_lowercase=True
      elif char.isdigit():
         is_digit=True
      elif char in special_character:
         is_special=True  

#feedback
   print("\n----PASSWORD ANALYSIS----")      
   if is_long:
      print("\n[OK] Length requitrment met")
   else:
      print("\n[x] Too short (minimum 8 characters)") 
   if is_uppercase:
      print("\n[OK] Contain uppercase letter.")
   else:
      print("\n[x] Missing uppercase letter")  
   if is_lowercase:
      print("\n[OK] Contain lowercase letter")
   else:
      print("\n[x] Missing lowercase letter")  
   if is_digit:
      print("\n[OK] Contain digit")
   else:
      print("\n[x] Mising digit")     
   if is_special:
      print("\n[OK] Contain special character")
   else:
      print("\n[x] Mising special character")             

#calculate password strength
   count=0
   for check in[is_long , is_uppercase , is_lowercase , is_digit , is_special]:
      if check:
       count=count+1

#special message
   if count <=1:
      print("STRENGTH= WEAK")
      print("Try again !") 
   elif count>=2 and count<=4:
      print("STRENGTH= MEDIUM") 
      print("Try again !") 
   else:
      print("STRENGTH= STRONG")
      print("\nPassword accepted ! Your account is secure.")    
      break 