import os 
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="This script download the Youtube Videos",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--folder-dst", type=str, required=False, default = '/home/hunglv/Youtube/',
                        help="folder destination")
    parser.add_argument("--url", type=str, required = False, default = 'https://www.youtube.com/user/francishung1708/videos',
                        help="download link")

    args = parser.parse_args()
    return args

def main():
    args = get_args()

    # Setting parameters
    url = args.url
    folder_dst = args.folder_dst

    cmd = 'cd ' + folder_dst
    os.system(cmd)

    cmd = "youtube-dl -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' " + url
    os.system(cmd)

if __name__ == '__main__':
    main()