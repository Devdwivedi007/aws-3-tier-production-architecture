# Application

Flask-based application for the AWS 3-Tier Production Architecture project.

The application connects to an Amazon RDS MySQL database through private networking.

## Architecture

```text
Application Load Balancer
          |
          v
Private EC2 Application Servers
          |
          v
Private RDS MySQL