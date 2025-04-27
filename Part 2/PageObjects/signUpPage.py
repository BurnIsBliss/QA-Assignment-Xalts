from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class SignUpPage:
    
    emailField = (By.XPATH, '//label[contains(text(), "E-Mail")]/ancestor::div/div/input')
    passwordField = (By.XPATH, '//label[text()= "Password"]/ancestor::div/div/input')
    confirmPasswordField = (By.XPATH, '//label[contains(text(), "Confirm Password")]/ancestor::div/div/input')
    signUpButton = (By.XPATH, '//button[text()="Sign Up"]')
    signInButton = (By.XPATH, '//button[text()="Already have an account? Click here to sign in."]')
    signOutButton = (By.XPATH, '//button[text()="Sign Out"]')
    passwordFieldErrorMessage = (By.XPATH, "//p[contains(text(), 'Password must contain')]")
    confirmPasswordErrorMessage = (By.XPATH, '//p[text()="Passwords do not match"]')

    def __init__(self, driver):
        self.driver = driver

    # Function to populate the email field
    def populateEmailField(self, value):
        self.driver.find_element(*SignUpPage.emailField).send_keys(Keys.COMMAND, 'a')
        self.driver.find_element(*SignUpPage.emailField).send_keys(Keys.DELETE)
        self.driver.find_element(*SignUpPage.emailField).send_keys(value)
    
    # Function to populate the password field
    def populatePasswordField(self, value):
        self.driver.find_element(*SignUpPage.passwordField).send_keys(Keys.COMMAND, 'a')
        self.driver.find_element(*SignUpPage.passwordField).send_keys(Keys.DELETE)
        self.driver.find_element(*SignUpPage.passwordField).send_keys(value)
    
    # Function to populate the confirm password field
    def populateConfirmPasswordField(self, value):
        self.driver.find_element(*SignUpPage.confirmPasswordField).send_keys(Keys.COMMAND, 'a')
        self.driver.find_element(*SignUpPage.confirmPasswordField).send_keys(Keys.DELETE)
        self.driver.find_element(*SignUpPage.confirmPasswordField).send_keys(value)

    # Function to check whether the button is clickable or not
    def checkSignUpButton(self):
        try:
            WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((SignUpPage.signUpButton)))
            return 'Enabled'
        except:
            return 'Disabled'

    # Function to click the sign in page button
    def navigateToSignInPage(self):
        self.driver.find_element(*SignUpPage.signInButton).click()

    # Function to check for sign out button
    def checkForSignOutButton(self):
        return self.driver.find_elements(*SignUpPage.signOutButton)

    def isConfirmPasswordErrorDisplayed(self):
        return self.driver.find_elements(*SignUpPage.confirmPasswordErrorMessage)
    
    def isPasswordErrorMessageDisplayed(self):
        return self.driver.find_elements(*SignUpPage.passwordFieldErrorMessage)
    