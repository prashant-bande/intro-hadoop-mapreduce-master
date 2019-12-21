# Intro to Hadoop and MapReduce from Udacity

Set of scripts written in Python 2.7 for Udacity course [Intro to Hadoop and MapReduce](https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617).

These scripts can be used locally or in Hadoop by creating MapReduce jobs. To use locally, you can run the following command:

    cat example_data.csv | ./example_mapper.py | sort | ./example_reducer.py > results.txt

## Lesson 3:

### Part 1 - Sales Data
These scripts process data about sales data from different stores: `purchases.txt`

**q1 - Sales per Category:**
This mapreduce program gives a sales breakdown by product category across all of our stores. Results are output in two columns: (1) category and (2) total sales by category.

**q2 - Highest Sale:**
This mapreduce program finds the monetary value for the highest individual sale for each separate store. Results are output in two columns: (1) store and (2) highest sale.

**q3 - Total Sales:**
This mapreduce program finds the total sales value across all the stores and the total number of sales. Results are output in two rows: (1) total sales and (2) total number of sales.

### Part 2 - Web Log Data
These scripts process data about an web server log file: `access_log`.

**q1 - Hits to Page:**
This mapreduce program finds the number of hits for each different file on the website. Results are output in two columns: (1) file and (2) number of hits.

**q2 - Hits from IP:**
This mapreduce program determines the number of hits to the site made by each different IP address. Results are output in two columns: (1) IP and (2) number of hits.

**q3 - Most Popular:**
This mapreduce program finds the most popular file on the website. Results are output in one row with columns: (1) most popular file and (2) number of occurrences.

## Lesson 4:

## Project:

These scripts process data about users of and posts on Udacity's forums: `forum_node.tsv`. To test locally, you can use `student_test_posts.tsv`

**q1 - Student Times:**
This mapreduce program finds for each student what is the hour during which the student has posted the most posts.
Results are output in two columns: (1) user ID and (2) hour with the most posts.

**q2 - Post and Answer Length:**
This mapreduce program calculates the correlation between the length of a post and the length of answers.
Results are output in three columns: (1) question ID, (2) question length, and (3) average answers length.

**q3 - Top Tags:**
This mapreduce program finds the top tags used in posts. 
Results are output in two columns, sorted by popularity: (1) tag and (2) number of posts with the tag.

**q4 - Study Groups:**
This mapreduce program creates a list of the users who interacted via a question. 
Results are output in two columns: (1) question ID and (2) list of user IDs.
