#dictionary

ec2_info = [
    {
        "id": "instance-01",
        "type": "t2.micro"
    },
    {
        "id": "instance-02",
        "type": "t2.medium"
    },
    {
        "id": "instance-03",
        "type": "t2.lxlarge"
    }
]

print("Type of: ", type(ec2_info))
print("ec2_info ", ec2_info)

print("Accessing particular element: ",ec2_info[1]["type"])
 