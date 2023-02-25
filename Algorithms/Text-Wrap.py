import textwrap

def wrap(string, max_width):
    
    x = textwrap.wrap(string, width=4)
    result = ''
    
    for i in x:
        result += i + '\n'
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
