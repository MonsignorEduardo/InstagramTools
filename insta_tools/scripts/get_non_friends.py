from instagrapi import Client


def get_non_friends(cl: Client, user_id: str):
    # Get all followers
    followers = cl.user_followers(user_id)
    followers_name = {follower.username for follower in followers.values()}

    # Get all following
    following = cl.user_following(user_id)
    following_name = {follower.username for follower in following.values()}

    # Get followers that Im not following
    non_following = followers_name - following_name
    # Get following that don't follow me
    not_follower = following_name - followers_name

    return non_following.union(not_follower)
