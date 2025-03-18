# Convolution - Benjamin Ortiz

# It is an operation between two number tables, usually between an image and weights.

# Step 1: padding the left array with zeros. We do this so that the output array has
# the same dimensions as the input array. (We dont want to lose information).

# Step 2: We "flip" the weights array. Do we do this in practice? If so, how many zeroes do we add?

# Step 3: We compute the sum.


image = [[-1, 1], [-2, 2]]
weights = [[0, 2],[1, 3]]

zeroesToPad = len(weights) - 1

arr = [0 for element in range(len(image[0]))]

# Add to the top    
image.insert(0, arr)

# Add to the left
for i in range(0, len(image)):
    for j in range(0, zeroesToPad):
        image[i].insert(0, 0)

# Add to the right
for i in range(0, len(image)):
    for j in range(0, zeroesToPad):
        image[i].append(0)

# Add to the bottom
image.append(arr)

# Flip the weights
weights = weights[::-1]
for i in range(0, len(weights)):
    weights[i] = weights[i][::-1]

print("Flipped Weight matrix:")
for i in range(0, len(weights)):
    print(weights[i])

# Computing the sum
# How many pointers do we need?
sum = 0
for i in range(0, (len(weights) + 1)):
    for j in range(0, (len(weights) + 1)):
        sum += image[i][j] * weights[i][j]
    
        
print("Sum: ", sum)

print("Image matrix:")
# Print the image
for i in range(0, len(image)):
    print(image[i])
