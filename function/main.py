from googleapiclient import discovery
from oauth2client.client import GoogleCredentials


def handler(request):
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)
    project_body = {
        'name': 'Test Project',
        'projectId': 'hurricane-59'
    }
    request = service.projects().create(body=project_body)
    request.execute()

    return 'request = \n' + request