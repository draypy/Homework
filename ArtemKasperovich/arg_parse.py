import argparse

parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader.')
parser.add_argument('source', help='RSS URL', nargs='?')
parser.add_argument("--version", help='Print version info', action='store_true')
parser.add_argument("--json",   action='store_true', help="Print version JSON in stdout")
parser.add_argument("--verbose", action='store_true', help="Outputs verbose status messages")
parser.add_argument("--limit", help="Limit new topics if parameter provided", type=int)
args = parser.parse_args()
