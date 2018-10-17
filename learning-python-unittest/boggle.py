from string import ascii_uppercase
from random import choice

def make_grid(width, height):
    """
    Creates a grid to hold all the tiles for a boggle game
    """
    return {
        (row, col): choice(ascii_uppercase) 
        for row in range(height) 
        for col in range(width)
    }
    
def neighbours_of_position(coords):
    """
    Get neighbours of a given position
    """
    row = coords[0]
    col = coords[1]
    
    # Assign each of the neighbours from top -left to bottom right
    top_left = (row-1, col-1)
    top_center = (row-1, col)
    top_right = (row-1, col+1)
    
    left = (row, col-1)
    right = (row, col+1)
    
    bottom_left = (row+1, col-1)
    bottom_center = (row+1, col)
    bottom_right = (row+1, col+1)
    
    return [top_left, top_center, top_right,
    left, right,
    bottom_left, bottom_center, bottom_right]
    
def all_grid_neighbours(grid):
    """
    Get all possible neighbours for each position
    """
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours
    
def path_to_word(grid, path):
    """
    Add all of the letters to the path to a string
    """
    return ''.join([grid[p] for p in path])

    
def search(grid, dictionary):
    """
    Search through the paths to locate words by matching in a dictionary
    """
    neighbours = all_grid_neighbours(grid)
    paths = []
    full_words, stems = dictionary
    
    def do_search(path):
        word= path_to_word(grid, path)
        if word in full_words:
            paths.append(path)
        if word not in stems:
            return
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
                
    for position in grid:
        do_search([position])
        
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)
    
def get_dictionary(dictionary_file):
    """
    Load dictionary file
    """
    full_words, stems = set(), set()
    
    with open(dictionary_file) as f:
        for word in f:
            word= word.strip().upper()
            full_words.add(word)
            for i in range(1, len(word)):
                stems.add(word[:i])
    return full_words, stems
        
def main():
    """
    Executes the project
    """
    grid = make_grid(4,4)
    dictionary = get_dictionary("bogwords.txt")
    words = search(grid, dictionary)
    for word in words:
        print(word)
    print ("Found %s words" % len(words))
    
if __name__ == "__main__":
    main()