import os 
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="This script download the Youtube Videos",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dst", type=str, required=False, default = '/home/hunglv/Youtube/',
                        help="folder destination")
    parser.add_argument("--url", type=str, required = False, default = 'https://www.youtube.com/user/francishung1708/videos',
                        help="download link")
    parser.add_argument("--res", type=int, default=720,help = "Download video with specific resolution")

    parser.add_argument("--playlist", type=bool, default = False, help="download playlist or a video")
    parser.add_argument("--only-audio", type=bool, default=False, help = "Downlaod only sound")

    args = parser.parse_args()
    return args

def main():
    args = get_args()

    # Setting parameters
    url = args.url
    folder_dst = args.dst
    resolution = args.res

    if not os.path.exists(folder_dst):
        os.mkdir(folder_dst)

    video_sound = ''

    if args.only_audio==True: 
        # dowload only audio
        video_sound = f"-f 'bestaudio/best[height<={resolution}]'"
    else: 
        # dowload only video
        video_sound = f"-f 'bestvideo[height<={resolution}]+ bestaudio/best[height<={resolution}]'"
        # video_sound = f"-f 'bestvideo[ext=mp4]'"


    if args.playlist==False:
        cmd = "youtube-dl -o {}/'%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s'".format(folder_dst) + " "  + url + " " + video_sound
        os.system(cmd)
    else:
        cmd = "youtube-dl -o {}/'%(title)s-%(id)s.%(ext)s'".format(folder_dst) + " " + url + " "+ video_sound
        os.system(cmd)

if __name__ == '__main__':
    main()