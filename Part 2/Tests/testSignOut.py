import pytest, time
from PageObjects.signUpPage import SignUpPage
from TestData.URLData import ValidURL

@pytest.mark.usefixtures('SignInTests')
class TestSignOut:

    # Tests to see whether the user can sign out from anywhere within the app
    @pytest.mark.parametrize('URL', ValidURL.URLlist)
    def test_SignOutURLs(self, URL):
        signUpPageObj = SignUpPage(self.driver)
        signUpPageObj.navigateToSignInPage()
        signUpPageObj.populateEmailField('abc123@gmail.com')
        signUpPageObj.populatePasswordField('Password1!')
        signUpPageObj.checkSignInButton()
        self.driver.get(URL)
        value = signUpPageObj.presenceSignInButton()
        assert value == "Sign out successful", 'Sign out was unsuccessful!'
