import json 
	
# Define student_details dictionary
student_details ={ 
	"name" : "sathiyajith", 
	"rollno" : 56, 
	"cgpa" : 8.6, 
	"phonenumber" : "9976770500"
} 
	
# Convert and write JSON object to file
with open("sample.json", "w") as outfile: 
	json.dump(student_details, outfile)
