
def num_to_base(num,base):
   convertString = "0123456789ABCDEF"
   if num < base:
      return convertString[num]
   else:
      return num_to_base(num//base,base) + convertString[num%base]
