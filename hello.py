import click
import boto3


def add(x,y):
    return x+y

# subtle bug that may burn you

@click.command()

def buckets():
    """this will lists my S3 buckets"""
    s3 = boto3.client("s3")
    all_buckets = s3.list_buckets()
    
    for bucket in all_buckets['Buckets']:
        click.echo(
            click.style(f"mybuckets: {bucket['Name']}", bg="yellow", fg="blue")
        )


if __name__ == "__main__":
    buckets()