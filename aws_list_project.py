"""
Your module description
"""
#project using aws service inventory

# 1 - create an empty list.
aws_list = []

# 2 - Populating the list using append.
aws_list.append("EC2")
aws_list.append("Lambda")
aws_list.append("Fargate")
aws_list.append("ECS")
aws_list.append("EKS")
aws_list.append("Cloud9")
aws_list.append("CloudFront")
aws_list.append("DynamoDB")
aws_list.append("Elastic Beanstalk")
aws_list.append("Kinesis")

# 3 - Printing the list & the length of the list.
print(aws_list)
print(len(aws_list))

# 4 - Removing two specific services from the list by name
aws_list.remove("Lambda")
aws_list.remove("CloudFront")

# 5 - Printing the list & the length of the list.
print(aws_list)
print(len(aws_list))
