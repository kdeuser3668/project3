# project3

Project: Stock Data Visualization

Project Objectives

To develop a working software application
To further gain experience and develop skill managing an agile project in Jira.
To further develop team organization and communication skill.
Description

In this project your scrum team will create a software application in python to visualize stock data trends. You have three (3) weeks to complete this project.

Purpose

The purpose of this project is to gain experience producing a working software application using agile project management

Scenario

A professor in your department is interested in tracking stock data trends and recently found the Alpha VantageLinks to an external site. website. This site offers an api that returns historical stock data from the past 20 years. The data is returned in json and other formats. There is no way to visualize the data or choose a date range to view the data. The api, by default, returns 20 years of data for all but one of its functions.

Your team’s job is to create a python application that queries the Alpha Vantage api, and allows the user to select a date range to view the data, and the type of chart they want to view the data in. Your team should use git and GitHub as a means of version control for the project.

The application should:

Ask the user to enter the stock symbol for the company they want data for.
Ask the user for the chart type they would like.
Ask the user for the time series function they want the api to use.
Ask the user for the beginning date in YYYY-MM-DD format.
Ask the user for the end date in YYYY-MM-DD format.
The end date should not be before the begin date
Generate a graph and open in the user’s default browser.
