# convert_to_jpg
import p2j
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-ip','--source_path',type=str, help="source path of the images")

    args = parser.parse_args()
    convert_to_jpg(args.source_path)
