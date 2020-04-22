import boto3
rekognition = boto3.client("rekognition")
translate = boto3.client("translate")

def handler(event, context):
    try:
        data = translate.translate_text(
            SourceLanguageCode="auto",
            TargetLanguageCode="en",
            Text="Hola"
        )
        print(data)
    except BaseException as e:
        print(e)
        raise(e)
        try:
            data = rekognition.detect_text(
                Image={
                    'S3Object': {
                        'Bucket': "cloud9-ktest",
                        'Name': "shot-buffalo-5daeeb9351a540214a19d115-wiu",
                        'Version': "png"
                    }
                }
            )
            print(data)
        except BaseException as e:
            print(e)
            raise(e)
    
    return {"message": "Successfully executed"}
