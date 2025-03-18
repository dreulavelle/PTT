import argparse
import sys
import os
import json

def main():
    parser = argparse.ArgumentParser(description="Parse filename or torrent name using Parsett")
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Parse command
    parse_parser = subparsers.add_parser('parse', help='Parse a filename or torrent name')
    parse_parser.add_argument('filename', type=str, help="The name of the file or torrent to be parsed")
    parse_parser.add_argument('-a', '--anime', action='store_true', help="Enable parsing of anime titles")
    parse_parser.add_argument('-tl', '--translate-languages', action='store_true', 
                            help="Translate language codes (e.g., 'en', 'jp') to their full language names (e.g., 'English', 'Japanese')")

    # Sort command
    sort_parser = subparsers.add_parser('sort', help='Sort a file by count. Requires `keyword,count` format on every line.')
    sort_parser.add_argument('filename', type=str, help='File to sort')

    # Combine command
    combine_parser = subparsers.add_parser('combine', help='Combine and sort keywords from txt files')
    combine_parser.add_argument('directory', type=str, help='Directory containing txt files')

    # Dedupe command
    dedupe_parser = subparsers.add_parser('dedupe', help='Deduplicate and sort a file by count. Requires `keyword` format on every line.')
    dedupe_parser.add_argument('filename', type=str, help='File to deduplicate and sort')

    args = parser.parse_args()

    if args.command == 'parse':
        if not args.filename:
            parser.print_help()
            sys.exit(1)

        from PTT import parse_title
        result = parse_title(
            args.filename,
            translate_languages=args.translate_languages
        )
        print(json.dumps(result, indent=4))
    elif args.command == 'sort':
        sort_by_count(args.filename)
    elif args.command == 'combine':
        combine_keywords(args.directory)
    elif args.command == 'dedupe':
        dedupe_and_sort(args.filename)
    else:
        parser.print_help()
        sys.exit(1)


def combine_keywords(directory: str) -> None:
    """Combine keywords from all txt files in directory into a single sorted list."""
    keywords = set()
    files_used = 0
    for filename in os.listdir(directory):
        if filename.endswith('.txt') and not "combined-keywords" in filename:
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                keywords.update(line.strip() for line in f if line.strip())
            files_used += 1

    # Write unique sorted keywords
    output_file = os.path.join(directory, 'combined-keywords.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        for keyword in sorted(keywords):
            f.write(f"{keyword}\n")
    
    print(f"Combined and sorted into {output_file.split('/')[-1]} using {files_used} files")


def sort_by_count(filename: str) -> None:
    """Sort a file by counts."""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Parse lines into tuples of (name, count)
    entries = []
    for line in lines:
        line = line.strip()
        if ',' in line:
            name, count = line.split(',')
            try:
                count = int(count)
                entries.append((name, count))
            except ValueError:
                continue

    sorted_entries = sorted(entries, key=lambda x: x[1], reverse=True)
    with open(filename, 'w', encoding='utf-8') as f:
        for name, count in sorted_entries:
            f.write(f"{name},{count}\n")

    print(f"Sorted by count {filename.split('/')[-1]}")


def dedupe_and_sort(filename: str) -> None:
    """Deduplicate and sort a file."""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    unique_keywords = set()
    for line in lines:
        keyword = line.strip()
        if keyword:
            unique_keywords.add(keyword)
    
    # write back a sorted list of unique keywords
    with open(filename, 'w', encoding='utf-8') as f:
        for keyword in sorted(unique_keywords):
            f.write(f"{keyword}\n")
    
    print(f"Deduplicated and sorted {filename.split('/')[-1]}")


if __name__ == "__main__":
    main()
