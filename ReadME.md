### Installation
To install it right away for all UNIX users (Linux, macOS, etc.), type:
```bash
sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
```

If you do not have curl, you can alternatively use a recent wget:

```bash
sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
```

### Run

Run the python script to download the videos at current directory

```
python downloads_YTvideos.py --folder-dst ./ 
```

### Arguments
```
-- dst_path: Where to save videos
-- url : Download link
```

