This is a test automation framework based on Python, Selenium, and pytest.

This framework follows the Page Object Model (POM).

Coming to the directory structure, the framework has been built in the below fashion:

1. PageObjects directory

    - The web elements and its associated functions has been spilt into different files according to the webpage.
      But in this instance there is only on file as, I have crammed everything into one for ease access and time constrains.

2. TestData directory

    - It houses the necessary test data, embedded within a class. When the data is required the class variables are accessed directly.

3. Tests directory

    - This directory has all the test cases, relating to sign up, sign in and sign out. A simple description of the tests has been mentioned within the files as comments.

4. Utilities

    - It includes the BaseClass that is inherited by the necessary classes that wants access to the logger functionalities

5. conftest.py

    - This file has the necessary pytest configurations, including the pytest fixtures.

6. Logs folder

    - Includes the log file that is created during test runs.
