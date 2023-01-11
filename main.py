import json

def main():
    followers_list = []
    following_list = []

    with open("data/followers.json", "r") as f:
        followers = json.load(f)

    with open("data/following.json", "r") as f2:
        following = json.load(f2)

    for each in followers["relationships_followers"]:
        followers_list.append(each["string_list_data"][0]["value"])

    for each in following["relationships_following"]:
        following_list.append(each["string_list_data"][0]["value"])

    print(f"Users who don't follow me back: {check_followback(followers_list, following_list)}")
    print(f"Users I didn't follow back: {check_follow(followers_list, following_list)}")

def check_followback(followers_list, following_list):
    no_followback = []

    for each in following_list:
        if each not in followers_list:
            no_followback.append(each)
    
    return no_followback

def check_follow(followers_list, following_list):
    didnt_follow = []

    for each in followers_list:
        if each not in following_list:
            didnt_follow.append(each)

    return didnt_follow

main()