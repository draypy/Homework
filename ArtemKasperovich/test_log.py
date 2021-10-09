import test_log as log
from arg_parse import *
if args.verbose:
    log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
    log.info("Verbose output.")
else:
    log.basicConfig(format="%(levelname)s: %(message)s")

log.info("This should be verbose.")
log.warning("This is a warning.")
log.error("This is an error.")