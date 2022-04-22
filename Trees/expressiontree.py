import queues.queue


class ExpressionTree:
    def __init__(self, expstr) -> None:
        pass
        self._exptree = None
        self.buildTree(expstr)

    def evaluate(self, varmap):
        return self._evalTree(self._exptree, varmap)

    def __str__(self):
        return self.buildString(self._exptree)

    def buildString(self, treeNode):
        if treeNode.left is None and treeNode.rigth is None:
            return str(treeNode.element)
        expstr = "("
        expstr += self.buildString(treeNode.left)
        expstr += str(treeNode.element)
        expstr += self.buildString(treeNode.rigth)
        expstr += ")"
        return expstr

    def _evalTree(self, subtree, vardict):
        if subtree.left is None and subtree.rigth is None:
            if subtree.element >= "0" and subtree.element <= "9":
                return int(subtree.element)
            assert subtree.element in vardict, "invalid variable"
            return vardict[subtree.element]
        lval = self._evalTree(subtree.left, vardict)
        rval = self._evalTree(subtree.rigth, vardict)

        def comp(l, o, r):
            if o == "+":
                return(l+r)

        return comp(lval, subtree.element, rval)

    def buildTree(self, expstr):
        exp = queue.Queue()
        for token in expstr:
            exp.enqueue(token)

        self._exptree = _ExpTreeNode(None)
        self._recBuildTree(self._exptree, exp)

    def _recBuildTree(self, currnode, exp):
        token = exp.dequeue()

        if token == "(":
            currnode.left = _ExpTreeNode(None)
            self._recBuildTree(currnode.left, exp)

            currnode.element = exp.dequeue()
            currnode.rigth = _ExpTreeNode(None)
            self._recBuildTree(currnode.rigth, exp)

            exp.dequeue()

        else:
            currnode.element = token


class _ExpTreeNode:
    def __init__(self, data):
        self.element = data
        self.rigth = None
        self.left = None


equation = ExpressionTree("((2+7)+8)")
print(equation.evaluate({}))
