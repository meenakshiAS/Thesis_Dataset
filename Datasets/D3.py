def _numpy_to_values(data):
    """Convert a NumPy array to values attribute."""

    def to_list_no_index(xvals, yvals):
        return [
            {"x": x, "y": np.asscalar(y)}
            for x, y in zip(xvals, yvals)
        ]

    if len(data.shape) == 1 or data.shape[1] == 1:
        xvals = range(data.shape[0] + 1)
        values = to_list_no_index(xvals, data)

    elif len(data.shape) == 2:
        if data.shape[1] == 2:
            # NumPy arrays and matrices have different iteration rules.
            if isinstance(data, np.matrix):
                xidx = (0, 0)
                yidx = (0, 1)
            else:
                xidx = 0
                yidx = 1

            xvals = [np.asscalar(row[xidx]) for row in data]
            yvals = [np.asscalar(row[yidx]) for row in data]

            values = [
                {"x": x, "y": y}
                for x, y in zip(xvals, yvals)
            ]

        else:
            raise ValueError("arrays with > 2 columns not supported")

    else:
        raise ValueError("invalid dimensions for ndarray")

    return values
