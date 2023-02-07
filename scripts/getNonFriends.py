from instagrapi import Client


def getNonFriends(cl: Client, user_id: str):
    # Get all followers
    followers = cl.user_followers(user_id)
    followers_name = set(
        [follower.username for follower in followers.values()])

    # Get all following
    following = cl.user_following(user_id)
    following_name = set(
        [follower.username for follower in following.values()])

    # Get followers that Im not following
    nonFollowing = followers_name - following_name
    # Get following that don't follow me
    notFollower = following_name - followers_name

    return nonFollowing.union(notFollower)