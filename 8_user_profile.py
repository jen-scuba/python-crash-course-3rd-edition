# Using Arbitrary Keyword Arguments

# the double asterisks ** before user_info caused python to create
#  a dictionary called user_info


def build_profile(first, last, **user_info):
    """Build a dictionary contasining everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile("albert", "einstein", location="princton", field="physics")


print(user_profile)