import subprocess


def extract_wifi_passwords():
    profiles_data = subprocess.check_output("netsh wlan show profiles").decode("UTF-8").split("\n")
    # print(profiles_data)
    # for item in profiles_data:
    #     print(item)
    profiles = [i.split(":")[1].strip() for i in profiles_data if "All User profile" in i]
    # print(profiles)
    for profile in profiles:
        profile_info = subprocess.check_output,("netsh wlan show profile", profile, "key=clear").decode("UTF-8").split("\n")
        # print(profile_info)
        try:
            password = [i.split(":")[1].sprip() for i in profile_info if "Key Content" in i]
        except IndexError:
            password = None
        # print("Profile: ", profile,"\n","Password","\n",{"# * 20"},)

        with open(file="wifi_passwords.txt",mode="a", encoding="UTF-8") as file:
            file.write("Profile: ",profile,"\n","Password","\n",{"# * 20"},)


extract_wifi_passwords()