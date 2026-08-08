# VPC & Networking

## Region

**AWS Region:** Mumbai (`ap-south-1`)

## VPC Design

The project uses a custom Amazon VPC with the CIDR block:

```text
10.0.0.0/16
```

The VPC is divided across two Availability Zones to provide a foundation for a highly available architecture.

## Availability Zones

* `ap-south-1a`
* `ap-south-1b`

## Subnet Design

| Subnet   | Availability Zone | CIDR           | Tier    | Purpose                   |
| -------- | ----------------- | -------------- | ------- | ------------------------- |
| Public-1 | `ap-south-1a`     | `10.0.1.0/24`  | Public  | Application Load Balancer |
| Public-2 | `ap-south-1b`     | `10.0.2.0/24`  | Public  | Application Load Balancer |
| App-1    | `ap-south-1a`     | `10.0.11.0/24` | Private | EC2 Application Server    |
| App-2    | `ap-south-1b`     | `10.0.12.0/24` | Private | EC2 Application Server    |
| DB-1     | `ap-south-1a`     | `10.0.21.0/24` | Private | RDS                       |
| DB-2     | `ap-south-1b`     | `10.0.22.0/24` | Private | RDS                       |

## Network Architecture

```text
                         VPC
                    10.0.0.0/16
                          |
          +---------------+---------------+
          |                               |
     ap-south-1a                     ap-south-1b
          |                               |
   +------+------+                 +------+------+
   |      |      |                 |      |      |
 Public  App     DB               Public  App    DB
 .1.0    .11.0   .21.0            .2.0    .12.0  .22.0
   |      |      |                 |      |      |
  ALB    EC2    RDS               ALB    EC2    RDS
```

## Design Rationale

### Why a custom VPC?

A custom VPC provides an isolated networking environment where routing, subnet placement, and network security can be controlled according to the application's requirements.

### Why two Availability Zones?

The application tier will be distributed across two Availability Zones to improve availability and reduce dependence on a single Availability Zone.

### Why public subnets?

Public subnets will be used for internet-facing components such as the Application Load Balancer.

### Why private application subnets?

Application servers should not be directly exposed to the public internet. They will receive application traffic through the load balancer.

### Why private database subnets?

The database should not be directly accessible from the internet. Database access will be restricted to the application tier through security groups.

## Internet Gateway

An Internet Gateway named `three-tier-igw` was created and
attached to the `three-tier-vpc`.

The Internet Gateway will provide internet connectivity for
resources in public subnets once the appropriate route table
is configured.

### Configuration

| Resource | Value |
|---|---|
| Internet Gateway | `three-tier-igw` |
| VPC | `three-tier-vpc` |
| Status | Attached |
| Region | `ap-south-1` |

## Route Tables

Three route tables were created to control traffic for the public, application, and database tiers.

### Public Route Table

The public route table is associated with both public subnets.

```text
Destination       Target
10.0.0.0/16       local
0.0.0.0/0         three-tier-igw

The default route sends internet-bound traffic from the public subnets to the Internet Gateway.

Private Application Route Table

The private application route table is associated with both application subnets.

Destination       Target
10.0.0.0/16       local
0.0.0.0/0         three-tier-nat-1a

The NAT Gateway provides outbound internet connectivity for resources in the private application subnets without directly exposing the application servers to inbound internet traffic.

Private Database Route Table

The private database route table is associated with both database subnets.

Destination       Target
10.0.0.0/16       local

No default internet route is configured for the database subnets. This keeps the database tier isolated from direct internet access.

NAT Gateway

A public NAT Gateway named three-tier-nat-1a was created in public-subnet-1a.

The NAT Gateway uses an Elastic IP and provides outbound internet connectivity for resources in the private application subnets.

Traffic flow:

Private EC2
     |
     v
Private App Route Table
     |
     v
NAT Gateway
     |
     v
Internet Gateway
     |
     v
Internet

For this project, one NAT Gateway is being used to control costs.

In a production environment, a NAT Gateway could be deployed in each Availability Zone to improve fault tolerance and eliminate the single-AZ dependency.

Subnet Associations
Public Route Table

Associated subnets:

public-subnet-1a
public-subnet-1b
Private Application Route Table

Associated subnets:

private-app-subnet-1a
private-app-subnet-1b
Private Database Route Table

Associated subnets:

private-db-subnet-1a
private-db-subnet-1b
Current Status
 VPC created
 Subnets created
 Internet Gateway configured
 Public route table configured
 Public subnet associations configured
 NAT Gateway configured
 Private application route table configured
 Private application subnet associations configured
 Private database route table configured
 Private database subnet associations configured
