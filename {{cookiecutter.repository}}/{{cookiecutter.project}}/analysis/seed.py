#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid


def get_uuid(flavor: str = None):
    """Generate a Universally Unique Identifier

    Args:
        flavor (str): Format of the uuid

    Raises:
        ValueError: Raised when flavor is not defined

    Returns:
        [str, bytes]: uuid
    """
    if flavor == "str":
        seed = str(uuid.uuid1())
    elif flavor == "hex":
        seed = uuid.uuid1().hex
    elif flavor == "bytes":
        seed = uuid.uuid1().bytes
    else:
        raise ValueError("undefined flavor")
    return seed
