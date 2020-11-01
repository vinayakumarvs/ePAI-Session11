# image_resizer.py resize the images

import imageresizer
import argparse


if __name__=='__main__':

    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(help='Choose a functionality.', dest='functionality')

    res_p_parser = subparsers.add_parser('res_p', help='image resize using realtive percentage')
    res_p_parser.add_argument('-fp', '--source_path', type=str, required=True, help='parent folder of the source images')
    res_p_parser.add_argument('-p', '--percentage', type=int, required=True, help='relative size percentage of the output images')

    res_w_parser = subparsers.add_parser('res_w', help='image resize to new width')
    res_w_parser.add_argument('-fp', '--source_path', type=str, required=True, help='parent folder of the source images')
    res_w_parser.add_argument('-w', '--width', type=int, required=True, help='reqired width for the output images')

    res_h_parser = subparsers.add_parser('res_h', help='image resize to new height')
    res_h_parser.add_argument('-fp', '--source_path', type=str, required=True, help='parent folder of the source images')
    res_h_parser.add_argument('-H', '--height', type=int, required=True, help='reqired height for the output images')

    args = parser.parse_args()
    if args.functionality == 'res_p':
        image_resize_pct(args.source_path, args.percentage)
    elif args.functionality == 'res_w':
        image_resize_width(args.source_path, args.width)
    elif args.functionality == 'res_h':
        image_resize_height(args.source_path, args.height)
