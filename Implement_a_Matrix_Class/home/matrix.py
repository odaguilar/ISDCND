import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
def dot_product(vector_one, vector_two):
    """
    Calculates the dot product between two vectors.  
    """
    product = 0
    for i in range(len(vector_one)):
        product += vector_one[i] * vector_two[i]
    return product

def get_row(matrix, row):
    """
    Gets the row from a matrix
    """
    return matrix[row]
    
def get_column(matrix, column_number):
    """
    Gets the column from a matrix
    """
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][column_number])
    return column

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        
        # Check if is square
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        # Check if is more than 2x2
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        
        # For 1x1 Matrix
        if self.h  == 1:
            det = self.g[0][0]
        
        # For 2x2 Matrix
        elif self.h == 2:
            det = self.g[1][1] * self.g[0][0] - self.g[0][1] * self.g[1][0]
            
        else:
            raise(NotImplementedError, "Sorry but i can't calculate a matrix largerer than 2x2  :( ")
        return det

    def trace(self):
        """
        Calculates the trace of a matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        
        trace = 0 
        for i in range(self.h):
            trace += self.g[i][i]
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        inverse = zeroes(self.h, self.w)
        
        
        determinant_matrix = 1 / self.determinant()
        
        # For 1x1 Matrix
        if self.h == 1:
            inverse[0][0] = determinant_matrix

        # For 2x2 Matrix
        # According to the formula:
        #
        # Inverse_matrix = 1/determinant * ([d,-b
        #                                  -c, a])
        #
        elif self.h == 2:   
            inverse[1][1] = self.g[0][0] * determinant_matrix
            inverse[0][1] = -self.g[0][1] * determinant_matrix
            inverse[1][0] = -self.g[1][0] * determinant_matrix
            inverse[0][0] = self.g[1][1] * determinant_matrix
            
        else:
            raise(NotImplementedError, "Sorry but i can't calculate a matrix largerer than 2x2  :( ")
        
        return inverse
    
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        
        # The heigth is the wide, and the wide is the heigth
        transpose = zeroes(self.w, self.h)
        
        for i in range(self.h):
            for j in range(self.w):
                transpose.g[j][i] = self.g[i][j]
        return transpose
    
    def is_square(self):
        """
        Checks if we got an squared Matrix.
        """
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.
        Example:
        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]
        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        
        # We create a list that will store the sum of A + B
        suma = []
        
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j] + other[i][j])
            suma.append(row)
        return Matrix(suma)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)
        Example:
        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        # We create a list that will store the product of A * -1
        neg = []
        
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j] * -1)
            neg.append(row)
        return Matrix(neg)
    
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        
        # We create a list that will store the substraction of A - B
        sub = []
        
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j] - other[i][j])
            sub.append(row)
        return Matrix(sub)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        
        # a_rows: rows of the first input of our function
        # b_columns: columns of the second input of our function
        
        a_rows = self.h
        b_columns = other.w
        
        # We create a list that will store the dot_product(A(row),B(column)
        mul = []
        
        for i in range(a_rows):
            row = []
            for j in range(b_columns):
                row.append(dot_product(get_row(self.g,i),get_column(other.g,j)))
            mul.append(row)
        return Matrix(mul)
    
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.
        Example:
        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            rmul = Matrix(self.g)
            
            for i in range(self.h):
                for j in range(self.w):
                    rmul[i][j] = self.g[i][j] * other
            return(rmul)