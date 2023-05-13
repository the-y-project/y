class y:
    def __init__(self, arg1):
        self.is_factory = False
        self.function = lambda x: x
        self.args = [arg1]
        self.kwargs = {}

    def __truediv__(self, function):
        if self.is_factory:
            return type(self)(function)
        res = self.function(*self.args, **self.kwargs)
        if function is ...:
            return res
        self.args = [res]
        self.function = function
        self.kwargs = {}
        return self

    def __mod__(self, function):
        if self.is_factory:
            return NotImplemented
        self.function(*self.args, **self.kwargs)
        if function is ...:
            return self.args[0]
        self.args = [self.args[0]]
        self.function = function
        self.kwargs = {}
        return self

    def __mul__(self, arg):
        self.args.append(arg)
        return self

    def __matmul__(self, args):
        if isinstance(args, dict):
            self.kwargs.update(args)
        else:
            self.args.extend(args)
        return self


y = y(None)
y.is_factory = True
