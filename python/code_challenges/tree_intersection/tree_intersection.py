# Keep code short and sweet by utilizing previously built Binary Tree & Node implementation
# Imports found in test

def tree_intersection(tree1, tree2):
    # Format trees into Set() data type
    tree1_set = set(tree1.pre_order())
    tree2_set = set(tree2.pre_order())
    # Use intersection built-in method to compare/return items that only exist in both sets
    intersect = tree1_set.intersection(tree2_set)
    # Format our data into list data type
    intersect_list = list(intersect)
    # Return values found in both trees
    return intersect_list
