import json
import os
import urllib.request
import sys

# Original Code : https://github.com/benhoff/facebook_api_script/blob/master/get_facebook_pictures.py
# Modify the code for our purpose with TOKEN

def return_data_new(url,token):
    ''' Token + URL '''
    url = url+ "&access_token=" + token
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    encoding = response.headers.get_content_charset()
    data = json.loads(response.read().decode(encoding))
    return data

# def return_data(url, api_key):
#     request = urllib.request.Request(url)
#     request.add_header('Authorization', 'Bearer {}'.format(api_key))

#     response = urllib.request.urlopen(request)
#     encoding = response.headers.get_content_charset()

#     data = json.loads(response.read().decode(encoding))
    
#     return data 

def get_next_from_data(data):
    if 'paging' in data:
        paging = data['paging']
        if 'next' in paging:
            return paging['next']
        else:
            return None
    else:
        return None

def parse_images(data, user_id, picture_number):
    # Facebook defaults to returning 25 pictures
    for data_object in data:
        picture_url = data_object['source']
        f = open('{}.jpg'.format(picture_number), 'wb')
        f.write(urllib.request.urlopen(picture_url).read())
        f.close()


        # Increment picture number for each picture 
        picture_number = picture_number + 1

def record_face_percentages_from_pictures(data, user_id, picture_number):

    face_coordinate_file = open('face_coordinates.txt', 'a')

    # Every data obj has 25 pictures in it
    for data_object in data:
        picture_tags = data_object['tags']['data']
        for data_tag in picture_tags:
            # FIXME: Not working correctly, getting too many tags
            # add in functionality to just get the id tags out
            if 'id' in data_tag:
                if data_tag['id'] == user_id:
                    x_face_coordinate = data_tag['x']
                    y_face_coordinate = data_tag['y']
                    face_coordinate_file.write(
                            "{},{},{}\n".format(picture_number,
                                                x_face_coordinate,
                                                y_face_coordinate))

        picture_number = picture_number + 1
    face_coordinate_file.close()

def download_albums():
    facebook_token = "EAAHW0mu5HWwBAFnOsgzptRaUfkoiYUwOGfGswcbhSX91BCsLGHObqVyzRyUeFVv1lCykrJpB6U37MqXnHj1I7DGCvqGbgirnhELpr8yIhNMJ8tYmnV9TF72OkvnYf4ZAZCGHilZAQfJ2KEBLu6tTgC1ZAZC2pk8Ly6zvi90GpKYjdgERCNevZCK7mgLpt7gkbUlkVJECbwnwiEE3p61pD7sMesKfvZCIXjO8rDYAmllEwZDZD"
    # TODO: create face_coordinate file off the get go/ or something
    base_url = "https://graph.facebook.com/v2.3/"
    data = return_data_new(base_url+"me?fields=id,name",facebook_token)

    # Make dir for pcitures and change into that directory
    if not os.path.exists("pictures"):
        os.makedirs("pictures")
    os.chdir("pictures")


    # This is getting out the user id!
    data = return_data_new(base_url+"me?", facebook_token)
    # Will need id for parsing photo tags
    user_id = data['id']
    print ("User ID: ",user_id)


    # This is getting out the first set of pictures!
    data = return_data_new(base_url+"me/albums?", facebook_token)
    data = data['data']

    list_album = []
    for data_object in data:
        album_id = data_object['id']
        list_album.append(album_id)

    # get the list of photos for each albums
    test_id = '152848714865205'
    data = return_data_new(base_url+test_id+"/photos?",facebook_token)
    print (data)

    # next_ = get_next_from_data(data)

    # print (next_)

    data = return_data_new(base_url+"me/albums?", facebook_token)


def main():
    facebook_token = "EAAHW0mu5HWwBAFnOsgzptRaUfkoiYUwOGfGswcbhSX91BCsLGHObqVyzRyUeFVv1lCykrJpB6U37MqXnHj1I7DGCvqGbgirnhELpr8yIhNMJ8tYmnV9TF72OkvnYf4ZAZCGHilZAQfJ2KEBLu6tTgC1ZAZC2pk8Ly6zvi90GpKYjdgERCNevZCK7mgLpt7gkbUlkVJECbwnwiEE3p61pD7sMesKfvZCIXjO8rDYAmllEwZDZD"
    # TODO: create face_coordinate file off the get go/ or something
    base_url = "https://graph.facebook.com/v2.3/"
    data = return_data_new(base_url+"me?fields=id,name",facebook_token)
    
    test_id = "100006599881056"
    data = return_data_new(base_url+test_id+"/photos?",facebook_token)
    print (data)

    quit()

    #super secret api password thingy!
    # facebook_api_key = os.getenv('FACEBOOK_API_KEY')

    # Make dir for pcitures and change into that directory
    if not os.path.exists("pictures"):
        os.makedirs("pictures")
    os.chdir("pictures")

    # If this script is run multiple times, removes issues with appending coords
    if os.path.isfile('face_coordinates.txt'):
        os.remove('face_coordinates.txt')
    
    # This is getting out the user id!
    data = return_data_new(base_url+"me?", facebook_token)
    # Will need id for parsing photo tags
    user_id = data['id']
    print ("User ID: ",user_id)

    # This is getting out the first set of pictures!
    data = return_data_new(base_url+"me/photos?", facebook_token)
    next_ = get_next_from_data(data)

    print (next_)

    data = data['data']
    picture_number = 0
    parse_images(data, user_id, picture_number)
    record_face_percentages_from_pictures(data, user_id, picture_number)
    picture_number += len(data)
    print(len(data))
    
    # if next_ is None:
    #     more_photos = False
    # else:
    #     more_photos = True 

    # while(more_photos):
    #     data = return_data(next_, facebook_api_key)
    #     next_ = get_next_from_data(data)

    #     data = data['data']
    #     parse_images(data, user_id, picture_number)
    #     record_face_percentages_from_pictures(data, user_id, picture_number)

    #     picture_number += len(data)
    #     print(len(data))
    #     if next_ is None:
    #         more_photos=False

    # print("Done!")

if __name__ == '__main__':
    main()
    # download_albums()