# AWS Serverless Assignment

## Overview

In this assignment, I worked on automating different AWS operations using AWS Lambda and Python (Boto3).
The goal was to understand how serverless architecture can be used to manage cloud resources efficiently.

I have completed 4 tasks covering EC2, S3, and EBS services.

---

## Assignment 1: EC2 Start/Stop Automation

### What I did

* Created two EC2 instances
* Added tags:

  * One with `Auto-Stop`
  * One with `Auto-Start`
* Wrote a Lambda function to check tags and start/stop instances accordingly

### Result

* Instance with `Auto-Stop` tag was stopped
* Instance with `Auto-Start` tag was started successfully

### Screenshots

<img width="2253" height="860" alt="image" src="https://github.com/user-attachments/assets/fe96a48e-37dd-44f5-b64a-b7c47fe52d7a" />


<img width="2399" height="348" alt="image" src="https://github.com/user-attachments/assets/eb3eeff4-4737-4b01-a445-5f631b46699b" />

---

## Assignment 2: S3 Bucket Cleanup

### What I did

* Created an S3 bucket and uploaded some test files
* Wrote a Lambda function to delete files older than a certain time
* For testing, I used minutes instead of days

### Result

* Old files were deleted automatically after running the Lambda

### Screenshots

* S3 bucket before cleanup →

<img width="2015" height="746" alt="image" src="https://github.com/user-attachments/assets/f8174110-dff8-41a5-b4aa-c400bcd62685" />

* Lambda logs showing deleted files →

<img width="2378" height="915" alt="image" src="https://github.com/user-attachments/assets/55c43f0f-e95f-44e6-89a8-8adfb478604a" />

  
* S3 bucket after cleanup → *(add screenshot here)*

<img width="1917" height="558" alt="image" src="https://github.com/user-attachments/assets/ec349500-55cb-4d77-aa88-7ea51435a8b3" />


## Assignment 3: EBS Snapshot Automation

### What I did

* Selected an existing EBS volume
* Created a Lambda function to take snapshots

### Result

* Snapshot was created successfully and visible in EC2 console

### Screenshots

* EBS volume → 

<img width="1660" height="259" alt="image" src="https://github.com/user-attachments/assets/d8a7e1f2-1622-4ec0-9895-ac14c37a3e74" />

* Lambda logs → 

<img width="2399" height="1038" alt="image" src="https://github.com/user-attachments/assets/eb850cf6-9175-4fff-92f8-347d92472c7b" />


* Snapshot created → 

<img width="2094" height="275" alt="image" src="https://github.com/user-attachments/assets/8da3b783-b4fa-41ab-809f-77eee3c57efb" />


---

## Assignment 4: Auto Tag EC2 (Event-Based)

### What I did

* Created a Lambda function to tag EC2 instances
* Configured EventBridge rule to trigger Lambda when instance state becomes "running"
* Launched a new EC2 instance to test

### Result

* EC2 instance was automatically tagged with:

  * `CreatedOn`
  * `Owner`

### Screenshots

* EventBridge rule → 

<img width="2390" height="800" alt="image" src="https://github.com/user-attachments/assets/250b8487-c4e2-4b0f-b77d-6540bab4cc82" />


* EC2 instance launch and tag → 

<img width="2396" height="889" alt="image" src="https://github.com/user-attachments/assets/40ebedfe-23aa-4757-a4c0-69277d79608c" />


* Lambda logs → 

<img width="2399" height="903" alt="image" src="https://github.com/user-attachments/assets/e22bd001-62dc-4583-8218-1b21e947407a" />


---

## Challenges Faced

* Faced IAM permission issues initially
* CloudWatch logs were not working due to missing permissions
* S3 encryption behavior was different due to AWS default settings

---

## Learnings

* Learned how to use AWS Lambda with Boto3
* Understood event-driven architecture using EventBridge
* Got hands-on experience with EC2, S3, and EBS automation
* Learned importance of IAM roles and permissions

---

## Conclusion

This assignment helped me understand how serverless architecture works in real scenarios.
I was able to automate multiple AWS tasks using Lambda and gained practical experience with cloud automation.


