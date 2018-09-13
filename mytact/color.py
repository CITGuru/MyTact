def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

print_format_table()


x = 0
for i in range(24):
    colors = ""
    for j in range(5):
        code = str(x+j)
        colors = colors + "\33[" + code + "m\\33[" + code + "m\033[0m "
    print(colors)
    x=x+5
