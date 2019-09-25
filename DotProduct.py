"Dot product between vectors a and b is defined as sum(a1b1+a2b2+a3b3+...+anbn"
def vectors(vector_size):
    '''Creates two vectors with given size'''
    vector1 = []
    vector2 = []
    for i in range(2):
        if i == 0:
            for j in range(vector_size):
                print("Element no {}:".format(j+1), end = ' ')
                element = float(input())
                vector1.append(element)
        if i == 1:
            for j in range(vector_size):
                print("Element no {}:".format(j+1), end = ' ')
                element = float(input())
                vector2.append(element)
    return vector1, vector2

def dot_sum(vector1, vector2, vector_size):
    dot_sum = 0
    for i in range(vector_size):
        dot_sum += vector1[i]*vector2[i]
    return dot_sum





def main():
    vector_size = int(input("Input vector size: "))
    vector1, vector2 = vectors(vector_size)
    print("Dot product is:", dot_sum(vector1, vector2, vector_size))

main()