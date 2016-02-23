def main():
    filename = sys.argv[1]
    try:
        for row in parse_csv(filename):
            print row
    except IOError:
        print >> sys.stderr, "The given file doesn't exist: ", filename
        sys.exit(1)
