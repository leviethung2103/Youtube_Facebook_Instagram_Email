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
Install the UniDecode package
```
pip install unidecode
```
### Download Youtube Videos

Run the python script to download the videos at current directory

```
python downloads_YTvideos.py --folder-dst ./ --url 
```

### Arguments
```
-- folder-dst: Where to save videos
-- url : Download link
```

### Post Processing After Downloading
* Decode the Unicode: convert Tiếng Việt to Tieng Viet
* Rename the filenames 

`filter_videos.py`

* work with file name as Unicode type
* rename the old names with new file names
