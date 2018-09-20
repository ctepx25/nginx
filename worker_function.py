import boto3
import paramiko, json
def worker_handler(event, context):

    s3_client = boto3.client('s3')
    s3_client.download_file('ctepx-lambda-nginx','id_rsa', '/tmp/id_rsa')

    k = paramiko.RSAKey.from_private_key_file("/tmp/id_rsa")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    host = event['Records'][0]['body'].split(',')[0]
    action = event['Records'][0]['body'].split(',')[1]
    print "Connecting to " + host
    c.connect( hostname = host, username = "ubuntu", pkey = k )
    print "Connected to " + host

    command = 'echo '+action+' >> /tmp/log.txt'
    command2 = 'sed \'s/VERSION=1/VERSION=2/g\' /home/ubuntu/nginx/docker-compose.yml > /tmp/docker-compose.yml;docker-compose -f /tmp/docker-compose.yml up --build -d'
    
    print "Executing {}".format(command)
    print "Executing {}".format(command2)
    stdin , stdout, stderr = c.exec_command(command)
    stdin , stdout, stderr = c.exec_command(command2)
    print stdout.read()
    print stderr.read()

    return
    {
        "statusCode": 200,
        "body": json.dumps('Hello from Lambda!')
    }
