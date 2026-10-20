def extract_months(time, months):
    """Extract times within specified months of the year.

    Parameters
    ----------
    time : xarray.DataArray
        Array of times that can be represented by numpy.datetime64 objects
        (i.e. the year is between 1678 and 2262).
    months : Desired months of the year to include

    Returns
    -------
    xarray.DataArray of the desired times
    """
    inds = _month_conditional(time, months)
    return time.sel(time=inds)
