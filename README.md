# farapp_public_api_challenge

**Steps to running the project:**
Step 1) cd farapp_public_api_challenge/ directory.
Step 2) docker-compose build
Step 3) docker-compose up
Step 4) Open browser to localhost:5000/ or localhost:5000/namesearch





I did not have enough time to compelte this project. These are the rest of the
steps that I need to take in order to compelte the rest of the project:
    1) Setup index and name search endpoint with HTMl pages and routing.
    2) Setup database schema and flask models for Names(first, last, middle)
    3) Setup 1000 name data from randomuser.me.
    4) Apply search feature for first, last, middle, and full names.
        - This will just be comparing substrings and querying the database
          for the proper names within the input box/form item, etc.
    5) Add pagination using CSS bootstrap libraries to display per every 100
       names on a web page.
        - This can be done using pagination and flask MVVC model with for loops in the DOM.
    6) Expand model/schema to include Email, Phone number and convert
       databse entries from Names into Contacts since this would not turn into
       more than just a names api.
    7) Add download button for a .csv format representation of the table by using an a tag with the download attribute.a
