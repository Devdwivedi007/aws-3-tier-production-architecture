# Security Groups

## Overview

The architecture uses separate Security Groups for the Application Load Balancer, EC2 application servers, and RDS database.

Traffic is restricted between tiers using Security Group references instead of allowing unrestricted access.

## Security Group Architecture

```text
Internet
   |
   | HTTP :80
   v
ALB
   |
   | HTTP :80
   v
EC2 Application Servers
   |
   | MySQL :3306
   v
RDS Database
ALB Security Group
Security Group

alb-sg

Purpose

Controls inbound traffic to the Application Load Balancer.

Inbound Rules
Protocol	Port	Source	Purpose
TCP	80	0.0.0.0/0	Allow HTTP traffic from the internet
Outbound Rules

The default outbound rule is currently enabled:

All traffic → 0.0.0.0/0
Application Security Group
Security Group

app-sg

Purpose

Controls access to the EC2 application servers located in the private application subnets.

Inbound Rules
Protocol	Port	Source	Purpose
TCP	80	alb-sg	Allow HTTP traffic only from the ALB

The EC2 instances are not directly exposed to the internet.

Traffic must first pass through the Application Load Balancer.

Outbound Rules

The default outbound rule is currently enabled:

All traffic → 0.0.0.0/0

Outbound internet traffic from the private application subnets is routed through the NAT Gateway.

Database Security Group
Security Group

db-sg

Purpose

Controls access to the RDS database.

Inbound Rules
Protocol	Port	Source	Purpose
TCP	3306	app-sg	Allow MySQL traffic only from application servers

The database does not allow direct internet access.

Outbound Rules

The default outbound rule is currently enabled.

Security Model

The project follows a layered security model:

Internet
    |
    v
  ALB
 alb-sg
    |
    | HTTP :80
    v
  EC2
 app-sg
    |
    | MySQL :3306
    v
  RDS
 db-sg

Each layer only accepts the traffic required from the previous layer.

Security Group References

Instead of allowing the entire internet to access EC2 and RDS, Security Group references are used.

alb-sg → app-sg → db-sg

This provides a more restrictive and maintainable security model.

Security Checklist
 ALB Security Group created
 Application Security Group created
 Database Security Group created
 ALB allows HTTP from the internet
 EC2 allows HTTP only from ALB Security Group
 RDS allows MySQL only from Application Security Group
 RDS is not exposed to the internet
Future Security Improvements

The following improvements can be added in later phases:

HTTPS using AWS Certificate Manager
Redirect HTTP to HTTPS
More restrictive outbound rules
AWS WAF
IAM least-privilege policies
Secrets Manager for database credentials
CloudTrail auditing