def convert(string):
    return ' '.join(sorted(set(string.split())))


string = "the Quick brown fox jumps over the lazy brown dog"
print(convert(string))
