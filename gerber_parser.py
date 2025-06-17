import importlib


def parse_gerber(file_path: str):
    """Parse a Gerber file using the pygerber library.

    Parameters
    ----------
    file_path : str
        Path to the Gerber file.

    Returns
    -------
    Any
        Parsed Gerber object as returned by :mod:`pygerber`.
    """
    pygerber = importlib.import_module("pygerber")

    # pygerber exposes multiple helpers for loading Gerber files.
    # Prefer ``load_layer_from_file`` when available.  The exact
    # API may vary between releases, so fall back to more generic
    # helpers when necessary.
    if hasattr(pygerber, "load_layer_from_file"):
        return pygerber.load_layer_from_file(file_path)
    if hasattr(pygerber, "load_layer"):
        return pygerber.load_layer(file_path)
    if hasattr(pygerber, "parse_file"):
        return pygerber.parse_file(file_path)

    raise NotImplementedError(
        "Cannot locate Gerber parsing function in pygerber."
    )
