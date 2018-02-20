# Computing Levenshtein distance between 2 strings

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Algorithm
# Step 1 - Create Matrix of required size
w, h = len(str2) + 1, len(str1) + 1
Matrix = [[0 for x in range(w)] for y in range(h)]

# Step 2 - Initialize Matrix
for i in range(w):
	Matrix[0][i] = i
for i in range(h):
	Matrix[i][0] = i

# Step 3 - Iteration
for i in range(1, h):
	for j in range(1, w):
		if str1[i-1] == str2[j-1]:
			t = 0
		else:
			t = 2
		Matrix[i][j] = min(Matrix[i-1][j]+1, Matrix[i][j-1]+1, Matrix[i-1][j-1]+t)


print("\nThe Levenshtein distance between strings "+str(str1)+" and "+str(str2)+" is "+str(Matrix[h-1][w-1])+"\n")

