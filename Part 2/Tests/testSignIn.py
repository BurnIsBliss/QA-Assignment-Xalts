import pytest, time
from PageObjects.signUpPage import SignUpPage
from TestData.SignUpPageTestData import TestDataSignUp

@pytest.mark.usefixtures('SignInTests')
class TestSignIn:

    # Test to verify valid email and password inputs
    @pytest.mark.parametrize('email, password', TestDataSignUp.validUsers)
    def test_ValidUser(self, email, password):
        signUpPageObj = SignUpPage(self.driver)
        signUpPageObj.navigateToSignInPage()
        signUpPageObj.populateEmailField(email)
        signUpPageObj.populatePasswordField(password)
        signUpPageObj.checkSignInButton()
        signOutElement = signUpPageObj.checkForSignOutButton()
        assert signOutElement, 'The user cannot be logged in due to invalid credentials'

    # Test to check the cases of unregistered users
    def test_UnregisteredUsers(self):
        signUpPageObj = SignUpPage(self.driver)
        signUpPageObj.navigateToSignInPage()
        signUpPageObj.populateEmailField('email@123.xx')
        signUpPageObj.populatePasswordField('Password1!')
        signUpPageObj.checkSignInButton()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        assert alert.text == 'User not found', 'User exists, test failed!'
        alert.accept()

    # Test to verify the case of users who enter the right email address but incorrect password
    def test_UsersWithIncorrectPassword(self):
        signUpPageObj = SignUpPage(self.driver)
        signUpPageObj.navigateToSignInPage()
        signUpPageObj.populateEmailField('abc123@gmail.com')
        signUpPageObj.populatePasswordField('Password2!')
        signUpPageObj.checkSignInButton()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        assert alert.text == 'Incorrect E-Mail or Password', 'User exists, test failed!'
        alert.accept()

    # Same tests executed for the email and password fields within the sign-up page can be executed here as well