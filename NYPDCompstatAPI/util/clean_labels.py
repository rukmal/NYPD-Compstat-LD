def cleanLabel(dirty_label: str) -> str:
    """Function to clean labels. Replaces all special characters
    with underscores.
    
    Arguments:
        dirty_label {str} -- Dirty label to be cleaned.
    
    Returns:
        str -- Cleaned label.
    """

    # Replace all specials with underscore
    kinda_dirty = ''.join([i if i.isalnum() else '_' for i in dirty_label])

    return kinda_dirty.replace('__', '_')
