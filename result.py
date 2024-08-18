from collections import defaultdict

def Adsense_Result(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines if line.strip()]

    data = {
        "Binge DE": defaultdict(lambda: {"visible": 0, "not visible": 0}),
        "Binge Us": defaultdict(lambda: {"visible": 0, "not visible": 0}),
        "Google DE": defaultdict(lambda: {"visible": 0, "not visible": 0}),
        "Google Us": defaultdict(lambda: {"visible": 0, "not visible": 0})
    }

    current_group = None
    position = 0

    for line in lines:
        if line in data:
            current_group = line
            position = 0
        elif current_group:
            position += 1
            if 'Adsense is visible' in line:
                data[current_group][position]["visible"] += 1
            elif 'Adsense is not visible' in line:
                data[current_group][position]["not visible"] += 1

    result_lines = []
    for group, positions in data.items():
        result_lines.append(f"{group}:")
        for position in range(1, 21):
            visible_count = positions[position]["visible"]
            not_visible_count = positions[position]["not visible"]
            result_lines.append(
                f"Position {position}: Adsense is visible {visible_count} times, Adsense is not visible {not_visible_count} times"
            )
        result_lines.append("")  
        
    
    with open(output_file, 'w') as output_file:
        output_file.write('\n'.join(result_lines))

input_file = '/Users/User/OneDrive/Desktop/Adsense 2.txt'
output_file = '/Users/User/OneDrive/Desktop/AdSense/url.txt'

Adsense_Result(input_file, output_file)

print(f"Results have been saved to {output_file}")