Project: CRUD web application

Objectives: Test the functionality of adding nodes to blockchains and creating private blockchains

Features to test:

1. User Sign-up
2. User Sign-in
3. Onboard OCN Node
4. Launch OCN Child Network
5. User Signout

Test Cases:

1. User Sign-up

    - Valid Sign-Up
      The user enters all the required fields with valid values and click on the 'SIGN UP' button.
      Expected result: The user must go to the landing page of the application.
    - Sign up using valid email IDs
      When the user signs up using valid email ID of the following format: user+tag@example.com, simple@example.com, john.doe@example.com, user123@example.co.uk, user-name@example.io, user_name@example.org, u@example.com
      Expected result: The email field should not be marked with a red outline.
    - Entering the password that satisfies the mentioned criteria
      When the user enters the following values after the 'Password' field: Sunny4#TreeFox, Rain8!CupMoooooo000o000oon, Book@9FastDog, Wind2$CatJet, Fish!7RockSky
      Expected result: The password field should not be marked with a red outline.
    - Entering the right password in the 'Confirm Password' field.
      When the user enters the same password mentioned within the 'Confirm Password' as the one mentioned within the 'Password' field.
      Expected result: The 'Confirm Password' field must not be marked with a red outline.
    - Sign-up with an existing account
      The user tries to sign-up with an already existing email ID.
      Expected result: The user must be shown the message: 'Provided E-Mail is already in use'.
    - User tries to sign-up using invalid email ids
      When the user tries to sign-up using invalid email id of the following format: paul.example.com, @example.com, abc@.com, paul@example,!paul@example.com
      Expected result: The email field should show the red outline and the 'SIGN UP' button should be greyed out even after fill the remaining required fields with valid values.
    - Entering the password that does not satisfy the criteria
      When the user enters the following values after the 'Password' field: 123, 12345678, 1234567!, 12345ab!, 12345abbbbbb!
      Expected result: The password field should be marked with a red outline.
    - Copy-pasting the password
      When the user copies and pastes the password from the 'Password' field into the 'Confirm Password' field.
      Expected Result: The 'Passwords do not match' error must be displayed along with the red outline for that field.
    - Check within different browsers
      The sign-up form must be checked within different browsers as part of cross-browser testing.
    - Check within different devices
      The responsiveness of the form must be looked into, by checking within different devices.
    - Enter multiple emails in the same field
      When multiple email ids are entered within the same field the email field should be shown with a red outline

2. User Sign-in

    - Valid Sign-in
        - When the user enters a valid email ID and it's corresponding password, the user must be redirected to the landing page of the application.
    - Login with incorrect email
        - When incorrect email ID is entered along with a valid password the email ID field must be highlighted with a red outline and the 'SIGN IN' button must be greyed out.
          eg: paul.example.com, @example.com, abc@.com, paul@example,!paul@example.com
    - Login with incorrect password
        - When incorrect password (password that doesn't meet the criteria) is entered along with a valid email ID the password field must be highlighted with a red outline and the 'SIGN IN' button must be greyed out.
          eg: 123, 12345678, 1234567!, 12345ab!, 12345abbbbbb!
    - Sign-in with an unregistered email
        - When the user tries to sign-in with an unregistered email, the following error message must be shown: 'User not found'.
    - Sign in with incorrect password
        - When the user enters a registered email ID along with an incorrect password, an error message must be displayed.
    - Email field contains whitespace
        - If there are white spaces in the email field the 'SIGN IN' button must be greyed out and the email field must have a red outline, if a valid password is given.
    - Refreshing the page after login
        - If the page is refreshed after the user logs in to the application, the user must not be asked to log in again or the user must not be signed out.
    - Opening the sign in URL for an already signed in user
        - When a signed in user navigates to the login page URL, the user must not be asked to enter their credentials again.
    - Parallel sessions
        - Check whether the user is able to login to different browsers simultaneously, see whether they have to terminate the previous session to initiate a new one.
    - Entering multiple emails in the same email field
        - When we enter multiple emails in the same email field, like abc123@gmail.comaxyz@gmail.com, an error must be displayed.
    - Rate limiting
        - There must be provisions setup in place to prevent brute force login attempts.

3. Onboard OCN node

    - Provide node details section

        - Node format validation
            - See whether the 'Node ID' input field follows the proper format of 'NodeID-{number}', where {number} is a natural number, or else the field must be highlighted in red.
        - IP address value validation
            - The IP address values must be of the form x.x.x.x where 0 <= x <= 255, if not the field must be highlighted in red.
        - Duplicate Node address and IP addresses
            - If the user enters the same values for the node ID and network, an error message must be displayed since the same entry has already been added to the table.
        - Node type dropdown
            - When the user selects different node types from 'Validator' or 'RPC' the same changes must be verified in the preview table.
        - Entries listed within the preview table section
            - All the entries that were created by user after clicking on the '+ADD NODE' button must be present in the preview table, and there values must be verified with the input values that were given to create those entries, look for any rounding of values.
        - Validate the select all checkbox and individual checkboxes in the preview table
            - Verify the working of the select all button along with pagination, and also with individual checkbox toggles.
        - Removing the selected nodes button
            - When a user clicks on the 'REMOVE SELECTED NODES' button, the rows that were selected prior to clicking on the button must be removed, and also it must be verified that the non-selected values are not affected.
        - Entering multiple nodes and addresses in the same field
            - When a user enters multiple nodes like 'NodeID-1 NodeID-2' in the same Node ID field the entry must be marked as invalid, similar case for Public IP field.
        - Sorting within the preview table
            - When a user sorts the columns of the table either in ascending ot descending order the table must be sorted accordingly.
        - Preview filter option
            - The user checks out the filter option within the preview table, using different different columns, operators and value combinations.
        - Hide column/manage column
            - When the user uses these options the column that must be hidden should be removed from the preview table after using the 'Hide column' button, and as for the manage

    - Provide Wallet details section

        - Entering valid 40 digit hexadecimal numbers
            - When the user enters valid 40 digit hexadecimal number of the format '0x{number}', the field must not be highlighted with a red outline
        - Skipping the prefix
            - If the user skips the prefix '0x' an error message must be displayed for the wallet details field.
        - Validate the preview table entries
            - The entries in the preview table must be validated, with the given input and it corresponding output
        - Validate the wallet permission
            - If the user were to give the wallet permissions of their choice the same must be reflected in the preview table.
        - Duplicate wallet details
            - When a user tries to use the same/already used wallet details a second time error message must be displayed.
        - 'Remove selected wallets' button
            - When the user uses the above button with the select all option or individually selected entries those entries must be deleted from the table.
        - Validate the back and next buttons
            - When a user clicks on the 'BACK' and 'NEXT' the sections must change accordingly.
        - Validate the select all checkbox and individual checkboxes in the preview table
            - Verify the working of the select all button along with pagination, and also with individual checkbox toggles.
        - Sorting within the preview table
            - When a user sorts the columns of the table either in ascending ot descending order the table must be sorted accordingly.
        - Preview filter option
            - The user checks out the filter option within the preview table, using different different columns, operators and value combinations.
        - Hide column/manage column
            - When the user uses these options the column that must be hidden should be removed from the preview table after using the 'Hide column' button, and as for the manage

    - Review and Submit

        - Verify the 'Preview node details' and 'Preview wallet details' tables
            - The entries within both these tables must be cross verified with the entries that were shown in the previous sections.
        - Validate the back and next buttons
            - When a user clicks on the 'BACK' button the sections must change accordingly.
        - Sorting within the preview table
            - When a user sorts the columns of the table either in ascending ot descending order the table must be sorted accordingly.
        - Preview filter option
            - The user checks out the filter option within the preview table, using different different columns, operators and value combinations.
        - Hide column/manage column
            - When the user uses these options the column that must be hidden should be removed from the preview table after using the 'Hide column' button, and as for the manage
        - When the user clicks on the submit button
            - In such a scenario the entries must be submitted and a success message must be displayed for a successful request.
        - Authentication request
            - Authentication can be required for submitting the response

4. Launch OCN Child Network

    - Provide network details
        - User enters valid network name
            - When the user enters valid network names, like 'polygon', 'arbitrum', 'mainnet', 'holesky' etc. the field must not be highlighted in red.
        - User enters invalid network
            - When the user enters invalid network names, the field must be highlighted in red outline.
        - Validate the wallet address format
            - The wallet address format, should be of the form '0x{number}'.
        - Check the 'Next' button
            - When a user clicks on the 'Next' button, they should move to the next section.
    - Provide node details
        - Same test cases as the one mentioned in 'Onboard OCN node > Provide node details' section.
    - Review and submit
        - Verify the table after editing the value
            - Both the table must be validated after editing their values and prior to that too.
        - Verify the back button
            - When the user clicks on the back button he must be moved to the previous section.
        - Review the table
            - The values within the table must be verified according to the values mentioned within the table in the previous section.
        - Sorting within the preview table
            - When a user sorts the columns of the table either in ascending ot descending order the table must be sorted accordingly.
        - Preview filter option
            - The user checks out the filter option within the preview table, using different different columns, operators and value combinations.
        - Hide column/manage column
            - When the user uses these options the column that must be hidden should be removed from the preview table after using the 'Hide column' button, and as for the manage
        - When the user clicks on the submit button
            - In such a scenario the entries must be submitted and a success message must be displayed for a successful request.
        - Authentication request
            - Authentication can be required for submitting the response

5. Sign out

-   Back button after sign out
    -   When a user clicks on the browser back button after sign out the user must not enter the signed in session again.
-   Sign out from every page
    -   The sign out must be verified from every page, make sure the user is taken back to homepage in every scenario.
-   Sign out from multiple tabs
    -   When the user signs out from one tab within the same browser, they must be signed out from all the tabs within the same user.
-   Multi login
    -   If the user logs in to the same user from a different browser the, previous session must be revoked.
-   Time out
    -   If the user has been idle for a long time, the session must be timed out after some time and they must be logged out.
