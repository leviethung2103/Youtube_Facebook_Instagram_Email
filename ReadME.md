### Introduction

I've created an automation project that simply focuses on 4 platforms. 

* Youtube
* Facebook
* Gmail
* Instagram
* Google Drive API 

I've got the idea while I wanted to backup my Instagram account. Therefore, I need to download all the images and videos from my personal account. 

After searching on Internet for a while, I've found that the Instagram API really can help me to crawl the data from any users (public users and your friends), execpt private users.

Every section is describe clearly as following

**Table of contents**

1. Instagram
2. Youtube
3. Facebook
4. Gmail
5. Coursera
6. Google Drive Download API

### Environments

I highly recommend to use virtual environment with Python 3.6.

### 1. INSTAGRAM

I've utilized the [Instaloader](https://github.com/instaloader/instaloader) to download images and videos from Instagram. 

**Instaloader's benefits:**

- downloads **public and private profiles, hashtags, user stories, feeds and saved media**,
- downloads **comments, geotags and captions** of each post,
- automatically **detects profile name changes** and renames the target directory accordingly,
- allows **fine-grained customization** of filters and where to store downloaded media.
- downloads many profiles at the same time

#### 1.1. Installation

```bash
$ pip3 install instaloader
```

#### 1.2. Usage

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

### 2. YOUTUBE

#### 2.1 Installation

To install it right away for all UNIX users (Linux, macOS, etc.), type:
```bash
$ sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
$ sudo chmod a+rx /usr/local/bin/youtube-dl
```

If you do not have curl, you can alternatively use a recent wget:

```bash
$ sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
$ sudo chmod a+rx /usr/local/bin/youtube-dl
```
Install the UniDecode package
```bash
$ pip install unidecode
```
#### 2.2 Usage

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

#### 3. FACEBOOK (Under Development)

```bash
$ python facebook/get_FB_imgs.py
```

#### 4. GMAIL

The main file is `quickstart.py`. We will filter emails with keywords

Input the keyword in function `delete_messages`

For example, I want to delete emails that contain Google Calendar. 

```
delete_messages('Google calendar')
```

#### 5. COURSERA

To download the courses of Coursera, you need to create an account and register the courses that you want to download. 

If you don't already have one, create a Coursera account and enroll in a class. See https://www.coursera.org/courses for the list of classes.

#### 5.1 Installation

Firstly, download this repository at this link via command line

```bash
$ git clone https://github.com/coursera-dl/coursera-dl
$ cd coursera-dl
```

#### 5.2 Usuage

**Running the script:**

Run the script to download the materials by providing your Coursera account and password as well as the class names. You can specify some additional parameters:

```
$ python coursera-dl -u <email> <course-name> --subtitle-language en --path <download-folder> --download-delay 0 
```

```
If you don't want to type your password in command line as plain text, you can use the script without -p option. In this case you will be prompted for password once the script is run.

Parameters
--subtitle-language en
--download-delay 0 
--path 
```

If you encounter the problem: 

```
HTTPError: 400 Client Error: Bad Request for url: https://api.coursera.org/api/login/v3 
```

You need install the coursera-dl chrome browser extension:

https://github.com/e-learning-archive/browser-extension/ in order to get cookies of coursera from your web browesr. Copy cookies from the extension and put this argument inside the main command line above.

```
--cauth <your_cookie>
```

The full implementation would be

```bash
$ python coursera-dl -u <email> <course-name> --subtitle-language en --path <download-folder> --download-delay 0 --cauth <your_cookie>
```

For advanced user, there're another interesting arguments you can discover later on. Please take a look the original repo at reference. 

####  6. Google Drive
**Step 1:** Install the required packages - Google Client Library

```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

**Step 2: Turn on the Drive API** 

After turn on the drive API, you will get the `credentials.json` file.

**Step 3:** 



## References:

[Coursera Downloader](https://github.com/coursera-dl/coursera-dl)

https://developers.google.com/drive/api/v3/quickstart/python

