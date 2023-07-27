def concat_words(*args, separator="."):
    return separator.join(args)


concat_words("a", "b", "c", "d", separator=".")
