class Tree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def main():
    t = Tree(25, "+", 4)
    p = Tree(1, "a", t)

    print(p.right.left)

if __name__ == "__main__":
    main()