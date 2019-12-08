### 1. Introduction

I've created an automation project that simply focuses on 4 platforms. 

* Youtube
* Facebook
* Gmail
* Instagram

I've got the ideas while I wanted to backup my Instagram account. Therefore, I need to download all the images and videos from my personal account. 

After searching on Internet, I've found the Instagram API that can help me to scape the data from any users (public users and your friends). 

**Table of contents**

1. Introduction
2. Instagram
3. Youtube
4. Faebook

### Environments

I highly recommend to use virtual environment and following packages

* Python 3.6

### 2. INSTAGRAM

I utilized the [Instaloader](https://github.com/instaloader/instaloader) to download images and videos from Instagram. 

**Instaloader**

- downloads **public and private profiles, hashtags, user stories, feeds and saved media**,
- downloads **comments, geotags and captions** of each post,
- automatically **detects profile name changes** and renames the target directory accordingly,
- allows **fine-grained customization** of filters and where to store downloaded media.
- downloads many profiles at the same time

#### 2.1. How to install

```bash
pip3 install instaloader
```

#### 2.2. Usage

To **download all pictures and videos of a profile**, as well as the **profile picture**, do

```bash
 instaloader profile [profile ...]
```

where `profile` is the name of a profile you want to download. Instead of only one profile, you may also specify a list of profiles.

Instaloader can also be used to **download private profiles**. To do so, invoke it with

```bash
instaloader --login=your_username profile [profile ...]
```

When logging in, Instaloader **stores the session cookies** in a file in your temporary directory, which will be reused later the next time `--login` is given. So you can download private profiles **non-interactively** when you already have a valid session cookie file.

```bash
instaloader [--comments] [--geotags] [--stories] [--highlights] [--tagged]
            [--login YOUR-USERNAME] [--fast-update]
            profile | "#hashtag" | :stories | :feed | :saved
```



### 3. YOUTUBE

#### 3.1 Installation

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
```bash
pip install unidecode
```
#### 3.2 Usage

##### Download the Youtube videos by run the python script to download the videos at current directory

```
python youtube/downloads_YTvideos.py --folder-dst ./ 
```

```
arguments:
-- dst_path: Where to save videos
-- url : Download link
```

##### Post Processing After Downloading

* Decode the Unicode: convert Tiếng Việt to Tieng Viet
* Rename the filenames 

`filter_videos.py`

* work with file name as Unicode type
* rename the old names with new file names

#### 4. FACEBOOK (Under Development)

```
python facebook/get_FB_imgs.py
```

#### 5. GMAIL

The main file is `quickstart.py`. We will filter emails with keywords

Input the keyword in function `delete_messages`

For example, I want to delete emails that contain Google Calendar. 

```
delete_messages('Google calendar')
```

#### 6. COURSERA



To download the courses of Coursera, you need to create an account and register the courses that you want to download. 

If you don't already have one, create a Coursera account and enroll in a class. See https://www.coursera.org/courses for the list of classes.

**Running the script:** 

Run the script to download the materials by providing your Coursera account and password as well as the class names. You can specify some additional parameters:

```
python coursera-dl.py -u <email> <course-name>
```

```
If you don't want to type your password in command line as plain text, you can use the script without -p option. In this case you will be prompted for password once the script is run.


Parameters
--subtitle-language en
```

```
Without -p field:            coursera-dl -u <user> modelthinking-004
Multiple classes:            coursera-dl -u <user> -p <pass> saas historyofrock1-001 algo-2012-002
Filter by section name:      coursera-dl -u <user> -p <pass> -sf "Chapter_Four" crypto-004
Filter by lecture name:      coursera-dl -u <user> -p <pass> -lf "3.1_" ml-2012-002
Download only ppt files:     coursera-dl -u <user> -p <pass> -f "ppt" qcomp-2012-001
Use a ~/.netrc file:         coursera-dl -n -- matrix-001
Get the preview classes:     coursera-dl -n -b ni-001
Specify download path:       coursera-dl -n --path=C:\Coursera\Classes\ comnetworks-002
Display help:                coursera-dl --help

Maintain a list of classes in a dir:
  Initialize:              mkdir -p CURRENT/{class1,class2,..classN}
  Update:                  coursera-dl -n --path CURRENT `\ls CURRENT`
```

