# Python-drill-46.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 3.5.  Basic range drill.

def main():

    # Prints 0 1 2 3 on different lines.
    v = range(0, 4)
    v_len = len(v)
    for i in range(0, v_len):
        print(v[i])
    print "\n"

    # Prints 3 2 1 0 on different lines.
    w = range(3, -1, -1)
    w_len = len(w)
    for i in range(0, w_len):
        print (w[i])
    print "\n"

    # Prints 8 6 4 2 on different lines.
    y = range(8, 1, -2)
    y_len = len(y)
    for i in range(0, v_len):
        print (y[i])

if __name__ == "__main__": main()
