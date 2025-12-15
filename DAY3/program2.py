input = str(input("Enter your String: "))
print("\nyour entered String: ",input)

# substring = s[start : end : step]
 # input = str("Hello Everyone my name is anurag manglekar")

 # Retrieve All Characters

print("\noutput:",input[:]) 

# Get All Characters Before or After a Specific Position

print("\noutput:",input[7:])

print("\noutput:",input[:7]) 

# Extract Characters Between Two Positions 

print("\noutput:",input[2:7])

# Get Characters at Specific Intervals 

print("\noutput:",input[::2])

print("\noutput:",input[2:9:2])

# Extract Characters Using Negative Indices

# Negative indexing is useful for accessing elements from the end of the String. The last element has an index of -1, the second last element -2 and so on.
print("\noutput:",input[:-2])  

print("\noutput:",input[-2:])  

print("\noutput:",input[-3:-8:-2]) 




