# AWS Lambda Packaging Examples

These examples are Cloudformation demonstrations on how to package and deploy lambda functions.

## How To Deploy

1. Package dependencies & source code locally

   ```
   pip install -r requirements.txt --target ./package
   cp -r example package/
   ```

2. Package cloudformation template into an S3 bucket

   ```
   aws cloudformation package --s3-bucket <BUCKET_NAME> --template-file unpackaged_template.yaml --output-template-file packaged_template.yaml
   ```

   Note that `LambdaRole` does __not__ need access to the intermediate Bucket, but whomever is running the command _will_!

3. Use `packaged_template.yaml` to deploy!

   (The required command is also outputted by the previous step)

   ```
   aws cloudformation deploy --stack-name <STACK_NAME> --template-file packaged_template.yaml --capabilities CAPABILITY_IAM
   ```
