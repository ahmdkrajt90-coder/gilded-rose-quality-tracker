def handler(request):
    """
    Minimal Vercel Python serverless function.
    Visit /api/hello to verify the deployment is reachable.
    """
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": '{"message": "hello from gilded-rose-quality-tracker"}',
    }
