# Importing Required Modules
# import backgourndremover
import requests

def remove_bg(input_path,filename):
    output_path = 'media/'+filename
    
    url = 'https://api.remove.bg/v1.0/removebg'
    api_key = 'pLUodtyNvnxfRBjSFzWk5wBr'
    image=open(input_path, 'rb')
    headers = {'X-API-Key': api_key}
    data = {
        'size': 'auto',
    }
    files={'image_file': image}


    response = requests.post(url, headers=headers, data=data,files=files)

    with open(output_path, 'wb') as f:
        f.write(response.content)
    return output_path
