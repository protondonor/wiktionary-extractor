# import datetime
import io

from get_middle_chinese import get_middle_chinese_for_character
import argparse

# timestamp = str(datetime.datetime.now()).replace(':', '').partition('.')[0]
parser = argparse.ArgumentParser()
parser.add_argument("--from-file", "-f", action="store_true")
parser.add_argument("characters", nargs='*', type = lambda s: unicode(s, 'utf8'))

args = parser.parse_args()

if(args.from_file):
    with io.open('resources/input', 'r', encoding='utf8') as input_f:
        input_lines = input_f.readlines()

    output_lines = []
    for line in input_lines:
        output_lines.append(get_middle_chinese_for_character(line.strip()) + '\n')


    with io.open('resources/output', 'w', encoding='utf8') as output_f:
        for line in output_lines:
            output_f.write(line)
else:
    for character in args.characters:
        print get_middle_chinese_for_character(character)