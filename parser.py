CFG = {
    "S": ["A", "$"],
    "A": ["b", "c", "$"]
}

# Works only in very simple cases.
def parser():
    rules = CFG["S"]
    input = "b"

    out = rec_parse("S", input, 0, "")


def rec_parse(nonterminal, input, input_iter, out):
    rules = CFG[nonterminal]
    match = False

    print("-----------------------------------")
    print("CFG: " + nonterminal)
    print(rules, out)

    for rule in rules:
        for i in range(len(rule)):
            print("curr rule " + rule)
            print("current input " + input[input_iter])
            if rule[i].isupper() == True:
                print("out before rec", out)
                out = rec_parse(rule[i], input, input_iter, out)
                print("out after rec ", out)
            else:
                if rule[i] == input[input_iter]:
                    out = out + rule[i]
                    input_iter += 1

            if out == input:
                match = True
                return out

        if match == True:
            return out

        print(out)


def parse_tmp(rule, input, input_iter, out):
    for i in range(len(rule)):
        print("curr rule " + rule)
        print("current input " + input[input_iter])
        if rule[i].isupper() == True:
            out = rec_parse(rule[i], input, input_iter, out)
        else:
            if rule[i] == input[input_iter]:
                out = out + rule[i]
                input_iter += 1

        if input_iter == len(input) and out == input:
            return

        print(out)

    return out


parser()
