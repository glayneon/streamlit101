import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Open YAML file

with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create authenticator object
authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["pre-authorized"],
    auto_hash=False,
)

# Render the login widget
name, authentication_status, username = authenticator.login(
    "sidebar", 5, 5, captcha=False, key="login1"
)

# hasehd_pwd = stauth.Hasher([]).generate()
# st.write(hasehd_pwd)

# Authenticate users
if st.session_state["authentication_status"]:
    authenticator.logout("Logout", "sidebar", key="unique_key")
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title("Some content")
elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")

# # Password reset widget
# if authentication_status:
#     try:
#         if authenticator.reset_password("sidebar", username, "Reset password"):
#             with open("config.yaml", "w") as file:
#                 yaml.dump(config, file, default_flow_style=False)
#             st.success("Password modified successfully")
#     except Exception as e:
#         st.error(e)

# # Register new user
# try:
#     if authenticator.register_user("sidebar", pre_authorization=False):
#         with open("config.yaml", "w") as file:
#             yaml.dump(config, file, default_flow_style=False)
#         st.success("User registered successfully")
# except Exception as e:
#     st.error(e)

# # Forgot password widget
# try:
#     (
#         username_of_forgotten_password,
#         email_of_forgotten_password,
#         new_random_password,
#     ) = authenticator.forgot_password(
#         "sidebar",
#     )
#     if username_of_forgotten_password:
#         st.success("New password sent securely")
#         # Random password to be transferred to user securely
#     else:
#         st.error("Username not found")
# except Exception as e:
#     st.error(e)

# # Forgot username
# try:
#     username_of_forgotten_username, email_of_forgotten_username = (
#         authenticator.forgot_username(
#             "sidebar",
#         )
#     )
#     if username_of_forgotten_username:
#         st.success("Username sent securely")
#         # Username to be transferred to user securely
#     else:
#         st.error("Email not found")
# except Exception as e:
#     st.error(e)

# # Update user details
# if authentication_status:
#     try:
#         if authenticator.update_user_details(
#             username, "sidebar", "Update user details"
#         ):
#             with open("config.yaml", "w") as file:
#                 yaml.dump(config, file, default_flow_style=False)
#             st.success("Entries updated successfully")
#     except Exception as e:
#         st.error(e)


# st.write(st.session_state)
# # Hash passwords and store them in the YAML file. Only do this once
# # hasehd_pwd = stauth.Hasher(['123', '12345']).generate()

# # st.write(hasehd_pwd)
