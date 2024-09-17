"""
NAME: Priyanka Ghimire
SID: @03086787
"""

class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = set(dictionary)
        self.solutions = set()
        self.n = len(grid)
        self.m = len(grid[0]) if grid else 0  # Handle case when grid is empty
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def setGrid(self, grid):
        self.grid = grid
        self.n = len(grid)
        self.m = len(grid[0]) if grid else 0

    def setDictionary(self, dictionary):
        self.dictionary = set(dictionary)

    def getSolution(self):
        self.solutions = set()
        for i in range(self.n):
            for j in range(self.m):
                self.dfs(i, j, "", set())
        return sorted(self.solutions)

    def dfs(self, i, j, current_word, visited):
        if (i, j) in visited:
            return
        
        current_word += self.grid[i][j]

        # Handle "Qu" and "St"
        if current_word.endswith("Qu") or current_word.endswith("St"):
            pass  # Logic for handling these should go here
        
        if len(current_word) >= 3 and current_word in self.dictionary:
            self.solutions.add(current_word)
        
        visited.add((i, j))
        for direction in self.directions:
            new_i, new_j = i + direction[0], j + direction[1]
            if 0 <= new_i < self.n and 0 <= new_j < self.m:
                self.dfs(new_i, new_j, current_word, visited.copy())
        
        visited.remove((i, j))


def main():
    grid = [["T", "W", "Y", "R"],
            ["E", "N", "P", "H"], 
            ["G", "Z", "Qu", "R"], 
            ["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()

