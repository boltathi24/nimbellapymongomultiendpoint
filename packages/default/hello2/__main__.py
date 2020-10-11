from database import PyMongo
def main(request_data):
    global responseFromNimbella

    # Handle the input and configure the message
    try:
        responseFromNimbella=PyMongo.getAllData("User")
    except Exception as e:
        responseFromNimbella = str(e)

     # Send the message
    try:

        return {
            "body": {
                "status": (responseFromNimbella)
            }
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "body": {
                "error": str(e)
            }
        }

