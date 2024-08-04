# username1 - avivschiby
# id1      - 206655540
# name1    - aviv schiby
# id2      - 213104177
# name2    - maya schiby


"""A class representing a node in an AVL tree"""
import random


#######################
# Binary Search Tree  # (code from lecture)
#######################

def printree(t, bykey=True):
    """Print a textual representation of t
    bykey=True: show keys instead of values"""
    # for row in trepr(t, bykey):
    #        print(row)
    return trepr(t, bykey)


def trepr(t, bykey=False):
    """Return a list of textual representations of the levels in t
    bykey=True: show keys instead of values"""
    if t == None:
        return ["#"]

    thistr = "k: " + str(t.key) + " v: " + str(t.value)

    return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))


def comp(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return True
    if len(s1) == 0 or len(s2) == 0:
        return False
    if (len(s1) == 1 and s1[0] == '*') or (
            len(s1) > 1 and s1[0] == '*' and s1[1] != s2[0] and len(s2) > 1 and len(s2) > len(s1)):
        return comp(s1, s2[1:])
    return comp(s1[1:], s2[1:])


def conc(left, root, right):
    """Return a concatenation of textual represantations of
    a root node, its left node, and its right node
    root is a string, and left and right are lists of strings"""

    lwid = len(left[-1])
    rwid = len(right[-1])
    rootwid = len(root)

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    ls = leftspace(left[0])
    rs = rightspace(right[0])
    result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += rwid * " "

        result.append(row)

    return result


def leftspace(row):
    """helper for conc"""
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1


def rightspace(row):
    """helper for conc"""
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i


class Tree_node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "(" + str(self.key) + ":" + str(self.val) + ")"


class AVLNode(object):
    """Constructor,

    @type key: int or None
    @param key: key of your node
    @type value: any
    @param value: data of your node
    @type left: AVLNode or none
    @param left: the left son of your node
    @type right: AVLNode or none
    @param right: the right son of your node
    @type parent: AVLNode or none
    @param parent: the parent of your node
    @type height: int
    @param height: the height of the subtree from that node
    @type size: int
    @param size: the size of the subtree from that node
    @type BF: int
    @param BF: the balance factor of the node
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        if key == None:
            self.height = -1
            self.size = 0
        else:
            self.height = 0
            self.size = 1
        self.BF = 0


    """sets balance factor in O(1)

    @type BF: int 
    @param BF: balance factor 
    """

    def is_real_node(self):
        return self.key != None

    def set_BF(self, BF):
        self.BF = BF

    """returns the balance factor in O(1)

    @rtype: int 
    @returns: the balance factor of self
    """

    def get_balance_factor(self):
        if not self.is_real_node():
            return 0
        return self.get_left().get_height() - self.get_right().get_height()
    """returns the height of self in O(1)

    @rtype: int 
    @returns: the height of self
    """

    def get_height(self):
        if not self.is_real_node():
            return -1
        return 1 + max(self.get_right().height, self.get_left().height)

    """returns the key

    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """

    def get_key(self):
        return self.key

    """returns the value

    @rtype: any
    @returns: the value of self, None if the node is virtual
    """

    def get_value(self):
        return self.value

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child (if self is virtual)
    """

    def get_left(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """

    def get_right(self):
        return self.right
    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def get_parent(self):
        return self.parent

    """returns the size of the subtree

    @rtype: int
    @returns: the size of the subtree of self, 0 if the node is virtual
    """

    def get_size(self):
        if not self.is_real_node():
            return 0
        return self.get_right().size + self.get_left().size + 1
    """sets key

    @type key: int or None
    @param key: key
    """

    def set_key(self, key):
        self.key = key

    """sets value

    @type value: any
    @param value: data
    """

    def set_value(self, value):
        self.value = value

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def set_left(self, node):
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def set_right(self, node):
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def set_parent(self, node):
        self.parent = node

    """sets the height of the node

    @type h: int
    @param h: the height
    """

    def set_height(self, h):
        self.height = h

    """sets the size of node

    @type s: int
    @param s: the size
    """

    def set_size(self, s):
        self.size = s


"""
A class implementing an AVL tree.
"""


class AVLTree(object):

    """
    Constructor

    @type root: AVLNode or None
    @param root: the root of self
    """

    def __init__(self):
        self.root = AVLNode(None, None)

    def __repr__(self):  # no need to understand the implementation of this one
        out = ""
        for row in printree(self.root):  # need printree.py file
            out = out + row + "\n"
        return out
    """searches for a node in the dictionary corresponding to the key in O(log(n)) because AVL tree is a BS tree.

    @type key: int
    @param key: a key to be searched
    @rtype: AVLNode
    @returns: node corresponding to key.
    """


    def search(self, key):  # O(log(n))
        node = self.root
        while node.is_real_node():
            if node.key < key:
                node = node.right
            elif node.key > key:
                node = node.left
            else:
                return node
        return None

    """finds the successor of A  in O(log(n)) 

        @type A: AVLNode 
        @param A: The node that we want to find his successor
        @rtype: AVLNode
        @returns: The successor on A
    """

    def find_successor(self, A):  # O(log(n))
        successor = None
        below_A = None
        above_A = None
        if A.get_right().is_real_node():
            below_A = A.right
            while below_A.get_left().is_real_node():  # the height of an avl tree is O(log(n)) so that loop is max O(log(n))
                below_A = below_A.get_left()
            successor = below_A
        elif A.get_parent() != None:
            above_A = A.parent
            while above_A.get_parent() != None and above_A.get_key() < A.get_key():  # the height of an avl tree is O(log(n))
                # so that loop is max O(log(n))
                above_A = above_A.parent
            if above_A.key > A.key:
                return above_A
            else:
                successor = None
        else:
            successor = None
        return successor

    """inserts val at position i in the dictionary in O(log(n)) 

        @type key: int
        @pre: key currently does not appear in the dictionary
        @param key: key of item that is to be inserted to self
        @type val: any
        @param val: the value of the item
        @rtype: int
        @returns: the number of rebalancing operation due to AVL rebalancing
    """



    def insert(self, key, val):
        if not self.root.is_real_node():
            self.root = AVLNode(key, val)
            virtual_node1 = AVLNode(None, None)
            virtual_node2 = AVLNode(None, None)
            self.root.set_right(virtual_node1)
            self.root.set_left(virtual_node2)
            virtual_node1.set_parent(self.root)
            virtual_node2.set_parent(self.root)
            return 0
        new_node, parent = self.insertWR(key, val)  # O(log(n))
        height_change_counter = 0
        while parent != None:
            parent.BF = parent.get_balance_factor()
            if abs(parent.BF) < 2 and parent.height == parent.get_height():
                parent.set_height(parent.get_height())
                return height_change_counter
            elif abs(parent.BF) < 2 and parent.height != parent.get_height():
                parent.set_height(parent.get_height())
                height_change_counter += 1
                parent = parent.get_parent()
                continue
            else:
                height_change_counter = self.rotate(parent, height_change_counter)
                break
        return height_change_counter


    """checks what type of rotation is needed and proform it with a helper function
        @returns: height changes that was given to it plus 1 or 2, depends of the type of the rotatin
    """


    def rotate(self, A, height_change_counter):
        if A.BF == 2:
            if A.get_left().get_balance_factor() >= 0:
                self.RR(A)
                A.set_height(A.get_height())
                A.set_size(A.get_size())
                A.get_parent().set_size(A.get_parent().get_size())
                return 1 + height_change_counter
            else:
                self.LR(A, A.get_left())
                A.get_parent().set_size(A.parent.get_size())
                A.set_height(A.get_height())
                return 2 + height_change_counter
        if A.get_balance_factor() == -2:
            if A.get_right().get_balance_factor() <= 0:
                self.LL(A)
                A.set_height(A.get_height())
                A.set_size(A.get_size())
                A.get_parent().set_size(A.parent.get_size())
                return 1 + height_change_counter
            else:
                self.RL(A, A.get_right())
                A.set_height(A.get_height())
                A.get_parent().set_size(A.parent.get_size())
                return 2 + height_change_counter
        return height_change_counter

    """inserts val at position i in the dictionary in O(log(n)) without roataions

        @type key: int
        @pre: key currently does not appear in the dictionary
        @param key: key of item that is to be inserted to self
        @type val: any
        @param val: the value of the item
        @rtype: tuple
        @returns: the new tree which is yet to be AVL tree, the new node and his parent
    """

    def insertWR(self, key, val):
        node = self.root
        parent = None
        while node.is_real_node():  # search in BST is worst case O(log(n))
            parent = node
            node.size += 1
            if node.get_key() < key:
                node = node.get_right()
            else:
                node = node.get_left()
        new_node = AVLNode(key, val)
        new_node.set_parent(parent)
        if parent.get_key() < key:
            parent.set_right(new_node)
        else:
            parent.set_left(new_node)
        virtual_node1 = AVLNode(None, None)
        virtual_node2 = AVLNode(None, None)
        new_node.set_right(virtual_node1)
        new_node.set_left(virtual_node2)
        virtual_node1.set_parent(new_node)
        virtual_node2.set_parent(new_node)
        return new_node, parent

    """Rotate left in O(1) 

        @type A: AVLNode
        @param A: the node that is BF his not right
    """

    def LL(self, A):
        A_parent = A.get_parent()
        A_right = A.get_right()
        if self.root is A:
            A.set_parent(A_right)
            A.set_right(A_right.get_left())
            A_right.get_left().set_parent(A)
            self.root = A_right
            A_right.set_parent(None)
            A_right.set_left(A)
        else:
            if A_parent.get_left() is A:
                A_parent.set_left(A_right)
            else:
                A_parent.set_right(A_right)
            A.set_parent(A_right)
            A.set_right(A_right.get_left())
            A_right.get_left().set_parent(A)
            A_right.set_parent(A_parent)
            A_right.set_left(A)
        A.set_height(A.get_height())
        A.get_parent().set_height(A.get_parent().get_height())
        A.BF = A.get_balance_factor()
        A.get_parent().BF = A.parent.get_balance_factor()

    """Rotate right in O(1) 

        @type A: AVLNode
        @param A: the node that is BF his not right
    """

    def RR(self, A):
        A_parent = A.get_parent()
        A_left = A.get_left()
        if self.root is A:
            A.set_parent(A_left)
            A.set_left(A_left.get_right())
            A_left.get_right().set_parent(A)
            self.root = A_left
            A_left.set_parent(None)
            A_left.set_right(A)
        else:
            if A_parent.right is A:
                A_parent.set_right(A_left)
            else:
                A_parent.set_left(A_left)
            A.set_parent(A_left)
            A.set_left(A_left.get_right())
            A_left.get_right().set_parent(A)
            A_left.set_parent(A_parent)
            A_left.set_right(A)
        A.height = A.get_height()
        A.get_parent().height = A.parent.get_height()
        A.BF = A.get_balance_factor()
        A.parent.BF = A.parent.get_balance_factor()

    """Rotate left - right in O(1) 

        @type A: AVLNode
        @param A: the node that his BF is not right
        @type B: AVLNode
        @param B: A's left son 
    """

    def LR(self, A, B):
        self.LL(B)
        B.size = B.get_size()
        self.RR(A)
        A.size = A.get_size()

    """Rotate left - right in O(1) 

        @type A: AVLNode
        @param A: the node that his BF is not right
        @type B: AVLNode
        @param B: A's right son 
    """

    def RL(self, A, B):
        self.RR(B)
        B.size = B.get_size()
        self.LL(A)
        A.size = A.get_size()

    """deletes node from the dictionary in O(log(n))

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, node):  # O(log(n))
        parent = node.parent
        if not has_only_one_child(node) and not is_leaf(node):  # so node has two children and the
            # physically deleted node is the successor
            y = self.find_successor(node)
            parent = y.parent
        self.delete_as_BST(node)
        cost = 0
        while parent != None:
            parent.BF = parent.get_balance_factor()
            prev_height = parent.height
            parent.height = parent.get_height()
            if abs(parent.BF) < 2 and prev_height == parent.height:
                self.tree_updates(parent)  # <<-- this method runs at O(log(n)) and it is in a while loop. but as
                parent.height = parent.get_height()  # you can see it beaks the while loop right after so it doesn't
                break  # add up to O(log^2(n)) but instead stays at O(log(n))
            elif abs(parent.BF) < 2 and prev_height != parent.height:
                parent.size = parent.get_size()
                parent.height = parent.get_height()
                cost += 1
                parent = parent.get_parent()
                continue
            else:
                if parent.BF == 2:
                    if parent.left.BF >= 0:
                        self.RR(parent)
                        parent.size = parent.get_size()
                        parent.height = parent.get_height()
                        cost += 2
                        parent = parent.parent
                        continue
                    else:
                        self.LR(parent, parent.left)
                        parent.size = parent.get_size()
                        parent.height = parent.get_height()
                        cost += 3
                        parent = parent.parent
                        continue
                if parent.BF == -2:
                    if parent.right.BF <= 0:
                        self.LL(parent)
                        parent.size = parent.get_size()
                        parent.height = parent.get_height()
                        cost += 2
                        parent = parent.parent
                        continue
                    else:
                        self.RL(parent, parent.right)
                        parent.size = parent.get_size()
                        parent.height = parent.get_height()
                        cost += 3
                        parent = parent.parent
                        continue
            parent = parent.parent
        return cost


    """ deletes like a regular BST in O(log(n))

        @type node: AVLNode
        @pre: node is a real pointer to a node in self
    """

    def delete_as_BST(self, node):  # O(log(n))
        if self.is_root(node):
            if not node.get_right().is_real_node() and not node.get_left().is_real_node():
                self.root = AVLNode(None, None)
                return
            elif not node.get_right().is_real_node() and node.get_left().is_real_node():
                self.root = node.get_left()
                node.get_left().set_parent(None)
                return
            elif node.get_right().is_real_node() and not node.get_left().is_real_node():
                self.root = node.right
                node.get_right().set_parent(None)
                return
        if is_leaf(node):
            self.delete_leaf(node)
            return
        else:
            if has_only_one_child(node):
                self.delete_node_with_only_one_child(node)
                return
            else:  # node has two children
                y = self.find_successor(node)
                if has_only_one_child(y):
                    self.delete_node_with_only_one_child(y)
                else:
                    self.delete_leaf(y)
                node.set_key(y.get_key())
                node.set_value(y.get_value())

    """deletes a leaf from the dictionary in O(1)

        @type node: AVLNode
        @pre: node is a real pointer to a leaf in self
        @param node: the leaf we want to delete from the tree
        @rtype: int
        @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete_leaf(self, node):
        parent = node.get_parent()
        node_to_replace = AVLNode(None, None)
        if parent.get_right() is node:
            parent.set_right(node_to_replace)
            node_to_replace.set_parent(parent)
        else:
            parent.set_left(node_to_replace)
            node_to_replace.set_parent(parent)
    """deletes a node with only one child from the dictionary in O(1)

            @type node: AVLNode
            @pre: node is a real pointer to a node in self and has only one child
            @param node: the node we want to delete from the tree
            @rtype: int
            @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete_node_with_only_one_child(self, node):
        parent = node.parent
        if not node.get_right().is_real_node():
            if parent.get_left() is node:
                node.get_parent().set_left(node.get_left())
                node.get_left().set_parent(node.get_parent())
            else:  ## node.parent.right == node
                node.get_parent().set_right(node.get_left())
                node.get_left().set_parent(node.get_parent())
        else:
            if node.get_parent().get_left() is node:
                node.get_parent().set_left(node.get_right())
                node.get_right().set_parent(node.get_parent())
            else:  ## node.parent.right == node
                node.get_parent().set_right(node.get_right())
                node.get_right().set_parent(node.get_parent())

    """check if this node is the root of self

        @rtype: boolean
        @returns: if node is the root of self
    """

    def is_root(self, node):
        return self.root is node

    """returns an array representing dictionary in O(n)

    @rtype: list
    @returns: a sorted list according to key of tuples (key, value) representing the data structure
    """

    def avl_to_array(self):
        arr = [0 for x in range(self.size())]
        curr = self.root
        while curr.is_real_node() and curr.get_left().is_real_node():
            curr = curr.get_left()  # so the curr will be the min node, so that takes O(log(n))
        i = 0

        while i < self.root.size:  # while i < n -> that will be O(n)
            arr[i] = (curr.get_key(), curr.get_value())
            curr = self.find_successor(curr)
            i += 1

        return arr

    """returns the number of items in dictionary in O(1)

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        return self.get_root().get_size()

    """splits the dictionary at a given node in O(log(n))

    @type node: AVLNode
    @pre: node is in self
    @param node: The intended node in the dictionary according to whom we split
    @rtype: list
    @returns: a list [left, right], where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    """

    def split(self, node):
        node = self.search(node.key)
        parent_last = node
        if node.get_left().is_real_node():
            left_tree = sub_tree(node.get_left())
        else:
            left_tree = AVLTree()

        if node.get_right().is_real_node():
            right_tree = sub_tree(node.get_right())
        else:
            right_tree = AVLTree()
        parent = node.get_parent()
        while parent != None:  # we go up from maximum a leaf to the root so that maximum O(log(n)) and as we saw in the
            # lecture the rest of the code will be summed into a total of O(log(n)) because we are joining subtrees
            if parent.get_left() == parent_last:
                if parent.get_right().is_real_node():
                    right_tree.join(sub_tree(parent.get_right()), parent.key, parent.value)
                else:
                    right_tree.insert(parent.key, parent.value)
            else:
                if parent.get_left().is_real_node():
                    left_tree.join(sub_tree(parent.get_left()), parent.key, parent.value)
                else:
                    left_tree.insert(parent.key, parent.value)
            parent_last = parent
            parent = parent.get_parent()
        node = AVLNode(None, None)  # so now the node won't be available
        return [left_tree, right_tree]

    """joins self with key and another AVLTree in O(log(n))

    @type tree: AVLTree 
    @param tree: a dictionary to be joined with self
    @type key: int 
    @param key: The key separating self with tree
    @type val: any 
    @param val: The value attached to key
    @pre: all keys in self are smaller than key and all keys in tree are larger than key,
    or the other way around.
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def join(self, tree, key, val):  ## O(log(n))
        if tree.root.is_real_node() and self.root.is_real_node():
            cost = abs(self.root.height - tree.root.height) + 1
        else:
            if tree.root.is_real_node() and not self.root.is_real_node():
                cost = tree.root.height + 1
            elif not tree.root.is_real_node() and self.root.is_real_node():
                cost = self.root.height + 1
            else:
                cost = 1
        X = AVLNode(key, val)
        if not self.root.is_real_node():
            tree.insert(key, val)
            self.root = tree.root
            return cost
        if not tree.root.is_real_node():
            self.insert(key, val)
            return cost
        if tree.root.key < self.root.key:  # the keys of tree is smaller than the keys of self
            # (we can think like tree is in the left of self)
            if tree.root.height < self.root.height - 1:
                b = self.root
                while b.height != tree.root.height and b.height != tree.root.height - 1:
                    b = b.left
                c = b.parent
                a = tree.root
                connect_to_X(b, a, c, X, "l")
                tree.root = AVLNode(None, None)
                self.tree_updates(c)

            elif tree.root.height > self.root.height + 1:  # tree is higher than self
                b = tree.root
                while b.height != self.root.height and b.height != self.root.height + 1:
                    b = b.right
                c = b.parent
                a = self.root
                connect_to_X(a, b, c, X, "r")
                self.root = tree.root
                tree.root = AVLNode(None, None)
                self.tree_updates(c)

            else:  # heights of the trees are equal
                a = self.root
                b = tree.root
                c = None
                connect_to_X(a, b, c, X, 'l')
                self.root = X
                self.tree_updates(X)

        else:  # keys of self smaller than keys of tree
            if tree.root.height > self.root.height + 1:  # tree is higher than tree
                b = tree.root
                while b.height != self.root.height and b.height != self.root.height + 1:
                    b = b.left
                a = self.root
                c = b.parent
                connect_to_X(b, a, c, X, "l")
                self.root = tree.root
                tree.root = AVLNode(None, None)
                self.tree_updates(c)

            elif tree.root.height < self.root.height - 1:
                b = self.root
                while b.height != tree.root.height and b.height != tree.root.height - 1:
                    b = b.right
                c = b.parent
                a = tree.root
                connect_to_X(a, b, c, X, "r")
                self.tree_updates(c)
                tree.root = AVLNode(None, None)

            else:
                b = self.root
                a = tree.root
                c = None
                connect_to_X(a, b, c, X, 'l')
                self.root = X
                if abs(X.BF) >= 2:
                    self.tree_updates(X)
        return cost

    """rotate as needed, update the size and update the Height of self in O(log(n))

        @type A: AVLNode 
        @pre: A is in the tree
    """

    def tree_updates(self, A):
        while A != None:
            A.set_height(A.get_height())
            A.set_size(A.get_size())
            A.BF = A.get_balance_factor()
            if abs(A.BF)>= 2:
                self.rotate(A, 0)
            A = A.get_parent()


    """compute the rank of node in the self in O(log(n))

    @type node: AVLNode
    @pre: node is in self
    @param node: a node in the dictionary which we want to compute its rank
    @rtype: int
    @returns: the rank of node in self
    """

    def rank(self, node):
        if not self.root.is_real_node():
            return None
        rank = node.get_left().get_size() + 1
        p = node
        while p != self.root:  # worst case if p is leaf the loop will be O(self.height) == O(log(n))
            if p.parent.get_right() == p:
                rank = rank + p.parent.get_left().get_size() + 1
            p = p.get_parent()
        return rank

    """finds the i'th smallest item (according to keys) in self in O(log(n)) using recursion

    @type i: int
    @pre: 1 <= i <= self.size()
    @param i: the rank to be selected in self
    @rtype: int
    @returns: the item of rank i in self
    """

    def select(self, i):
        return self.select_rec(self.root, i)

    def select_rec(self, node, i):  # O(log(n))
        if not node.get_left().is_real_node():
            left_size = 1
        else:
            left_size = node.get_left().get_size() + 1
        if i < left_size:
            return self.select_rec(node.get_left(), i)
        elif i > left_size:
            return self.select_rec(node.get_right(), i - left_size)
        else:
            return node

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return self.root


"""
    returns if node is leaf in O(1)

    @type node: AVLNode
    @rtype: boolean
    @returns: if node is left
"""


def is_leaf(node):
    return not node.get_left().is_real_node() and not node.get_right().is_real_node()


"""
    returns if node has only one child in O(1)

    @type node: AVLNode
    @rtype: boolean
    @returns: if node has only one child
"""


def has_only_one_child(node):
    # return (node.right == None and node.left != None) or (node.right != None and node.left == None)
    return (not node.get_right().is_real_node() and node.get_left().is_real_node()) or \
        (node.get_right().is_real_node() and not node.get_left().is_real_node())

"""
    creates and return a subtree that his root is node

    @type node: AVLNode
    @rtype: AVLTree
    @returns: the subtree 
"""


def sub_tree(node):
    T = AVLTree()
    T.root = node
    T.root.parent = None
    return T


"""
    takes 4 nodes and connects them properly as needed in O(1)

    @type a: AVLNode
    @type b: AVLNode
    @type c: AVLNode
    @type X: AVLNode
    @type side: String

"""


def connect_to_X(a, b, c, X, side):
    X.set_right(a)
    X.set_left(b)
    X.set_parent(c)
    a.set_parent(X)
    b.set_parent(X)
    X.set_height(X.get_height())
    X.set_size(X.get_size())
    if c:
        c.set_left(X) if side == "l" else c.set_right(X)
    if c:
        c.set_height(c.get_height())
        c.set_size(c.get_size())
        c.BF = c.get_balance_factor()


t = AVLTree()
n = 10
for i in range(1, 11):
    t.insert(i, n-i)
print(t)
