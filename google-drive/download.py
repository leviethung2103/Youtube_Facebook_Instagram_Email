import argparse
import gdown

def get_args():
    parser = argparse.ArgumentParser(description="This script download the Youtube Videos",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--id", type=str, required=True, default = '',
                        help="id of link")
    parser.add_argument("--unzip", type=bool, required = False, default = False,
                        help="unzip after the dowload")
    parser.add_argument("--dst-path", type=str, default="",help = "destination path")
    args = parser.parse_args()
    return args

def main():
    args = get_args()

    gdown.download(args.id,args.dst_path,quiet=False)

if __name__ == '__main__':
    main()