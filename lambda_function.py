def lambda_handler(event, context):
    import subprocess
    result = subprocess.call("curl -I http://HOST/lambda.php?command=deploy", shell=True)
    return result
