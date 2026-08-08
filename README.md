# AWS Production-Style 3-Tier Application

> A production-style, highly available 3-tier web application architecture built on Amazon Web Services (AWS).

![Project Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

---

## 📌 Project Overview

This project demonstrates the design and deployment of a **highly available 3-tier web application architecture on AWS**.

The application is divided into three logical layers:

1. **Presentation / Load Balancing Tier**
2. **Application Tier**
3. **Database Tier**

The infrastructure is initially being deployed manually through the AWS Management Console to build a strong understanding of AWS networking, security, compute, database, storage, and monitoring concepts.

Infrastructure automation using **Terraform** and CI/CD using **GitHub Actions** will be implemented in later phases.

---

## 🏗️ Architecture

### Final Architecture

```text
                         INTERNET
                             |
                             v
                  Application Load Balancer
                             |
                  +----------+----------+
                  |                     |
                  v                     v
              EC2 - AZ1             EC2 - AZ2
           Private Subnet         Private Subnet
                  |                     |
                  +----------+----------+
                             |
                             v
                         Amazon RDS
                       Private Subnet
                             |
                             v
                          Amazon S3
```

> Architecture diagram will be added after the AWS infrastructure is designed and deployed.

---

## 🎯 Project Objectives

* Design a custom AWS VPC
* Create public and private subnets
* Deploy resources across multiple Availability Zones
* Configure Internet Gateway and NAT Gateway
* Configure route tables
* Implement secure Security Groups
* Deploy EC2 application servers
* Configure an Application Load Balancer
* Implement Amazon RDS
* Configure Amazon S3
* Implement EC2 Auto Scaling
* Configure CloudWatch monitoring
* Test high availability and fault tolerance
* Document deployment and troubleshooting
* Convert infrastructure to Terraform
* Implement CI/CD using GitHub Actions

---

## 🛠️ Technologies

### AWS Services

* Amazon VPC
* Amazon EC2
* Application Load Balancer
* EC2 Auto Scaling
* Amazon RDS
* Amazon S3
* AWS IAM
* Amazon CloudWatch

### Networking

* VPC
* Public Subnets
* Private Subnets
* Route Tables
* Internet Gateway
* NAT Gateway
* Security Groups

### DevOps

* Git
* GitHub
* Terraform *(planned)*
* GitHub Actions *(planned)*

---

## 🏛️ Architecture Components

| Component                 | Purpose                                                  |
| ------------------------- | -------------------------------------------------------- |
| VPC                       | Provides isolated AWS networking                         |
| Public Subnets            | Host internet-facing resources                           |
| Private App Subnets       | Host application servers                                 |
| Private DB Subnets        | Isolate the database                                     |
| Internet Gateway          | Provides internet connectivity for public resources      |
| NAT Gateway               | Allows private resources to access the internet securely |
| Application Load Balancer | Distributes incoming application traffic                 |
| EC2                       | Runs the application                                     |
| Auto Scaling              | Maintains application availability and scalability       |
| RDS                       | Provides managed relational database services            |
| S3                        | Provides object storage                                  |
| IAM                       | Controls AWS access and permissions                      |
| CloudWatch                | Provides monitoring and logging                          |

---

## 🔐 Security Design

The architecture follows a layered security approach.

### Network Isolation

* Public and private subnets are separated.
* Application servers are placed in private subnets.
* The database is placed in private database subnets.

### Traffic Flow

```text
Internet
   |
   v
ALB
   |
   v
EC2
   |
   v
RDS
```

Only required traffic will be allowed between the layers using Security Groups.

### Credentials

No AWS credentials, private keys, passwords, or sensitive information will be committed to this repository.

---

## 📚 Project Documentation

Detailed documentation is maintained in the `docs/` directory.

| Documentation                                           | Description                        |
| ------------------------------------------------------- | ---------------------------------- |
| [Project Overview](docs/01-project-overview.md)         | Project goals and architecture     |
| [VPC & Networking](docs/02-vpc-networking.md)           | VPC, subnets, routing and gateways |
| [Security Groups](docs/03-security-groups.md)           | Network security configuration     |
| [EC2 Application Tier](docs/04-ec2-application-tier.md) | EC2 deployment                     |
| [Load Balancer](docs/05-load-balancer.md)               | ALB configuration                  |
| [RDS Database](docs/06-rds-database.md)                 | Database deployment                |
| [S3 Storage](docs/07-s3-storage.md)                     | Object storage                     |
| [Auto Scaling](docs/08-auto-scaling.md)                 | Scalability and availability       |
| [CloudWatch](docs/09-cloudwatch-monitoring.md)          | Monitoring and logging             |
| [Testing](docs/10-testing.md)                           | Architecture testing               |
| [Troubleshooting](docs/11-troubleshooting.md)           | Problems and solutions             |

---

## 📸 Screenshots

Implementation screenshots are organized by AWS component in the `screenshots/` directory.

```text
screenshots/
├── 01-vpc/
├── 02-security/
├── 03-ec2/
├── 04-alb/
├── 05-rds/
├── 06-s3/
├── 07-autoscaling/
└── 08-cloudwatch/
```

---

## 🚀 Implementation Roadmap

### Phase 1 — Manual AWS Deployment

* [ ] VPC
* [ ] Subnets
* [ ] Internet Gateway
* [ ] Route Tables
* [ ] NAT Gateway
* [ ] Security Groups
* [ ] EC2
* [ ] Application Load Balancer
* [ ] RDS
* [ ] S3
* [ ] Auto Scaling
* [ ] CloudWatch

### Phase 2 — Testing

* [ ] Application connectivity
* [ ] Load balancer testing
* [ ] Database connectivity
* [ ] Auto Scaling testing
* [ ] Failure testing
* [ ] Security verification

### Phase 3 — Infrastructure as Code

* [ ] Terraform project structure
* [ ] Terraform VPC
* [ ] Terraform EC2
* [ ] Terraform ALB
* [ ] Terraform RDS
* [ ] Terraform Auto Scaling
* [ ] Terraform outputs and variables

### Phase 4 — CI/CD

* [ ] GitHub Actions workflow
* [ ] Application build
* [ ] Automated deployment
* [ ] Deployment verification

---

## 🧠 Key Learning Outcomes

Through this project, I am developing practical knowledge of:

* AWS networking
* VPC architecture
* Public vs private subnets
* Routing
* Load balancing
* EC2 deployment
* Auto Scaling
* Database architecture
* AWS security
* Monitoring
* Infrastructure as Code
* CI/CD

---

## 🛠️ Challenges & Troubleshooting

All significant deployment issues, investigation steps, root causes, and solutions will be documented in:

`docs/11-troubleshooting.md`

---

## 🔮 Future Improvements

Potential future improvements include:

* Infrastructure automation using Terraform
* CI/CD using GitHub Actions
* HTTPS using ACM
* Route 53 DNS configuration
* Containerization using Docker
* Kubernetes deployment using Amazon EKS
* Advanced monitoring and observability

---

## 👨‍💻 Author

**Dev Dwivedi**

Cloud & DevOps Engineer

