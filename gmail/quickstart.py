from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from get_gmail import *
# from delete_email import *
# If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
# SCOPES = ['https://www.googleapis.com/auth/gmail']
SCOPES = 'https://mail.google.com/'

# Get the authentication at here: https://developers.google.com/gmail/api/quickstart/python#step_3_set_up_the_sample
# Install the package 
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


def init(user_id = 'me'):
    global service

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)

def search(query, user_id='me'):
    """Returns a list of gmail thread objects of all the messages matching query
    Ref: https://gist.github.com/saralgyaan/bb005d371bcf0bacd9cec06e21708a50
    Parameters
    __________
    query : str
        The string Exactly you will use in Gmail's Search Box
        label:UNREAD
        from:abc@email.com
        subject:hello
        has:attachment
        more described at https://support.google.com/mail/answer/7190?hl=en
    user_id : str
        User id of the Gmail User (default is 'me')
    Returns
    _______
    list
        List of Messages that match the criteria of the query.
        Note that the returned list contains Message IDs, you must use get with the appropriate ID to get the details of a Message.
    """

    if service is None:
        init()

    try:
        response = service.users().messages().list(userId=user_id,
                                                   q=query).execute()
        # print (response)
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])
            print ("This one")

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId=user_id, q=query,
                                                       pageToken=page_token).execute()
            messages.extend(response['messages'])
        # print (messages)
        # print(len(messages))
        return messages
        
   
    except errors.HttpError as error:
        print (f'An error occured: {error}')


def delete_messages(query, user_id='me'):
    """Deletes the message matching the query
    Parameters
    __________
    query : str
        The string Exactly you will use in Gmail's Search Box
        label:UNREAD
        from:username@email.com
        subject:hello
        has:attachment
        more described at https://support.google.com/mail/answer/7190?hl=en
    user_id : str
        User id of the Gmail User (default is 'me')
    """
    messages = search(query)
    if messages:
        for message in messages:
            service.users().messages().delete(userId=user_id, id=message['id']).execute()
            print (f'Message with id: {message["id"]} deleted successfully.')

    else:
        print ("There was no message matching the query.")


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """    
    if service is None: 
        init()

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])
    results = service.users().messages().list(userId='me').execute()
    print (results)

    # GetMessage(service,"me",)

if __name__ == '__main__':
    init()
    delete_messages('Google calendar')