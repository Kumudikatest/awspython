import boto3
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
    
    return {"message": "Successfully executed"}
