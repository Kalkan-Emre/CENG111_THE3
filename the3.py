def is_empty(t):
    return t == []

def datum(t):
    return t[0]

def children(t):
    return t[1:]

def is_leaf(t):
    return len(children(t)) == 0





### HELPER FUNCTIONS ###

def find_root(lst):  # Verilen listenin root node'unu bulur
    datums = []
    children = []
    for ele in lst:
        datums.append(ele)
        if type(ele[1])== tuple:
            for sub_ele in ele[1:]:
                children.append(sub_ele[1])
    for datum in datums:
        if datum[0] not in children:
            return datum

def make_tree_recursive(node,lst):  # Verilen listeyle tree oluşturur
    if is_empty(lst):
        pass
    else:
        if type(node[1])== tuple:
            siblings = [x[1] for x in node[1:]]
            tree = [tuple(node)]
            for i in range(len(siblings)):
                index_of_child = [x[0]for x in lst].index(siblings[i])
                tree += [make_tree_recursive(lst[index_of_child],lst)]
            return tree
        else:
            return [tuple(node)]
        
def build_tree(part_list):  # make_tree_recursive'i kullanır
    root = find_root(part_list)
    return make_tree_recursive(root,part_list)

def calculate_price_recursive(tree,leaves):  
    if is_empty(tree):
        return 0
    else:
        if list(tree[0]) not in leaves:
            cost_of_subtrees = 0
            for i in range(1,len(tree)):
                cost_of_subtrees  += calculate_price_recursive(tree[i],leaves)*tree[0][i][0]
            return cost_of_subtrees
        else:
            return tree[0][1]

def required_parts_recursive(tree,leaves):   
    if is_empty(tree):
        pass
    else:
        if list(tree[0]) not in leaves:
            parts = []
            for i in range(1,len(tree)):
                subtree = required_parts_recursive(tree[i],leaves)
                parts = parts + [((x[0]*tree[0][i][0]),x[1]) for x in subtree if type(x)==tuple]
            return parts
        else:
            return [(1,tree[0][0])]








def calculate_price(part_list):
    tree = build_tree(part_list)
    leaves = [x if type(x[1])!=tuple else [] for x in part_list ]   # Listeden tree'nin leaf node'larını bulur
    return calculate_price_recursive(tree,leaves)

def required_parts(part_list): 
    leaves = [x if type(x[1])!=tuple else [] for x in part_list ]   # Listeden tree'nin leaf node'larını bulur
    tree = build_tree(part_list)
    return required_parts_recursive(tree,leaves)

def stock_check(part_list,stock_list):
    required = required_parts(part_list)
    shortage = []
    stock_material = [x[1] for x in stock_list]
    for ele in required:
        if ele[1] in stock_material:
            index_of_stock = stock_material.index(ele[1])
            stock_amount = stock_list[index_of_stock][0]
            shortness_amount = ele[0]-stock_amount
            if shortness_amount > 0:
                shortage.append((ele[1],shortness_amount))
        else:
            shortage.append((ele[1],ele[0]))
    return shortage


