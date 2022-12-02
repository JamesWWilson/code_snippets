# README Best Practices (Always use H1, or a single hash, here for title)
***Author Name***<br>
***Author Title***<br>
***Author's Team**<br>
***Date (so that folks know how old the documentation is)***

# IMPORTANT NOTE (Use H1 or H2 for this to be sure folks see it)
If there are any super important notes about your repo, put it clearly at the top. Often engineers don't read a whole README file until they hit a problem...though you should always read the README first!

### Description [or Definition] (Use H3 for the sub headings from here on)
In as few words as possible define this repository's product and purpose

### Architecture
In the case of a deployed model, or a model pipeline, using lucidchart or another drawing software is highly recommended to communicate the big picture to the rest of the team and to non-technical stake holders.

### Installation
If you create a `pip install` functionality for your software package or model package, tell folks how to install it.

### Usage

1. Step one on how to use this package
    1. This might be `pip install -r requirements.txt`
    1. This might be the execution step:

    `python execution/main.py arg1 arg2 arg3`

1. Step two if there are multiple steps to be aware of
1. If there is a data output step, manual or automated, describe it here

### Outputs
Your model should have outputs. Define here where those get sent and what, if any, action is expected to be taken with them

  
### REST API / GraphQL API
You should describe if your model or this package contains an API that can be consumed by a front-end application or by the internet. 

1. Does your API require authentication keys?
1. Does your API have an API Gateway between it and the internet?
1. What happens if the input is not acceptible
    1. Are there error messages / warnings returned as a response JSON payload?


### Compatibility
This is where you define and describe your docker image. There may or may not be notes that matter to folks. Assume that nobody uses your code for 18 months and has to figure out what versions of everything were in use right now beyond the requirements file.

This is also a spot where you can display your `requirements.txt` file, especially if you want to clarify for users if there are different files on different operating systems, or in different virtual environments.
