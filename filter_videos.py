import os 
import pandas as pd
import string
import re
from unidecode import unidecode


directory = 'Uploads from Francis Hung - Corporate Master Trainer'
origin = [i for i in sorted(os.listdir(directory))]


for video in sorted(os.listdir(directory)):
	new_name = unidecode(video).lower()
	new_name = new_name.replace("francis hung","")
	new_name = new_name.replace("-","")
	new_name = " ".join(new_name.split())
	full_name = os.path.join(directory,new_name)
	old_name = os.path.join(directory,video)
	os.rename(old_name,full_name)


# videos = [unidecode(i).lower() for i in sorted(os.listdir(directory))]

'''
# filter
videos = [video for video in videos  if 'hien the' not in video]
videos = [video for video in videos  if 'chua' not in video]
videos = [video.replace("francis hung","") for video in videos]
videos = [video.replace("-","") for video in videos]
videos = [" ".join(video.split()) for video in videos]

video_indices = [video[:3] for video in videos]
print (video_indices)


### Future
## rename the video names


## remove the non-useful videos
'''

# a = pd.DataFrame({'Video': videos})
# print (a.head())