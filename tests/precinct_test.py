from context import NYPDCompstatAPI

ls = NYPDCompstatAPI.metadata.getPrecincts('prev_ytd','grand_larceny')

print("\n\n\nTest:\n")
for i in ls:
    print(i)