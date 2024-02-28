import os
import re


class LogAnonymizer:
    """Class for anonymizing MSISDN values in log files.

   This class reads log files from an input directory, replaces values with dummy values,
   processes according to logic (defined in `process_files()` method),
   and writes the anonymized logs to an output directory.

   Args:
       args (dict): A dictionary containing configuration parameters for the anonymization process.
       The following keys are expected:
       - input_dir (str): The path to the input directory containing log files.
       - output_dir (str): The path to the output directory where anonymized logs will be saved.
       - msisdn_dummy (str): The dummy value to use for replacing MSISDN numbers.
    """

    def __init__(self, args):
        self.args = args

    def process_files(self):
        """Reads all files from the specified input directory line by line, processes them according to rules,
        and outputs them to files with the same name in the specified output directory.
        """

        input_dir = self.args["input_dir"]
        output_dir = self.args["output_dir"]

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
                        line = self.replace_msisdn_in_path(line)
                        line = self.replace_msisdn_in_body(line)
                        output_file.write(line)
                except UnicodeDecodeError:
                    print(f"Error: Unable to decode file `{input_file.name}`")

    def replace_msisdn_in_body(self, line):
        """Replaces the MSISDN value in a given line of text with a dummy value.

        Args:
            line (str): The line of text to modify.

        Returns:
            str: The modified line of text with the MSISDN value replaced.

        This function is used to anonymize MSISDN (Mobile Station International Subscriber Directory Number)
        values in text data. It uses a regular expression to find and replace the MSISDN value with a dummy
        value stored in the `self.args["msisdn_dummy"]` attribute.

        **Note:** This function assumes that the MSISDN value is always enclosed in double quotes and
        preceded by the string `"msisdn":`. If the format of the data is different, the regular expression
        pattern will need to be modified accordingly.
        """

        # Regular expression pattern to find and replace "msisdn" value
        pattern = r'"msisdn"\s*:\s*"\d+"'
        replacement = f'"msisdn":"{self.args["msisdn_dummy"]}"'

        # Perform the replacement
        modified_string = re.sub(pattern, replacement, line)

        return modified_string

    def replace_msisdn_in_path(self, line):
        """Replaces the MSISDN value in a URL path with a dummy value.

        Args:
            line (str): The URL path to modify.

        Returns:
            str: The modified URL path with the MSISDN value replaced.

        This function is used to anonymize MSISDN (Mobile Station International Subscriber Directory Number)
        values in URL paths. It uses a regular expression to find and replace the MSISDN value with a dummy
        value stored in the `self.args["msisdn_dummy"]` attribute.

        **Note:** This function assumes that the MSISDN value is in the format `msisdn=`, followed by a
        sequence of digits. If the format of the data is different, the regular expression pattern will need
        to be modified accordingly.
        """

        pattern = r'msisdn=\d+'
        replacement = f'"msisdn":"{self.args["msisdn_dummy"]}"'

        modified_string = re.sub(pattern, replacement, line)

        return modified_string
