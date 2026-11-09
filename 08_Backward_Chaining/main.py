knowledge_base = {
    "flu": [["cough", "fever"]],
    "fever": [["sore_throat"]]
}
facts = {"sore_throat", "cough"}

def backward_chaining(goal, visiting=None):
    if visiting is None:
        visiting = set()
    if goal in facts:
        return True
    if goal in visiting or goal not in knowledge_base:
        return False
    visiting = visiting | {goal}
    for conditions in knowledge_base[goal]:
        if all(backward_chaining(condition, visiting) for condition in conditions):
            return True
    return False

if __name__ == "__main__":
    query = "flu"
    if backward_chaining(query):
        print(f"The patient is diagnosed with {query}.")
    else:
        print(f"The patient does NOT have {query}.")
