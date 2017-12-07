import re
from collections import Counter

def get_total_weight(node_name, nodes):
    node_object = nodes[node_name]
    total_weight = node_object['weight']
    child_weights = []
    
    for c in node_object['children']:
        child_weight = get_total_weight(c, nodes)
        child_weights.append(child_weight)
        total_weight += child_weight

    return total_weight

def main():
    nodes = {}
    for line in open('input.txt', 'r').readlines():
        line = line.rstrip().split(' ', 1)
        name = line[0]
        weight = int(re.search('\d+', line[1]).group())
        children = re.findall('[a-z]+', line[1])
        nodes[name] = {
            'weight': weight,
            'children': children
        }

    for node in nodes:
        node_object = nodes[node]
        total_weight = get_total_weight(node, nodes)
        child_weights = [get_total_weight(n, nodes) for n in node_object['children']]
        
        counted = Counter(child_weights)
        if (len(counted) > 1):
            odd_one_out_weight = min(counted, key=counted.get)
            odd_one_out_index = child_weights.index(odd_one_out_weight)
            odd_one_out_name = node_object['children'][odd_one_out_index]
            difference = odd_one_out_weight - max(counted, key=counted.get)
            print(nodes[odd_one_out_name]['weight'] - difference)

if __name__ == '__main__':
    main()
