output "dynamodb_table_arn" {
  value       = module.dynamodb_table.arn
  description = "ARN of the DynamoDB table"
}

output "add_user_lambda_arn" {
  value       = module.lambda_add.arn
  description = "ARN of the Add User Lambda function"
}

output "retrieve_user_lambda_arn" {
  value       = module.lambda_retrieve.arn
  description = "ARN of the Retrieve User Lambda function"
}

output "api_gateway_invoke_url" {
  value       = module.api_gateway.invoke_url
  description = "Invoke URL of the API Gateway"
}
