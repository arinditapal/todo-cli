from argparse import ArgumentParser
from handler import show_handler, add_handler, delete_handler, update_handler



parser = ArgumentParser()

parser.add_argument("operation", help="operation you want to do with todos", choices=["show", "add", "delete", "update"])

# array of all command line arguments
args = parser.parse_args()


if args.operation == "show":
    show_handler()
elif args.operation == "add":
    add_handler()
elif args.operation == "delete":
    delete_handler()
elif args.operation == "update":
    update_handler()