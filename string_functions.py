# count() is a string method to count the occurance of a perticular letter in a string

str = "hi! Iam the $string value"
name = input("enter your name:")


print(str.count("$"))   #syntax of count is :  string_name.count("value_name")

print(str.replace("$","@")) #replace() used to replace something in string
                            #syntax- "string_name.replace("new_value","old_value")

print(str.find("!")) #find() returns the index value of mention letter
                     #syntax- "string_name.replace("value_name")"

print(str.endswith("ue"))#it returns true if string returns with substring 

print("lenth of the string is:",len("name"))

print(str[1:2])

reversed_str=''.join(reversed(str)) #reversed() used to reverse a string and join() used to join the string tuple and list element

print(reversed_str)


# average of 2 floating no