import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Parse filename or torrent name using Parsett")
    parser.add_argument('filename', type=str, help="The name of the file or torrent to be parsed")
    parser.add_argument('-a', '--anime', action='store_true', help="Enable parsing of anime titles")
    parser.add_argument('-tl', '--translate-languages', action='store_true', help="Translate language codes (e.g., 'en', 'jp') to their full language names (e.g., 'English', 'Japanese')")

    args = parser.parse_args()
    if not args.filename:
        parser.print_help()
        sys.exit(1)

    from PTT import parse_title

    print(
        parse_title(
            args.filename,
            translate_languages=args.translate_languages,
            parse_anime=args.anime
        )
    )

if __name__ == "__main__":
    main()