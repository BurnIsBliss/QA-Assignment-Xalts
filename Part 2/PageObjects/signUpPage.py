from selenium.webdriver.common.by import By

class SignUpPage:
    
    emailField = (By.XPATH, '//label[contains(text(), "E-Mail")]/ancestor::div/div/input')
    passwordField = (By.XPATH, '//label[text()= "Password"]/ancestor::div/div/input')
    confirmPasswordField = (By.XPATH, '//label[contains(text(), "Confirm Password")]/ancestor::div/div/input')
    signUpButton = (By.XPATH, '//button[text()="Sign Up"]')
    signInButton = (By.XPATH, '//button[text()="Already have an account? Click here to sign in."]')
    signOutButton = (By.XPATH, '//button[text()="Sign Out"]')

    def __init__(self, driver):
        self.driver = driver

    # Function to populate the email field
    def populateEmailField(self, value):
        self.driver.find_element(*SignUpPage.emailField).clear()
        self.driver.find_element(*SignUpPage.emailField).send_keys(value)
    
    # Function to populate the password field
    def populatePasswordField(self, value):
        self.driver.find_element(*SignUpPage.passwordField).clear()
        self.driver.find_element(*SignUpPage.passwordField).send_keys(value)
    
    # Function to populate the confirm password field
    def populateConfirmPasswordField(self, value):
        self.driver.find_element(*SignUpPage.confirmPasswordField).clear()
        self.driver.find_element(*SignUpPage.confirmPasswordField).send_keys(value)

    # Function to check whether the button is clickable or not
    def clickSignUpButton(self):
        return self.driver.find_element(*SignUpPage.signUpButton).click()

    # Function to click the sign in page button
    def navigateToSignInPage(self):
        self.driver.find_element(*SignUpPage.signInButton).click()

    def checkForSignOutButton(self):
        return self.driver.find_elements(*SignUpPage.signOutButton)
    