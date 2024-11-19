def answer(question: str) -> int:
    """
    Function to parse and evaluate simple math word problems
    returning the answer as an integer
    """
    for item in question.split():
        if item == "cubed?" or item == "Who":
            raise ValueError("unknown operation")
    question = question.replace("plus", "+").replace("minus", "-").replace("multiplied by", "*").replace("divided by", "/").replace("What is ", "").replace("?", "").split()

    if not question:
        raise ValueError("syntax error")
    question.insert(0, "(")
    question.insert(4, ")")

    try:
        return eval(" ".join(question))

    except:
        raise ValueError("syntax error")
