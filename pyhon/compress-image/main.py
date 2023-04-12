import tinify
import krakenio

def compress_image(provider, image):
    if provider == "tinypng":
        tinify.key = "your_tinypng_secret_key"
        source = tinify.from_buffer(image)
        return {"success": True, "image": source.to_buffer()}
    elif provider == "krakenio":
        kraken = krakenio.Client(api_key='your_krakenio_secret_key')
        response = kraken.upload(image)
        if response['success']:
            compressed_image = kraken.url(response['kraked_url'])
            return {"success": True, "image": compressed_image}
        else:
            return {"success": False, "message": response['message']}
    else:
        return {"success": False, "message": "Invalid provider}
                
      
# The function receives a payload in base64 format containing the provider to use and the image to compress. The compressed version is returned in base64 format.

# For example, if you want to compress an image using tinypng:
                

import base64

payload = {"provider":"tinypng","image":"iVBORw0KGgoAAAANSUhEUgAAAaQAAALiCAY...QoH9hbkTPQAAAABJRU5ErkJggg=="}

provider = payload["provider"]
image = base64.b64decode(payload["image"])

result = compress_image(provider, image)

if result["success"]:
    compressed_image = base64.b64encode(result["image"]).decode('utf-8')
    print({"success": True,"image": compressed_image})
else:
    print({"success": False,"message": result["message"]})
    
    
    
# The output will be:

# {"success":true,"image":"iVBORw0KGgoAAAANSUhE...o6Ie+UAAAAASU5CYII="}
# If there’s an error during the compression process:


import base64

payload = {"provider":"tinypng","image":"iVBORw0KGgoAAAANSUhEUgAAAaQAAALiCAY...QoH9hbkTPQAAAABJRU5ErkJggg=="}

provider = payload["provider"]
image = base64.b64decode(payload["image"])

result = compress_image(provider, image)

if result["success"]:
    compressed_image = base64.b64encode(result["image"]).decode('utf-8')
    print({"success": True,"image": compressed_image})
else:
    print({"success": False,"message": result["message"]})

    
    
# The output will be:
# {"success":false,"message":"Input file is not an image."}
