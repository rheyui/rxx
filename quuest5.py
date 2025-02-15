def sorts(d):
    sorted_dict=dict(sorted(d.items(),key=lambda item:item[1]))
    return sorted_dict
h={101:"John Doe", 102:"Jane Smith", 103:"Peter Johnson"}
sorting=sorts(h)
print(sorting)