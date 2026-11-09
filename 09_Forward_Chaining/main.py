knowledge_base = [
    (["cough", "fever"], "flu"),
    (["sore_throat", "runny_nose"], "cold"),
    (["sore_throat"], "fever")
]
facts = {"cough", "sore_throat"}

def forward_chaining(facts, rules):
    facts = set(facts)
    changed = True
    while changed:
        changed = False
        for conditions, conclusion in rules:
            if all(condition in facts for condition in conditions):
                if conclusion not in facts:
                    facts.add(conclusion)
                    changed = True
    return facts

if __name__ == "__main__":
    final_facts = forward_chaining(facts, knowledge_base)
    if "flu" in final_facts:
        print("The patient is diagnosed with flu.")
    elif "cold" in final_facts:
        print("The patient is diagnosed with cold.")
    else:
        print("No conclusive diagnosis could be made.")
    print("Inferred facts:", sorted(final_facts))
