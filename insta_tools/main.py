import click
from colorama import Fore, Style
from instagrapi import Client

from insta_tools.scripts.get_non_friends import get_non_friends

menu = """
 ______                        __                                                                  ________                   __           
/      |                      /  |                                                                /        |                 /  |          
$$$$$$/  _______    _______  _$$ |_     ______   ______    ______    ______   ______   _____  ____$$$$$$$$/______    ______  $$ |  _______ 
  $$ |  /       \  /       |/ $$   |   /      \ /      \  /      \  /      \ /      \ /     \/    \  $$ | /      \  /      \ $$ | /       |
  $$ |  $$$$$$$  |/$$$$$$$/ $$$$$$/   /$$$$$$  |$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$  |$$$$$$ $$$$  | $$ |/$$$$$$  |/$$$$$$  |$$ |/$$$$$$$/ 
  $$ |  $$ |  $$ |$$      \   $$ | __ $$ |  $$/ /    $$ |$$ |  $$ |$$ |  $$/ /    $$ |$$ | $$ | $$ | $$ |$$ |  $$ |$$ |  $$ |$$ |$$      \ 
 _$$ |_ $$ |  $$ | $$$$$$  |  $$ |/  |$$ |     /$$$$$$$ |$$ \__$$ |$$ |     /$$$$$$$ |$$ | $$ | $$ | $$ |$$ \__$$ |$$ \__$$ |$$ | $$$$$$  |
/ $$   |$$ |  $$ |/     $$/   $$  $$/ $$ |     $$    $$ |$$    $$ |$$ |     $$    $$ |$$ | $$ | $$ | $$ |$$    $$/ $$    $$/ $$ |/     $$/ 
$$$$$$/ $$/   $$/ $$$$$$$/     $$$$/  $$/       $$$$$$$/  $$$$$$$ |$$/       $$$$$$$/ $$/  $$/  $$/  $$/  $$$$$$/   $$$$$$/  $$/ $$$$$$$/  
                                                         /  \__$$ |                                                                        
                                                         $$    $$/                            by @monsignor_eduardo                                            
                                                          $$$$$$/                                                                          


"""  # noqa: E501, W291, W605


@click.group()
def main():
    print(f"{Fore.CYAN}{menu}{Style.RESET_ALL}")
    print("Starting...")
    print("Input your session id...")
    session = input("->  ")
    cl = Client()
    cl.login_by_sessionid(session)
    print(f"{Fore.GREEN}Logged{Style.RESET_ALL}")
    # Get friends
    print("Getting friends...")
    friends = get_non_friends(cl, "11770464186")

    if friends == None:
        print(f"{Fore.RED}No friends{Style.RESET_ALL}")
    else:
        print(
            f"{Fore.GREEN}Got {len(friends)} non friends saving them to file NonFriends.txt {Style.RESET_ALL}"
        )
        with open("NonFriends.txt", "w") as file:
            for friend in friends:
                file.write(f"{friend}\n")


if __name__ == "__main__":
    main()
