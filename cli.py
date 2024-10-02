import argparse

def main():
    parser = argparse.ArgumentParser(description="Parse filename or torrent name using Parsett")
    parser.add_argument('filename', type=str, help="Parse filename")

    args = parser.parse_args()

    if args.filename:
        from PTT import parse_title
        print(parse_title(args.filename))

if __name__ == "__main__":
    main()