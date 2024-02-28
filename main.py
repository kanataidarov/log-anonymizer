from args_parser import parse_args
from log_anonymizer import LogAnonymizer


def main():
    args = parse_args()
    la = LogAnonymizer(args)

    la.process_files()


if __name__ == '__main__':
    main()
