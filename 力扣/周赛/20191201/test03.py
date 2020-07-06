import numpy as np
class Solution:
    def countSquares(self, matrix):
        numbers=[0 for k in range(len(matrix))]
        for i in range(len(matrix)):
            index = 0
            for j in range(len(matrix[i])):

                if matrix[i][j]==1:

                    numbers[index]=numbers[index]+1
                    add_=1
                    while True:
                        if i+add_<=len(matrix)-1 and j+add_<=len(matrix[i])-1:
                            matrix_a=np.array(np.array(matrix)[i:i+add_+1,j:j+add_+1])
                            matrix_b=np.ones((add_+1,add_+1))
                            if matrix_a.all()==matrix_b.all():
                                add_+=1
                                index += 1
                                numbers[index]=numbers[index]+1
                            else:
                                add_=1
                                index = 0
                                break
                        else:
                            add_=1
                            index = 0
                            break
        print(sum(numbers))
        for i in range(len(numbers)):
            if numbers[i]>0:
                new_in=i+1
                print('边长为',new_in,'的正方形有',numbers[i],'个')
        return sum(numbers)
matrix =[

        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ]
a=Solution()
a.countSquares(matrix)