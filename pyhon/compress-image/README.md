# ⚡ compressImage()

A Python Cloud Function for compressing Image using [Deepgram](https://deepgram.com/)

_Example function payload:_

```json
{
  "fileUrl": ""
}
```

_Successful function response::_

```json
{ "success": true, "image":"iVBORw0KGgoAAAANSUhE...o6Ie+UAAAAASU5CYII=" }
```

_Error function response:_

```json
{"success":false,"message":"Input file is not an image."}
```
