# imagecropper.py crop the images by size and percentages

from PIL import Image
import imagecropper
import argparse



if __name__=='__main__':

    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(help='Choose a functionality.', dest='functionality')

    crp_px_parser = subparsers.add_parser('crp_px', help='center crop images of required dimensions')
    crp_px_parser.add_argument('-fp', '--source_path', type=str, required=True, help='parent folder of the source images')
    crp_px_parser.add_argument('-w', '--width', type=int, required=True, help='reqired width for the output images')
    crp_px_parser.add_argument('-H', '--height', type=int, required=True, help='reqired height for the output images')

    crp_p_parser = subparsers.add_parser('crp_p', help='center crop images of required relative percentage')
    crp_p_parser.add_argument('-fp', '--source_path', type=str, required=True, help='parent folder of the source images')
    crp_p_parser.add_argument('-p', '--percentage', type=int, required=True, help='reqired relative percentage size for the output images')


    args = parser.parse_args()


    if args.functionality == 'crp_px':
        image_crop_size(args.source_path, (args.width, args.height))
    elif args.functionality == 'crp_p':
        image_crop_pct(args.source_path, args.percentage)
