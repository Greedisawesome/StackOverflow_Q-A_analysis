# elevation_final_project
Final project of Data Analyst Evelation Academy course
The StackOverflow dataset is publicly available on Google BigQuery public datasets. It is tens of GB in size,
so we’ve exported a subset of the data into our SQL server. The schema is comprised of:
Posts Table - All the posts since Jan. 1st, 2018.
Answers Table - All answers to the posts in the posts table.
Users Table - All users that created the answers and posts, or joined after Jan. 1st, 2018.
The purpose of this project is to give basic analysis to provide data and find some basic trends about users behavior.
We used SQL queries to have a better understanding of data
Some of main conclusions:
- There is a distinct trend is user activity - significant decrease in December due to holidays and increase in February, which could be explained by "New Year Resolutions" to start learn programming in next year
- Users activity tend to decreaase with the time goes by. Majority of posts and answers are created on first month after registration and then users start to produce less content
- Python, Java and JavaScript are main topics of discussion on StackOverflow
