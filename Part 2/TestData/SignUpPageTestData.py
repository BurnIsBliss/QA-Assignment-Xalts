class TestDataSignUp:
    validEmailData = ['user+tag@example.com', 'simple@example.com', 'john.doe@example.com', 'user123@example.co.uk', 'user-name@example.io', 'user_name@example.org', 'u@example.com']
    invalidEmails = ['paul.example.com', '@example.com', 'abc@.com', 'paul@example', '!paul@example.com']
    validPasswords = ['Sunny4#TreeFox', 'Rain8!CupMoooooo000o000oon', 'Book@9FastDog', 'Wind2$CatJet', 'Fish!7RockSky']
    invalidPasswords = ['123', '12345678', '1234567!', '12345ab!', '12345abbbbbb!', '    ', '']
    confirmPassword = ['Rain8!CupMoooooo000o000oon', 'Book@9FastDog', '123', '123 ', '1234567!', '12345ab!', '12345abbbbbb!']
    
    validUsers = [('abc123@gmail.com', 'Password1!'), ('xyz@gmail.com', 'Tryhard1!'), ('abxxyz@outlook.com', 'Password01!')]