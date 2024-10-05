## Job Scraper
Job scraper, used to determine in-demand skills for software engineers.

## Tech used
* [Selenium](https://www.selenium.dev/) - Scraping a JavaScript-heavy website
* [SQLAlchemy](https://www.sqlalchemy.org/) - Object Relational Mapper
* [Alembic](https://alembic.sqlalchemy.org/en/latest/) - Migrations
* [SQLite](https://www.sqlite.org/) - Storing scraped jobs
* [PySpark](https://spark.apache.org/docs/latest/api/python/index.html) - Token analysis

## Insights

Python, Java, and JavaScript are the most popular languages among job postings in the "IT - Software" category on ClearanceJobs, which comes as no surprise. However, it is surprising to see that Angular is considerably more popular than React (14% Angular vs. 9% React), especially since, in the broader software engineering industry, React is nearly twice as popular as Angular (according to the [2024 Stack Overflow Developer Survey](https://survey.stackoverflow.co/2024/technology#most-popular-technologies-webframe-prof)).

The data was scraped in October 2024. It is important to note that tokens were limited to words containing only letters, meaning that technologies like .NET (~3%), C++ (~11%), and C# (~5%) are not displayed in the rankings. Despite C# and Java being comparable in demand across the wider industry, ClearanceJobs leans heavily toward Java. AWS significantly outpaces Azure in popularity (25% vs. 12%). On the database side, RDS (7.5%) and Oracle (7%) are neck-and-neck, but both surpass Postgres (4%) — although it is likely that a significant portion of RDS databases are actually running Postgres.

In summary, if you're looking to find a job on ClearanceJobs, having experience with Java, Python, Javascript, and AWS is important. On the frontend, Angular is the framework of choice, while on the backend, RDS (probably with Postgres) or Oracle are your best bets.

![Unigrams](./unigrams.png)

### Top Tokens (Percentage of Job Postings where Token is Mentioned) out of 2,652 scraped jobs:

python - 37.78%<br>
java - 36.69%<br>
infrastructure - 28.58%<br>
javascript - 26.21%<br>
linux - 25.94%<br>
aws - 25.83%<br>
scripting - 21.49%<br>
devops - 20.59%<br>
analytics - 19.65%<br>
database - 19.49%<br>
jenkins - 17.01%<br>
git - 16.48%<br>
docker - 14.56%<br>
sql - 13.84%<br>
angular - 13.69%<br>
c - 13.08%<br>
azure - 11.92%<br>
bash - 11.65%<br>
kubernetes - 11.39%<br>
spring - 11.31%<br>
css - 11.16%<br>
rest - 11.12%<br>
html - 10.94%<br>
google - 10.67%<br>
cots - 10.41%<br>
unix - 9.95%<br>
scripts - 9.73%<br>
elasticsearch - 9.24%<br>
ansible - 8.97%<br>
react - 8.79%<br>
cybersecurity - 8.22%<br>
apis - 8.18%<br>
gots - 8.11%<br>
gitlab - 7.99%<br>
protocols - 7.62%<br>
github - 7.50%<br>
rds - 7.50%<br>
excel - 7.39%<br>
junit - 7.20%<br>
virtualization - 7.16%<br>
servers - 7.05%<br>
oracle - 6.98%<br>
springboot - 6.83%<br>
cisco - 6.41%<br>
relational - 6.37%<br>
api - 6.33%<br>
modeling - 6.30%<br>
nosql - 6.11%<br>
distributed - 6.11%<br>
ui - 6.07%<br>
restful - 6.07%<br>
pipelines - 6.00%<br>
mysql - 6.00%<br>
json - 5.92%<br>
nifi - 5.92%<br>
apache - 5.81%<br>
ms - 5.69%<br>
perl - 5.51%<br>
powershell - 5.17%<br>
elastic - 5.09%<br>
xml - 5.09%<br>
containerization - 5.02%<br>
mongodb - 4.86%<br>
efs - 4.68%<br>
katalon - 4.64%<br>
backend - 4.64%<br>
shell - 4.60%<br>
embedded - 4.56%<br>
terraform - 4.45%<br>
postgresql - 4.19%<br>
puppet - 4.19%<br>
std - 4.19%<br>
phantom - 4.19%<br>
maven - 4.11%<br>
microservices - 4.00%<br>
r - 4.00%<br>
servicenow - 3.96%<br>
cno - 3.92%<br>
ruby - 3.88%<br>
tomcat - 3.88%<br>
postgres - 3.77%<br>
devsecops - 3.70%<br>
splunk - 3.66%<br>
eclipse - 3.62%<br>
dodaf - 3.58%<br>
hadoop - 3.54%<br>
pipeline - 3.36%<br>
typescript - 3.36%<br>
lambda - 3.32%<br>
visualization - 3.24%<br>
rf - 3.09%<br>
kafka - 3.09%<br>
firewalls - 3.02%<br>
etl - 3.02%<br>
vmware - 3.02%<br>
pig - 2.98%<br>
vue - 2.90%<br>
assembly - 2.90%<br>
nodejs - 2.64%<br>
cryptography - 2.56%<br>
cloudformation - 2.49%<br>
sharepoint - 2.45%<br>
go - 2.38%<br>
kibana - 2.34%<br>
jquery - 2.22%<br>
spark - 2.19%<br>
elk - 2.11%<br>
hive - 2.11%<br>
bootstrap - 2.07%<br>
hashing - 2.07%<br>
ip - 2.04%<br>
mbse - 2.00%<br>
mongo - 2.00%<br>
frontend - 1.96%<br>
iac - 1.96%<br>
dynamodb - 1.96%<br>
cli - 1.92%<br>
dns - 1.89%<br>
chef - 1.81%<br>
grafana - 1.81%<br>
selenium - 1.81%<br>
geospatial - 1.77%<br>
js - 1.77%<br>
swift - 1.77%<br>
php - 1.70%<br>
dashboards - 1.62%<br>
hdfs - 1.62%<br>
san - 1.58%<br>
sqs - 1.58%<br>
android - 1.55%<br>
centos - 1.55%<br>
solr - 1.55%<br>
visualizations - 1.55%<br>
helm - 1.55%<br>
node - 1.51%<br>
sysml - 1.51%<br>
ghidra - 1.51%<br>