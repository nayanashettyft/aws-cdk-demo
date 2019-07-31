from aws_cdk import core
import aws_cdk.aws_sqs as _sqs
import aws_cdk.aws_lambda as _lambda
import aws_cdk.aws_lambda_event_sources as event_sources


class HelloCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        queue = _sqs.Queue(
                    self,
                    'HelloQueue'
        )

        my_lambda = _lambda.Function(
                        self,
                        'HelloFunction', 
                        runtime=_lambda.Runtime.PYTHON_3_7,
                        code=_lambda.Code.asset('lambda'),
                        handler='hello.handler'
        )

        my_lambda.add_event_source(event_sources.SqsEventSource(queue))

        # The code that defines your stack goes here
