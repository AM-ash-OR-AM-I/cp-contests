from importlib import metadata
ds = metadata.distributions()
for d in ds:
    # print("===")
    # print(d)
    # print(f"{d.name=}")
    if d.name is None:
        print("FOUND")
        broken_dist = d
        print(f"found broken distribution at {d._path}")
        break