from parse_tree import Node


def parser(CFG, input):
    print(CFG)
    rules = CFG['S']
    input = input[:-1]

    if CFG != {}:
        out, parse_tree = rec_parse(CFG, "S", input, 0, "", Node("S"), [])
        print("End of input parsing")
        print(out)
        print_parse_tree(parse_tree)


def rec_parse(CFG, nonterminal, input, input_iter, out, node, parse_tree):
    rules = CFG[nonterminal]
    match = False

    print("-----------------------------------")
    print("CFG: " + nonterminal)
    print(rules, out)

    parse_tree.append(node)

    for rule in rules:
        print(rule)
        match = False
        for i in range(len(rule)):
            node.add_children(rule[i])
            print_parse_tree(parse_tree)

            print("curr rule " + rule)
            print("current input " + input[input_iter])
            if rule[i].isupper() == True:
                print("out before rec", out)
                out, parse_tree = rec_parse(CFG, rule[i], input, input_iter, out, Node(rule[i]), parse_tree)
                print("out after rec ", out)
            else:
                if rule[i] == input[input_iter]:
                    out = out + rule[i]
                    input_iter += 1
                else:
                    # backtracking:
                    for el in node.children:
                        out = out.replace(el, "")
                        input_iter = input_iter - 1
                    node.remove_children()
                    match = False
                    print(out)
                    print("Backtracking")
                    break

            if out == input:
                match = True
                print("match")
                return out, parse_tree


        if match == True:
            return out, parse_tree
        else:
            node.remove_children()
            # if node.children == [] and len(parse_tree) > 0:
            #     parse_tree.pop()
            # input_iter = 0

    print("parsing ends", out)
    return out, parse_tree


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
    print("\n-------------------------    PARSE TREE      -------------------------")
    for el in parse_tree:
        el.print_node()

    print("----------------------------------------------------------------------\n")
