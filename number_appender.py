import os
import re

# Directory containing the markdown files
directory = "proposals"

# Regular expression to match the proposal line and extract the identifier
proposal_pattern = re.compile(r"\* Proposal: \[(SE-\d+)\]\((.*?)\)")

for filename in os.listdir(directory):
    if filename.endswith(".md"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Extract the title and identifier
        title = lines[0].strip()[2:].strip()  # Remove the '# ' from the start and any trailing whitespace
        identifier = None
        for line in lines:
            match = proposal_pattern.match(line.strip())
            if match:
                identifier = match.group(1)  # Extract the identifier
                break

        if identifier:
            # Only prepend if the identifier is not already in the title
            if not title.startswith(identifier):
                modified_title = f"# {identifier} - {title}\n"
                lines[0] = modified_title  # Replace the first line with the modified title

                # Write the changes back to the file
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.writelines(lines)
            else:
                print(f"Identifier already present in the title of {filename}")
        else:
            print(f"No identifier found in {filename}")
