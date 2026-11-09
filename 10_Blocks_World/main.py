class BlocksWorld:
    def __init__(self):
        self.state = {"A": "B", "B": "table", "C": "table"}
        self.goal = {"A": "B", "B": "C", "C": "table"}

    def clear_block(self, block):
        return block not in self.state.values()

    def move(self, block, destination):
        if self.clear_block(block):
            print(f"Moving {block} from {self.state[block]} to {destination}")
            self.state[block] = destination

    def plan_moves(self):
        print("Initial State:", self.state)

        # Clear A from B so that B can be moved safely.
        if self.state["A"] == "B":
            self.move("A", "table")

        # Move B onto C, then restore A onto B.
        if self.state["B"] != "C":
            self.move("B", "C")
        if self.state["A"] != "B":
            self.move("A", "B")

        print("Final Goal State Reached:", self.state)

if __name__ == "__main__":
    BlocksWorld().plan_moves()
