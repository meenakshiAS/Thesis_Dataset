def postorder(self, funct, stopOn=None):
    """
    Iterates in postorder, calling the function with the current node.
    If stopOn is set to True or False, it will stop on true or false.
    """
    if stopOn is None:
        for i in range(len(self.children) - 1, -1, -1):
            self.children[i].postorder(funct)
    else:
        for i in range(len(self.children) - 1, -1, -1):
            if self.children[i].postorder(funct) == stopOn:
                return stopOn

    return funct(self.symbol)
