import pytest
from Utilities.BaseClass import BaseClass
from PageObjects.signUpPage import SignUpPage
from TestData.SignUpPageTestData import TestDataSignUp

@pytest.mark.usefixtures('SetUp')
class TestSignUp(BaseClass):

    # Tests regarding signing up with valid email ID
    @pytest.mark.parametrize('validEmail', TestDataSignUp.validEmailData)
    def test_emailFieldValid(self, validEmail):
        log = self.getLogger()
        signUpPageObj = SignUpPage(self.driver)
        signUpPageObj.populateEmailField(validEmail)
        log.info('Test run for the value: ' + validEmail)
        signUpPageObj.populatePasswordField('XYZword1!')
        signUpPageObj.populateConfirmPasswordField('XYZword1!')
        buttonState = signUpPageObj.checkSignUpButton()
        assert buttonState == 'Enabled', 'The provided email address has been marked as invalid'

    # Tests relating to user sign up with valid passwords that satisfies the given criteria
    @pytest.mark.parametrize('validPassword', TestDataSignUp.validPasswords)
    def test_PasswordField(self, validPassword):
        log = self.getLogger()
        signUpPageObj = SignUpPage(self.driver)
        signUpPageObj.populateEmailField('abcd@gmail.com')
        signUpPageObj.populatePasswordField(validPassword)
        signUpPageObj.populateConfirmPasswordField(validPassword)
        log.info('Test run for the value: ' + validPassword)
        errorMessageDisplayed = signUpPageObj.isPasswordErrorMessageDisplayed()
        assert not errorMessageDisplayed, 'The provided password has been marked as invalid'

    # Tests associated with invalid email id within the Sign Up page
    @pytest.mark.parametrize('invalidEmail', TestDataSignUp.invalidEmails)
    def test_emailFieldInValid(self, invalidEmail):
        log = self.getLogger()
        signUpPageObj = SignUpPage(self.driver)
        signUpPageObj.populateEmailField(invalidEmail)
        log.info('Test run for the value: ' + invalidEmail)
        signUpPageObj.populatePasswordField('XYZword1!')
        signUpPageObj.populateConfirmPasswordField('XYZword1!')
        buttonState = signUpPageObj.checkSignUpButton()
        assert buttonState == 'Disabled', 'The provided email address is a valid one'
    
    # Tests associated with invalid Passwords in the sign Up page
    @pytest.mark.parametrize('invalidPassword', TestDataSignUp.invalidPasswords)
    def test_invalidPasswordField(self, invalidPassword):
        log = self.getLogger()
        signUpPageObj = SignUpPage(self.driver)
        signUpPageObj.populateEmailField('abcd@gmail.com')
        signUpPageObj.populatePasswordField(invalidPassword)
        signUpPageObj.populateConfirmPasswordField(invalidPassword)
        log.info('Test run for the value: ' + invalidPassword)
        errorMessageDisplayed = signUpPageObj.isPasswordErrorMessageDisplayed()
        assert errorMessageDisplayed, 'The provided password is a VALID one'

    # Tests associated with confirm password field
    @pytest.mark.parametrize('validPassword', TestDataSignUp.confirmPassword)
    @pytest.mark.parametrize('confirmPassword', TestDataSignUp.confirmPassword)
    def test_ConfirmPasswordField(self, validPassword, confirmPassword):
        log = self.getLogger()
        signUpPageObj = SignUpPage(self.driver)
        signUpPageObj.populateEmailField('abcd@gmail.com')
        signUpPageObj.populatePasswordField(validPassword)
        signUpPageObj.populateConfirmPasswordField(confirmPassword)
        log.info('Test run for the value: ' + validPassword + '\t' + confirmPassword)
        errorMessage = signUpPageObj.isConfirmPasswordErrorDisplayed()
        assert errorMessage, 'The "Confirm Password" and "Password" fields are having the same values.'

    

    
