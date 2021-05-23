from parse_tree import Node

CFG = {
    "S": ["A", "$"],
    "A": ["b", "c", "$"]
}

# Works only in very simple cases.
def parser():
    rules = CFG["S"]
    input = "b"

    out, parse_tree = rec_parse("S", input, 0, "", Node("S"), [])
    print(out)
    print_parse_tree(parse_tree)


def rec_parse(nonterminal, input, input_iter, out, node, parse_tree):
    rules = CFG[nonterminal]
    match = False

    print("-----------------------------------")
    print("CFG: " + nonterminal)
    print(rules, out)

    for rule in rules:
        for i in range(len(rule)):
            node.add_children(rule[i])
            print("curr rule " + rule)
            print("current input " + input[input_iter])
            if rule[i].isupper() == True:
                print("out before rec", out)
                out, parse_tree = rec_parse(rule[i], input, input_iter, out, Node(rule[i]), parse_tree)
                print("out after rec ", out)
            else:
                if rule[i] == input[input_iter]:
                    out = out + rule[i]
                    input_iter += 1

            if out == input:
                match = True
                parse_tree.append(node)
                return out, parse_tree

        if match == True:
            parse_tree.append(node)
            return out, parse_tree

        print(out)

    print_parse_tree(parse_tree)

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


def print_parse_tree(parse_tree):
    print("-------------------------    PARSE TREE      -------------------------")
    for el in parse_tree:
        el.print_node()

parser()
