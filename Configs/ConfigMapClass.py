from Map import Map

class ConfigMap:
    def __init__(self, width, height):
        self.map_array = [Map([[0, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0],
                    [2, 0, 3, 0, 3],
                    [0, 0, 0, 0, 2],
                    [1, 0, 1, 0, 1]],
                   [[(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 4)], [0, 1, 1, 0, 0, 3, 3, 0]], width, height,
                   20, 100),
        Map([[1, 0, 0, 0, 1],
                    [1, 2, 1, 0, 1],
                    [0, 0, 0, 0, 0],
                    [0, 1, 0, 4, 0],
                    [0, 1, 3, 0, 0]],
                   [[(0, 4), (0, 3), (0, 2), (1, 2), (2, 2), (3, 2), (3, 1), (3, 0), (2, 0), (1, 0)],
                    [0, 0, 3, 3, 3, 0, 0, 1, 1, 1]], width, height,
                   20, 100),
        Map([[0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 1, 4, 0, 0, 1],
                    [0, 5, 2, 0, 0, 1, 0],
                    [0, 0, 1, 0, 0, 3, 0],
                    [1, 0, 0, 0, 1, 0, 0]],
                   [[(0, 3), (5, 1), (4, 1), (4, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4), (1, 3)], [3, 0, 3, 0, 3, 0, 0, 3, 3, 2]], width, height,
                   20, 100),
        Map([[0, 1, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 3, 0],
                    [1, 0, 6, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 1],
                    [5, 0, 4, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 1, 0],
                    [1, 0, 0, 2, 0, 0, 0]],
                   [[(2, 0), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (4, 4), (4, 3), (4, 2), (3, 2)], [2, 1, 2, 2, 2, 2, 3, 3, 3, 0, 0, 0, 1, 2]], width,
                   height,
                   20, 100),
        Map([[0, 0, 0, 0, 1, 0, 0],
                    [1, 6, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 5],
                    [1, 0, 1, 7, 0, 0, 1],
                    [2, 0, 0, 0, 0, 0, 1],
                    [0, 1, 0, 3, 4, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0]],
                   [[(6, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (3, 2), (2, 2), (1, 2), (1, 3), (1, 4)], [1, 0, 0, 0, 0, 1, 1, 2, 1, 1, 2, 2, 2]], width, height,
                   20, 100),
        Map([[0, 0, 1, 0, 0, 6, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [0, 1, 1, 0, 0, 0, 0],
                    [0, 0, 3, 0, 4, 0, 1],
                    [0, 1, 0, 5, 0, 0, 2],
                    [1, 0, 0, 0, 0, 0, 1],
                    [0, 1, 0, 0, 7, 0, 0]],
                   [[(2, 6), (2, 5), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1)], [0, 3, 3, 3, 0, 0, 0, 0, 1, 1, 1, 1, 2]], width, height,
                   20, 100)]

    def get_map_array(self):
        return self.map_array