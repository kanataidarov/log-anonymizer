class Positionals:
    IN_DIR = {"name": "input_dir", "help": "Directory with files to process."}
    OUT_DIR = {"name": "output_dir", "help": "Directory with files to put processed files."}


class Optionals:
    MSISDN_DUMMY = {"name": "--msisdn_dummy", "default": "<11-значный CTN>",
                    "help": "All MSISDNs should be replaced with given value."}
