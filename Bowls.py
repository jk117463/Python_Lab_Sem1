# #using loop
print("Enter the rows  : ")  # Requesting user input
limit = input()
Bowl = 0
for i in range (int(limit)+1):
    Bowl = Bowl + i
print("Bowls :", Bowl)


#using recursive function
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("Enter the rows  : ")  # Requesting user input
limit = input()
print("\n\nRecursion Example Results")
print(tri_recursion(int(limit)))


#using sequence
# def bowls_sequence(n):
#     # TODO ...
#     return n