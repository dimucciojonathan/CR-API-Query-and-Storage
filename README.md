# CR-API-Query-and-Storage

Before running any analytics, it's important to get the data from somewhere. Many platforms such as video game publishers have extensive API's from which anyone can access their data. One limitation to an API is that there is usually not always a long history of data stored in the API.

Clash Royale is a competitve mobile game that combines aspects from genres such as tower defense and collectible card games. The API hold an extensive range of data from game logs to profile information. The issue is that a players info can only be retrieved at real time, and game logs only hold up to 14 previous matches.

To solve this problem, I set out to automate the process of gathering and storing data from the API. My program is currently running on Amazon Web Services through a Lambda function. It automatically takes data from the API and stores it to a database that is hosted through AWS on a Relational Database Service.

My goal for this writeup is to document my process of start to finish. Before this, I have never queried an API or set up a database, but I have spent time learning the SQL language. I'll give a walkthrough of: the steps I took, roadblocks I faced, and resources that helped me overcome them.

1. Query the Clash Royale API

The first thing I wanted to do is simply query the API and print out the data I want in string format. This API requires a authentication key that has a whitelisted IP connected to it. This doesn’t present any problems now, but AWS Lambda functions have a different IP for each instance by default. Later on I will explain how I got my lambda function to have a single, static IP address.

    https://www.youtube.com/watch?v=pxofwuWTs7c&t=185s
    https://www.youtube.com/watch?v=3RAtqgVQ1rU&t=324s

2.  Insert the data into a local database

Still on my local machine, I figured the next logical step was to learn a bit about databases. SQLite was very easy to install since it’s just an import, and I went with that. Here I got down the basics of connections, tables, and executing statements.

https://www.youtube.com/watch?v=pd-0G0MigUA&t=1110s

3. Figure out how to automate this process

Now that I can query the API and store it in the most simple way possible, I decided it was time to automate the process. At first, I didn’t consider cloud services. My first idea was just to use a scheduler on my local machine and go from there. Once I discovered AWS I decided it’d be a great learning experience.

4. Run a ‘Hello World’ AWS Lambda function, then repeat step 1 with AWS

For some uses, porting your code to AWS is as simple as a copy and paste. But here, I spent a decent amount of time getting my function’s IP address to stay the same. Turns out I had to learn a bit about how networks interact with each other to complete this task.

https://www.youtube.com/watch?v=-8L4OxotXlE&t=1227s

5. Connect an elastic IP to my AWS Lambda function

Lambda does not inherently have the functionality to insert an elastic IP. The workaround is to route your function through a Virtual Private Cloud (VPC) that is connected to an NAT Gateway, which has an elastic IP. The steps are:

a.	Create a VPC through AWS
b.	Create an NAT Gateway and an Internet Gateway
c.	Create two private subnets and one public subnet.
d.	Connect the two private subnets to the NAT Gateway.
e.	Connect the public subnet to both the VPC and the Internet Gateway.
f.	Ensure that all subnets are linked to the original VPC. The VPC now has an internet connection and an elastic IP.
g.	After creating the lambda function, scroll down to ‘Network’ and choose the VPC and Subnets that were just created.

https://aws.amazon.com/premiumsupport/knowledge-center/internet-access-lambda-function/

5. Install MYSQL and MYSQL Workbench on my system

This part took me longer than it should have. There was an issue where I had uninstalled and reinstalled MYSQL, and the installer no longer gave me the master password. The solution was to fully delete MYSQL through the terminal then reinstall.

https://gist.github.com/vitorbritto/0555879fe4414d18569d
https://www.youtube.com/watch?v=UcpHkYfWarM&list=LLoNcHvIIiw-5gCSrQpDAmKg&index=5&t=774s

6. Set up a MYSQL database using the RDS feature of AWS

This step is straightforward thanks to Amazon’s interface. I made sure to set the database to publicly available so that I can connect from my local system for testing purposes.

7. Connect to the MYSQL RDS then create schemas and tables

This was my first time setting up a database, so I went with MYSQL Workbench for simplicity. After each call, I looked over the SQL code to make sure I would be able to do this step from the terminal if needed. MYSQL Workbench is also using for getting a UI on a database where I can view tables and such from a high level.

https://www.youtube.com/watch?v=HoZL7oyR-wo&t=2s

Up to this point, I can query the clash royale API through my lambda function, and I have access to my database from my local machine. The last step is to just create some insert statements within my lambda function and run the function on an automatic schedule.

8. Deployment Packages in Lambda

AWS Lambda does not automatically come with every import. For example, lambda does not have requests or pymysql, and I needed both. The workaround here is to first install the packages into the application folder. Next, I zipped up the .py file with the packages I needed and uploaded to my lambda function. Zipping up all the files that are necessary and uploading is known as a deployment package.

https://www.youtube.com/watch?v=rDbxCeTzw_k&t=594s

9. Insert to database from Lambda

Finally, we can put the pieces together. Every lambda function has to be pointed to a specific python file and function with parameters (event, context). My program has the same inputs every time, so I have my (event,context) set to None. After lambda enters this first function, I point it to my ‘save_events’ function which gathers the data and inserts it into the database.

https://www.youtube.com/watch?v=-CoL5oN1RzQ&t=268s

10. Run the Lambda function on automatic intervals

This function can be ran automatically through cron expressions. I navigated over to the CloudWatch dashboard, then created a new rule. I can set my event to run at a fixed rate of any time I want, and I chose my lambda function as the target.

https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Scheduled-Rule.html

11. Conclusion

Now I can confidently go to sleep and let my Lambda function continue to collect data on any player or clan I want in Clash Royale. I learned a lot through this project, and hope to use the skills learned as a springboard into more endeavors in the future. 
