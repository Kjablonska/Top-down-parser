from parse_tree import Node


def parser(CFG, input):
    print(CFG)
    rules = CFG['S']
    # input = input[:-1]

    if CFG != {}:
        out, parse_tree, match = rec_parse(CFG, "S", input, 0, "", Node("S"), [], 0)
        print("\n\nEnd of input parsing")
        print(out)
        print_parse_tree(parse_tree)


def rec_parse(CFG, nonterminal, input, input_iter, out, node, parse_tree, matched):
    rules = CFG[nonterminal]
    match = False

    print("-----------------------------------")
    print("CFG: " + nonterminal)
    print(rules, out)

    parse_tree.append(node)

    for rule in rules:
        print("rule", rule)
        match = False
        matched = 0
        for i in range(len(rule)):
            node.add_children(rule[i])
            print_parse_tree(parse_tree)

            print("curr rule " + rule)
            print("current input " + input[input_iter])
            if rule[i].isupper() == True:
                out, parse_tree, match = rec_parse(CFG, rule[i], input, input_iter, out, Node(rule[i]), parse_tree, matched)
                print("rec end", out, input[:-1], match)
                if out == input[:-1] and match == True:
                    match = True
                    print("out rec match")
                    return out, parse_tree, match
            else:
                if rule[i] == input[input_iter]:
                    out = out + rule[i]
                    input_iter += 1
                    matched += 1
                    match = True
                elif rule[i] == '$':
                    match = True
                    continue
                else:
                    # backtracking:
                    print("\t\tBacktracking")
                    print(input_iter)
                    print(input[input_iter])
                    print(input)

                    for el in range(matched):
                        out = out.replace(el, "")
                        input_iter = input_iter - 1

                    node.remove_children()
                    match = False
                    matched = 0
                    break

        if out == input[:-1] and match == True:
            match = True
            print("inner loop match")
            return out, parse_tree, match


        if out == input[:-1] and match == True:
            return out, parse_tree, match
        else:
            node.remove_children()

    print("parsing ends", out)
    return out, parse_tree, match


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
