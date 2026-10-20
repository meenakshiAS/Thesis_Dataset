def number_check(*args, func=None):
    """Check if arguments are numbers."""
    func = func or inspect.stack()[2][3]
    for var in args:
        if not isinstance(var, numbers.Number):
            name = type(var).__name__
            raise DigitError(f'Function {func} expected number, {name} got instead.')