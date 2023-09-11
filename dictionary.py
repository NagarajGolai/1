n = input("Enter your name (case sensitive) : ")
c = n.lower()

members = {'Suresh':12, 'Ramesh':18,'Siddu':12,'Satish':18,'Kalmesh':28}

if c in members.keys():
	print(f"Their share is {members[n]}%\n")
	
elif n not in members.keys():
	print('\n',n,''' is not present in the dictionary\n Do you want to update this name ? (Press "y" for yes and "n" for no)\n''')
	a = input(" ")
	if a == 'y'.lower():
		upvalue = int(input("Enter their share : "))
		members[n] = upvalue
		print(f"Updated dictionary : {members}\n")	
		
	elif a == 'n'.lower():
		print(" ")

b=0
for i in members.values():
	b += i

print(f"Number of shares : {len(members)}")
print(f"Sum of all shares : {b}")