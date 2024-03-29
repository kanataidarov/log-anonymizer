from argparse import ArgumentParser
from const import Optionals, Positionals
from custom_argparse import CustomArgparseFormatter


def parse_args():
    arg_parser = ArgumentParser(description=description(), formatter_class=CustomArgparseFormatter)

    arg_parser.add_argument(Positionals.IN_DIR["name"], help=Positionals.IN_DIR["help"])
    arg_parser.add_argument(Positionals.OUT_DIR["name"], help=Positionals.OUT_DIR["help"])

    arg_parser.add_argument(Optionals.MSISDN_DUMMY["name"], default=Optionals.MSISDN_DUMMY["default"], type=str, help=Optionals.MSISDN_DUMMY["help"])

    parsed_args = arg_parser.parse_args()

    args = {
        "input_dir": parsed_args.input_dir,
        "output_dir": parsed_args.output_dir,
        "msisdn_dummy": parsed_args.msisdn_dummy
    }

    return args


def description():
    return """
     Anonymizes logs in specified directory and outputs to another directory.
     """
