def zip_with(fn,a1,a2):
    return [fn(a,b) for a,b in zip(a1,a2)]
