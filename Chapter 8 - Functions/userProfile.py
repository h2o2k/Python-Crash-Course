def buildProfile(first, last, **userInfo):
    profile = {}
    profile['firstName'] = first
    profile['lastName'] = last
    for key, value in userInfo.items():
        profile[key] = value
    return profile

userProfile = buildProfile('albert', 'einstein',
                           location = 'princeton',
                           field='physics')
print(userProfile)
