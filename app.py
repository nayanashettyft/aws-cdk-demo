#!/usr/bin/env python3

from aws_cdk import core
import aws_cdk.aws_sqs as sqs

from hello_cdk.hello_cdk_stack import HelloCdkStack

stack_tags = {"systemCode": "id-rnd", 
    "teamDL": "ent.svcs.fs.id@ft.com",
    "environment": "d"}

app = core.App()
HelloCdkStack(app, "hello-cdk", tags=stack_tags)

app.synth()
