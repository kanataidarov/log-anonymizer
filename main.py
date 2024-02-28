from args_parser import parse_args

import os
import re

msisdn_dummy = '<11-значный CTN>'


def replace_msisdn_in_body(input_string):
    # Regular expression pattern to find and replace "msisdn" value
    pattern = r'"msisdn"\s*:\s*"\d+"'
    replacement = f'"msisdn":"{msisdn_dummy}"'

    # Perform the replacement
    modified_string = re.sub(pattern, replacement, input_string)

    return modified_string


def replace_msisdn_in_path(input_string):
    # Regular expression pattern to find and replace "msisdn" value
    pattern = r'msisdn=\d+'
    replacement = f'"msisdn":"{msisdn_dummy}"'

    # Perform the replacement
    modified_string = re.sub(pattern, replacement, input_string)

    return modified_string


def process_files(input_dir, output_dir):
    """
    Reads all files from the specified input directory line by line, processes them according to rules,
    and outputs them to files with the same name in the specified output directory.

    Args:
        input_dir (str): Path to the input directory.
        output_dir (str): Path to the output directory.

    Raises:
        FileNotFoundError: If the input directory does not exist.
    """

    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"Input directory not found: {input_dir}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create output directory if it doesn't exist

    for filename in os.listdir(input_dir):
        input_filepath = os.path.join(input_dir, filename)
        output_filepath = os.path.join(output_dir, filename)

        with (open(input_filepath, 'r', encoding='utf-8') as input_file,
              open(output_filepath, 'w', encoding='utf-8') as output_file):
            print(f'processing {input_filepath}')
            try:
                for line in input_file:
                    line = replace_msisdn_in_path(line)
                    line = replace_msisdn_in_body(line)
                    output_file.write(line)
            except UnicodeDecodeError:
                print(f"Error: Unable to decode file")


def main():
    args = parse_args()

    process_files(args["input_dir"], args["output_dir"])


if __name__ == '__main__':
    main()
