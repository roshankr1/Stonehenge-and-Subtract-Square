""" Tree class and functions
"""
from csc148_queue import Queue
from typing import List, Any, Union, Callable


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.

    === Attributes ===
    value - value  of root node
    children - root nodes of children
    """
    value: object
    children: List["Tree"]

    def __init__(self, value: object, children: List["Tree"]=None) -> None:
        """
        Create Tree self with content value and 0 or more children
        """
        self.value = value
        # copy children if not None
        # NEVER have a mutable default parameter...
        self.children = children[:] if children is not None else []

    def __repr__(self) -> str:
        """
        Return representation of Tree (self) as string that
        can be evaluated into an equivalent Tree.

        >>> t1 = Tree(5)
        >>> t1
        Tree(5)
        >>> t2 = Tree(7, [t1])
        >>> t2
        Tree(7, [Tree(5)])
        """
        # Our __repr__ is recursive, because it can also be called
        # via repr...!
        return "Tree({}, {})".format(self.value, self.children)

    def __eq__(self, other: Any) -> bool:
        """
        Return whether this Tree is equivalent to other.

        >>> t1 = Tree(5)
        >>> t2 = Tree(5, [])
        >>> t1 == t2
        True
        >>> t3 = Tree(5, [t1])
        >>> t2 == t3
        False
        """
        return (type(self) is type(other) and
                self.value == other.value and
                self.children == other.children)

    def __str__(self, indent: int=0) -> str:
        """
        Produce a user-friendly string representation of Tree self,
        indenting each level as a visual clue.

        >>> t = Tree(17)
        >>> print(t)
        17
        >>> t1 = Tree(19, [t, Tree(23)])
        >>> print(t1)
           23
        19
           17
        >>> t3 = Tree(29, [Tree(31), t1])
        >>> print(t3)
              23
           19
              17
        29
           31
        """
        root_str = indent * " " + str(self.value)
        mid = len(self.children) // 2
        left_str = [c.__str__(indent + 3)
                    for c in self.children][: mid]
        right_str = [c.__str__(indent + 3)
                     for c in self.children][mid:]
        return "\n".join(right_str + [root_str] + left_str)

    def count_nodes(self) -> int:
        """
        Return the number of nodes in self.

        >>> t = descendants_from_list(Tree(19), [1, 2, 3, 4, 5, 6, 7], 3)
        >>> t.count_nodes()
        8
        """
        return 1 + sum([c.count_nodes() for c in self.children])
        pass

    def is_leaf(self) -> bool:
        """Return whether Tree self is a leaf

        >>> Tree(5).is_leaf()
        True
        >>> Tree(5,[Tree(7)]).is_leaf()
        False
        """
        return len(self.children) == 0

    def __contains__(self, v: object) -> bool:
        """
        Return whether Tree self contains v.

        >>> t = Tree(17)
        >>> t.__contains__(17)
        True
        >>> t = descendants_from_list(Tree(19), [1, 2, 3, 4, 5, 6, 7], 3)
        >>> t.__contains__(5)
        True
        >>> t.__contains__(18)
        False
        """
        return self.value == v or any([v in tree
                                    for tree in self.children])
        pass

    def height(self) -> int:
        """
        Return length of longest path, + 1, in tree rooted at self.

        >>> t = Tree(5)
        >>> t.height()
        1
        >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
        >>> t.height()
        3
        """
        if self.children == []:
            return 1
        else:
            return 1 + max(child.height() for child in self.children)


    def flatten(self) -> list:
        """ Return a list of all values in tree rooted at self.

        >>> t = Tree(5)
        >>> t.flatten()
        [5]
        >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
        >>> L = t.flatten()
        >>> L.sort()
        >>> L == [0, 1, 3, 5, 7, 7, 9, 11, 13]
        True
        """
        if self.is_leaf():
            return [self.value]
        else:
            return ([self.value]
                    + sum([c.flatten()
                           for c in self.children], []))

def count_at_depth(t, d):
    """ Return the number of nodes at depth d of t.
    @param Tree t: tree to explore --- cannot be None
    @param int d: depth to report from, non-negative
    @rtype: int

    >>> t = Tree(17, [Tree(0), Tree(1, [Tree(4)]), Tree(2, [Tree(5)]), Tree(3)])
    >>> count_at_depth(t, 0)
    1
    >>> count_at_depth(t, 1)
    4
    >>> count_at_depth(t, 2)
    2
    >>> count_at_depth(t, 5)
    0
    """

    if d == 0:

        return 1
    else:
        #d -= 1
        return sum([count_at_depth(child, d - 1) for child in t.children])




# helpful helper function
def descendants_from_list(t: Tree, list_: list, arity: int) -> Tree:
    """
    Populate Tree t's descendants from list_, filling them
    in in level order, with up to arity children per node.
    Then return t.

    >>> descendants_from_list(Tree(0), [1, 2, 3, 4], 2)
    Tree(0, [Tree(1, [Tree(3, []), Tree(4, [])]), Tree(2, [])])
    """
    q = Queue()
    q.add(t)
    list_ = list_.copy()
    while not q.is_empty():  # unlikely to happen
        new_t = q.remove()
        for i in range(0, arity):
            if len(list_) == 0:
                return t  # our work here is done
            else:
                new_t_child = Tree(list_.pop(0))
                new_t.children.append(new_t_child)
                q.add(new_t_child)
    return t

def sum_nest(item: Union[int, list]):
    if isinstance(item, int):
        return [item]
    else:
        return sum(sum_nest(item1) for item1 in item)

class LinkedList:
    def __init__ (self, value, next = None):
        self.value = value
        self.next = next
    def __repr__ (self):
        return 'LinkedList({}, {})'.format(self.value, repr(self.next))

def reverse (item, tail = None):
    """
    >>> a = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4))))
    >>> a
    LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, None))))
    >>> b = reverse(a)
    >>> b
    LinkedList(4, LinkedList(3, LinkedList(2, LinkedList(1, None))))
    >>> a # note that there is a new head pointer now
    LinkedList(1, None)
    """
    next = item.next
    item.next = tail
    if next is None:
        return item
    else:
        return reverse(next, item)

def combination(letters: list, length: int) -> list:
    if length == 0:
        return []
    elif length == 1:
        return letters
    else:
        new_list = []
        for letter in combination(letters, length - 1):
            for letter1 in letters:
                new_list.append(letter + letter1)
        return new_list

def max_nested(list_: list):
    def max_helper(item: object):
        if isinstance(item, int):
            return item
        elif isinstance(item, list):
            return max([max_helper(n) for n in item])
    return max_helper(list_)

def nested_contains(L: list, value: int):
    def nested_helper(item: object, value: int):
        if not isinstance(item, list):
            return item == value
        elif isinstance(item, list):
            return any([nested_contains(item1, value) for item1 in item])
    return nested_helper(L, value)

def concat_strings(L: list):
    def concat_helper(item: object):
        if isinstance(item, str):
            return item
        elif isinstance(item, list):
            string = ''
            for item1 in item:
                string += concat_helper(item1)
    return concat_helper(L)

def list_leaves(t: Tree) -> list:
    """
    Return list of values in leaves of t.

    >>> t = Tree(0)
    >>> list_leaves(t)
    [0]
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> list_ = list_leaves(t)
    >>> list_.sort() # so list_ is predictable to compare
    >>> list_
    [3, 4, 5, 6, 7, 8]
    """
    if t.children == []:
        return [t.value]
    else:
        return sum([list_leaves(child) for child in t.children], [])


def list_all(t: Tree) -> list:
    """
    Return list of values in t.

    >>> t = Tree(0)
    >>> list_all(t)
    [0]
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> list_ = list_all(t)
    >>> list_.sort()
    >>> list_
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    """
    if t.children == []:
        return [t.value]
    else:
        return [t.value] + sum([list_all(child) for child in t.children], [])

def depth(t: Tree):
    if t is None:
        return 0
    elif t.children == []:
        return 1
    else:
        return 1 + max(depth(child) for child in t.children)

def list_interior(t):
    """
    Return list of values in interior nodes of t.

    @param Tree t: tree to list interior values of
    @rtype: list[object]

    >>> t = Tree(0)
    >>> list_interior(t)
    []
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> L = list_interior(t)
    >>> L.sort()
    >>> L
    [0, 1, 2]
    """
    if t.children == []:
        return []
    else:
        return [t.value] + sum([list_interior(child) for child in t.children], [])

# def list_if(t: Tree, p: Callable[int, bool]) -> list:
#     """
#     Return a list of values in Tree t that satisfy predicate p(value).
#
#     Assume p is defined on all of t's values.
#
#     >>> def p(v): return v > 4
#     >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
#     >>> list_ = list_if(t, p)
#     >>> list_.sort()
#     >>> list_
#     [5, 6, 7, 8]
#     >>> def p(v): return v % 2 == 0
#     >>> list_ = list_if(t, p)
#     >>> list_.sort()
#     >>> list_
#     [0, 2, 4, 6, 8]
#     """
#     if t.children == []:
#         return [t.value] if p(t.value) else []
#     else:
#         return ([t.value] if p(t.value) else []) + sum([list_if(child, p) for child in t.children], [])

def list_below(t: Tree, n: int) -> list:
    """
    Return list of values in t from nodes with paths no longer
    than n from root.

    >>> t = Tree(0)
    >>> list_below(t, 0)
    [0]
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> L = list_below(t, 1)
    >>> L.sort()
    >>> L
    [0, 1, 2, 3]
    """
    if n == 0:
        return [t.value]
    else:
        return [t.value] + sum([list_below(child, n - 1) for child in t.children], [])



def list_after(t: Tree, n: int) -> list:
    if n == 0:
        return list_all(t)
    elif n == 1:
        return sum([list_all(child) for child in t.children], [])
    else:
        return sum([list_after(child, n - 1) for child in t.children], [])

def path_length(t: Tree, node: Tree) -> int:
    if node == t:
        return 0
    else:
        return 1 + sum([path_length(child, node) for child in t.children])

def contains_test_passer(t: Tree, test: Callable[[Tree], bool]) -> bool:
    """
    Return whether t contains a value that test(value) returns True for.

    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4.5, 5, 6, 7.5, 8.5], 4)
    >>> def greater_than_nine(n): return n > 9
    >>> contains_test_passer(t, greater_than_nine)
    False
    >>> def even(n): return n % 2 == 0
    >>> contains_test_passer(t, even)
    True
    """

def max_length(obj: Union[list, object]) -> int:
    """
    Return the maximum length of obj or any of its sublists, if obj is a list.
    otherwise return 0.

    >>> max_length(17)
    0
    >>> max_length([1, 2, 3, 17])
    4
    >>> max_length([[1, 2, 3, 3], 4, [4, 5]])
    4
    """
    if not isinstance(obj, list):
        return 0
    else:
        return max([len(obj)] + [max_length(item) for item in obj])

def frac(k: int, n: int) -> list:
    result = []
    for index in range(n + 1):
        equation1 = k ** (index + 1)
        equation2 = equation1 - 1
        equation3 = k - 1
        result.append(equation1/(equation2 / equation3))
    return result

def pathlength_sets(t: Tree) -> None:
    if t.children == []:
        t.value = {0}
    else:
        for child in t.children:
            count = 0
            pathlength_sets(child)
# def count_path(t: Tree, carry: Union[set, None]) -> set:
#     if t.children == []:
#         return {0}
#     else:
#         for

def return_A_list_of_leaves(t: Tree) -> list:
    if t.children == []:
        return [t.value]
    else:
        for child in t.children:
            return sum([return_A_list_of_leaves(child)], [])

def divrem(a: int, b: int):
    count = 0
    den = b
    def divrem_helper(a: int, b: int):
        if b > a:
            raise Exception(" a cannot be greater than b")
        elif a == b:
            return b




class A:
    def g(self, n):
        return n

    def f(self, n):
        return self.g(n)

class B(A):
    def g(self, n):
        return 2*n

if __name__ == '__main__':
    t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    print(return_A_list_of_leaves(t))



