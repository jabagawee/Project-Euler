triangle = [map(int,x.split(' ')) for x in open('triangle.txt').read().strip().split('\n')]

length_to = [[0 for item in row] for row in triangle]
length_to[0][0] = triangle[0][0]

for i in xrange(len(triangle)-1):
    for j in xrange(len(triangle[i])):
        if length_to[i+1][j] <= length_to[i][j] + triangle[i+1][j]:
            length_to[i+1][j] = length_to[i][j] + triangle[i+1][j]
        if length_to[i+1][j+1] <= length_to[i][j] + triangle[i+1][j+1]:
            length_to[i+1][j+1] = length_to[i][j] + triangle[i+1][j+1]

print max([length for length in length_to[-1]])
