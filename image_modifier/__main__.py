from j2p_f import j2p
from p2j_f import p2j
from imageresizer_f import imageresizer
from imagecropper_f import imagecropper
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)

    subparsers = parser.add_subparsers(help='Choose a functionality.', dest='functionality')

    j2p_parser = subparsers.add_parser('j2p', help='jpg/jpeg to png conversion')
    j2p_parser.add_argument('-ip', '--source_path', type=str, required=True, help='path of the source image')

    p2j_parser = subparsers.add_parser('p2j', help='jpg/jpeg to png conversion')
    p2j_parser.add_argument('-ip', '--source_path', type=str, required=True, help='path of the source image')

    res_p_parser = subparsers.add_parser('res_p', help='image resize using realtive percentage')
    res_p_parser.add_argument('-fp', '--source_path', type=str, required=True, help='parent folder of the source images')
    res_p_parser.add_argument('-p', '--percentage', type=int, required=True, help='relative size percentage of the output images')

    res_w_parser = subparsers.add_parser('res_w', help='image resize to new width')
    res_w_parser.add_argument('-fp', '--source_path', type=str, required=True, help='parent folder of the source images')
    res_w_parser.add_argument('-w', '--width', type=int, required=True, help='reqired width for the output images')

    res_h_parser = subparsers.add_parser('res_h', help='image resize to new height')
    res_h_parser.add_argument('-fp', '--source_path', type=str, required=True, help='parent folder of the source images')
    res_h_parser.add_argument('-H', '--height', type=int, required=True, help='reqired height for the output images')

    crp_px_parser = subparsers.add_parser('crp_px', help='center crop images of required dimensions')
    crp_px_parser.add_argument('-fp', '--source_path', type=str, required=True, help='parent folder of the source images')
    crp_px_parser.add_argument('-w', '--width', type=int, required=True, help='reqired width for the output images')
    crp_px_parser.add_argument('-H', '--height', type=int, required=True, help='reqired height for the output images')

    crp_p_parser = subparsers.add_parser('crp_p', help='center crop images of required relative percentage')
    crp_p_parser.add_argument('-fp', '--source_path', type=str, required=True, help='parent folder of the source images')
    crp_p_parser.add_argument('-p', '--percentage', type=int, required=True, help='reqired relative percentage size for the output images')
    
    # parser.add_argument('source_path', type=str, help="source path")

    # parser.add_argument('-j2p',action='store_true', help="converter from jpeg to png") 
    # parser.add_argument('-p2j',action='store_true', help="converter from png to jpg") 

    # parser.add_argument('-res_p', type=int, help="proportion percentage")
    # # parser.add_argument('-source_path', type = str)
    # # parser.add_argument('-p', type = int)

    # parser.add_argument('-res_w', type=int, help="image width")
    # parser.add_argument('-res_h', type=int, help="image height")

    # parser.add_argument('-crp_px', nargs='+', type=int, help="pixel size in tuple (width, height")
    # parser.add_argument('-crp_p', nargs='+', type=int, help="percentage width and height")

    args = parser.parse_args()

    if args.functionality == 'j2p':
        j2p.convert_to_png(args.source_path)
    elif args.functionality == 'p2j':
        p2j.convert_to_jpg(args.source_path)
    elif  args.functionality == 'res_p':
        imageresizer.image_resize_pct(source_path=args.source_path,res_p=args.percentage)
    elif args.functionality == 'res_w':
        imageresizer.image_resize_width(source_path=args.source_path, res_w=args.width)
    elif args.functionality == 'res_h':
        imageresizer.image_resize_height(source_path=args.source_path, res_h=args.height)
    elif args.functionality == 'crp_px':
        imagecropper.image_crop_size(source_path=args.source_path, crp_px=(args.width, args.height))
    elif args.functionality == 'crp_p':
        imagecropper.image_crop_pct(source_path=args.source_path, crp_p=args.percentage)
    else:
        print(f"No option provided, please provide one of ['-j2p','-p2j','-res_p','-resp_w','-res_h','-crp_px','-crp_p']")
        
