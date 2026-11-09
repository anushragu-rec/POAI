def unify(x, y, substitution=None):
    if substitution is None:
        substitution = {}
    if x == y:
        return substitution

    if isinstance(x, str) and x.startswith("?"):
        return unify_variable(x, y, substitution)
    if isinstance(y, str) and y.startswith("?"):
        return unify_variable(y, x, substitution)

    if isinstance(x, (list, tuple)) and isinstance(y, (list, tuple)) and len(x) == len(y):
        for left, right in zip(x, y):
            substitution = unify(left, right, substitution)
            if substitution is None:
                return None
        return substitution
    return None

def unify_variable(variable, value, substitution):
    if variable in substitution:
        return unify(substitution[variable], value, substitution)
    if isinstance(value, str) and value in substitution:
        return unify(variable, substitution[value], substitution)
    substitution[variable] = value
    return substitution

def substitute(term, theta):
    if isinstance(term, (list, tuple)):
        return tuple(substitute(part, theta) for part in term)
    return theta.get(term, term) if isinstance(term, str) else term

def resolve(query, facts, rules):
    if query in facts:
        return True
    for premise, conclusion in rules:
        theta = unify(conclusion, query, {})
        if theta is not None:
            grounded_premises = [substitute(item, theta) for item in premise]
            if all(resolve(p, facts, rules) for p in grounded_premises):
                return True
    return False

if __name__ == "__main__":
    print("Unification:", unify(["Human", "?x"], ["Human", "John"]))
    facts = {("Human", "John")}
    rules = [
        ([("Human", "?x")], ("Mortal", "?x"))
    ]
    query = ("Mortal", "John")
    print("Query is resolved: John is Mortal" if resolve(query, facts, rules)
          else "Query could not be resolved")
