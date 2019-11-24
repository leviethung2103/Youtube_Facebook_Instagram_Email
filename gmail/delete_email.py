"""Delete a Message.
"""

from apiclient import errors


def DeleteMessage(service, user_id, msg_id):
  """Delete a Message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: ID of Message to delete.
  """
  try:
    service.users().messages().delete(userId=user_id, id=msg_id).execute()
    print ('Message with id: %s deleted successfully.' % msg_id)
  except Exception as error:
    print ('An error occurred: %s' % error)