# this messily converts manual text file saves of chats into
# a starting point for markdown formatting, ready to refine.
# refining the results of this script required manual work.

import os

with open("excluded-lines", 'r') as f:
    excluded_lines = f.readlines()

dirname = "manual-data-retention/"

for filename in os.listdir(dirname):
    if os.path.isdir(filename) or not filename.endswith(".txt"):
        continue
    
    with open(f"{dirname}{filename}", 'r') as f:
        data = f.readlines()

    you_said = False
    it_said = False
    skip_next_line = False
    inline_next_sequence = False
    last_line_had_content = False

    sequence = []
    chunk_temp = ""
    line_builder = ""

    for (i, line) in enumerate(data):
        if line.endswith("You said:\n"):
            if it_said:
                sequence.append(chunk_temp)
                chunk_temp = ""
            you_said = True
            it_said = False
            # print("you said something")
            continue
        elif line.endswith(f"{excluded_lines[0].strip()} said:\n"):
            # if you_said:
            #     sequence.append(chunk_temp)
            #     chunk_temp = ""
            you_said = False
            it_said = True
            inline_next_sequence = False
            last_line_had_content = False
            # print("it said something")
            continue

        if line in excluded_lines:
            continue

        if skip_next_line:
            skip_next_line = False
            continue

        if you_said:
            chunk_temp += line
        elif it_said:
            last_line_had_content = data[i - 1].strip() != ""

            # if line.strip(" .\n").isnumeric():
            #     last_line_had_content = True
            #     skip_next_line = True
            #     line = f"\n> {line.strip(" \n")}"
            # elif line.strip(" :\n").endswith("*") and line.strip(" :\n").startswith("*"):
            #     last_line_had_content = True
            #     skip_next_line = True
            #     line = f" {line.strip(" \n")} "

            if last_line_had_content:
                line_builder += f" {line.strip()}"
            else:
                chunk_temp += f"> {line_builder}  \n"
                line_builder = f"{line.rstrip('\n')}"

            # if not line.strip():
            #     inline_next_sequence = False
            # else:
            #     # line = f"\n{line}"
            #     inline_next_sequence = True
            # else:
            #     if inline_next_sequence:
            #         line = f"{line.replace('\n', '').lstrip(" *")} "
            #     else:
            #         line = f"> {line.replace('\n', '')}  \n"
            # chunk_temp += line

    sequence.append(chunk_temp)

    destination = f"formatted-raw/{filename[0:2]}.md"
    with open(destination, 'w') as f:
        f.write('\n'.join(sequence))
        print(f"file written: {destination}")
