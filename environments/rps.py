import numpy as np

M = np.matrix([[0, -1, 1],
              [1, 0, -1],
              [-1, 1, 0]])

M_weighted_symmetric = np.matrix([[0, -3, 2],
                                [3, 0, -1],
                                [-2, 1, 0]])

M_weighted_nonsymmetric = np.matrix([[0, -6, 4],
                                    [3, 0, -5],
                                    [-2, 1, 0]])