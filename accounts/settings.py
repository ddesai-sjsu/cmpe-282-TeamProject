import sys
import os

# AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", None)
# AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", None)
# AWS_REGION = os.getenv("AWS_REGION", None)
# COGNITO_USER_POOL_ID = os.getenv("COGNITO_USER_POOL_ID", None)
# COGNITO_APP_CLIENT_ID = os.getenv("COGNITO_APP_CLIENT_ID", None)
# S3_BUCKET = os.getenv("S3_BUCKET", None)
# S3_URL = os.getenv("S3_BUCKET", None)
# CLOUD_FRONT_URL = os.getenv("CLOUD_FRONT_URL", None)

AWS_ACCESS_KEY_ID='AKIAT4M2Z3IG3XN3BAVP'
AWS_SECRET_ACCESS_KEY='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'
AWS_REGION="us-east-1"
COGNITO_USER_POOL_ID="us-east-1_H8LF61zTj"
COGNITO_APP_CLIENT_ID="37a456ds565vfclm5d8sgs8aep"
S3_BUCKET="profileimagemyskills"
S3_URL="s3://profileimagemyskills/"

# HOST_NAME = os.getenv("HOST_NAME", "localhost")
# HOST_PORT = os.getenv("HOST_PORT", "8000")
# HOST_PROTOCOL = os.getenv("HOST_PROTOCOL", "http")

TABLE_NAME = "Users"
VALID_USER_TYPES = ["consumer", "provider"]
VALID_SKILL_TYPES = ["driver", "electrician", "plumber", \
    "carpenter", "house maid", "baby sitter", \
    "elder care", "cook", "nanny", "beautician", \
    "painter", "delivery boy", "gardener",  \
    "cleaner", "pest control", "decorators"]


if AWS_ACCESS_KEY_ID is None:
    print("Please set AWS_ACCESS_KEY_ID !!!")
    sys.exit(1)
elif AWS_SECRET_ACCESS_KEY is None:
    print("Please set AWS_SECRET_ACCESS_KEY !!!")
    sys.exit(1)
elif AWS_REGION is None:
    print("Please set AWS_REGION !!!")
    sys.exit(1)
elif COGNITO_USER_POOL_ID is None:
    print("Please set COGNITO_USER_POOL_ID !!!")
    sys.exit(1)
elif COGNITO_APP_CLIENT_ID is None:
    print("Please set COGNITO_APP_CLIENT_ID !!!")
    sys.exit(1)
elif S3_BUCKET is None:
    print("Please set S3_BUCKET !!!")
    sys.exit(1)
elif S3_URL is None:
    print("Please set S3_URL !!!")
    sys.exit(1)
# elif CLOUD_FRONT_URL is None:
#     print("Please set CLOUD_FRONT_URL !!!")
#     sys.exit(1)
