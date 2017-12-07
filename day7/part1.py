import re

def get_root_node(nodes):
    all_nodes = set()
    children = set()
    
    for n in nodes:
        all_nodes.add(n[0])
        for c in n[2:]:
            children.add(c)
    return next(iter(all_nodes - children))

def main():
    nodes = sorted([re.findall('[a-z]+|\d+', line.rstrip()) for line in open('input.txt', 'r').readlines()], key=lambda x: len(x))
    root = get_root_node(nodes)
    print(root)

if __name__ == '__main__':
    main()