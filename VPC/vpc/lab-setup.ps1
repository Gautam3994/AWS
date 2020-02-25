# Lab-Setup.ps1

#Replace the values below and save this file as credentials.ps1
$AWSAccessKey="AKIAJ2HCVRW3WZ6SEGHQ" # Replace with your access key
$AWSSecretKey="9s5kkQ89QibR5k0aHS62wltJhCL1ldnkidnDjms+" # Replace with your secret key

# Set AWS credentials and region
$AWSProfileName="aws-networking-deep-dive-vpc"
$AWSRegion = "us-east-2"

# Set AWS credentials and store them
Set-AWSCredential -AccessKey $AWSAccessKey -SecretKey $AWSSecretKey -StoreAs $AWSProfileName

# Load the credentials for this session
Set-AWSCredential -ProfileName $AWSProfileName

# Set the default region
Set-DefaultAWSRegion -Region $AWSRegion
Get-DefaultAWSRegion

# Test functionality
if ((Get-EC2Vpc).count -ge 1) { Write-Host Connectivity to AWS established!} 