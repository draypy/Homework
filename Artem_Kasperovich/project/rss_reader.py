import argparse
import logging
import os
import sys

sys.path.append(os.path.abspath(os.pardir))
from .parse_news import NewsParser, ParserError
from .converter import convert_to_html, PDF

VERSION = 'Version 4.0'


def create_arguments() -> argparse.Namespace:
    """ Obtaining information about the necessary processes
        Attributes:
            --version          Print version info
            --json             Print result as JSON in stdout
            --verbose          Outputs verbose status messages
            --limit LIMIT      Limit news topics if this parameter provided
            --date DATE        Date
            --to-html TO_HTML  Make .html file
            --to-pdf TO_PDF    Make pdf file
        :return: parser with arguments that user print
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("source", nargs="?", type=str, help="RSS URL")
    parser.add_argument("--version", help="Print version info",
                        action="version", version=VERSION)
    parser.add_argument("--json", help="Print result as JSON in stdout",
                        action="store_true")
    parser.add_argument("--verbose", help="Outputs verbose status messages",
                        action="store_true")
    parser.add_argument("--limit", type=int, help="Limit news topics if this "
                                                  "parameter provided")
    parser.add_argument("--date", type=str, help="Date")
    parser.add_argument('--to-pdf', action='store_true', required=False,
                        help="PDF which format will be generated")
    parser.add_argument('--to-html', action='store_true', required=False,
                        help="HTML which format will be generated")
    return parser.parse_args()


def main():
    logger = logging.getLogger(__name__)
    args = create_arguments()
    try:
        if args.verbose:
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s: %(message)s')
        logger.info("starting the process")
        parser = NewsParser(args.source, limit=args.limit, json_format=args.json,
                            date=args.date)
        parser.parse()
        parser.write_json()
        print(parser)
        html_path = os.path.join(os.path.dirname(__file__), "output_files", "news.html")
        pdf_path = os.path.join(os.path.dirname(__file__), "output_files", "news.pdf")
        if args.to_pdf:
            pdf = PDF(parser, pdf_path)
            pdf.create_pdf()
        if args.to_html:
            convert_to_html(parser, html_path)
    except ParserError:
        pass
    logger.info("End process!")


if __name__ == '__main__':
    main()
