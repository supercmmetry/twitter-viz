from typing import List
import twint


class UserModel:
    @staticmethod
    def __twint_to_pandas_user_df():
        if twint.run.output.panda.User_df is None:
            return None
        return twint.run.output.panda.User_df[twint.run.output.panda.User_df.columns]

    @staticmethod
    def __twint_to_pandas_follow_df():
        if twint.run.output.panda.Follow_df is None:
            return None
        return twint.run.output.panda.Follow_df[twint.run.output.panda.Follow_df.columns]

    def __init__(self):
        self.user_name: str = ''
        self.name: str = ''
        self.description: str = ''
        self.followers: int = 0
        self.following: int = 0
        self.likes: int = 0
        self.url: str = ''
        self.profile_image_url: str = ''
        self.followers_list: List[UserModel] = []
        self.following_list: List[UserModel] = []

    def __eq__(self, other):
        return self.user_name == other.user_name

    def __hash__(self):
        return hash(self.user_name)

    @staticmethod
    def from_tweepy_object(obj):
        user = UserModel()
        user.user_name = obj.screen_name
        user.name = obj.name
        user.followers = obj.followers_count
        user.following = obj.friends_count
        user.likes = obj.favourites_count
        user.url = obj.url
        user.description = obj.description
        user.profile_image_url = obj.profile_image_url_https
        user.followers_list = []
        user.following_list = []

        return user

    @staticmethod
    def __from_df_row(row):
        user = UserModel()
        user.user_name = row['username']
        user.name = row['name']
        user.followers = row['followers']
        user.following = row['following']
        user.likes = row['likes']
        user.url = row['url']
        user.profile_image_url = row['avatar']

        return user

    @staticmethod
    def from_df():
        df = UserModel.__twint_to_pandas_user_df()
        for _, row in df.iterrows():
            return UserModel.__from_df_row(row)
        return UserModel()

    def load_followers(self):
        config = twint.Config()
        config.Username = self.user_name
        config.Pandas = True
        config.Hide_output = True

        twint.run.Followers(config)

        df = self.__twint_to_pandas_follow_df()

        if df is None:
            return

        self.followers_list.clear()

        for _, row in df.iterrows():
            self.followers_list.append(self.__from_df_row(row))

    def load_following(self):
        config = twint.Config()
        config.Username = self.user_name
        config.Pandas = True
        config.Hide_output = True

        self.following_list.clear()

        twint.run.Following(config)
        df = self.__twint_to_pandas_follow_df()

        if df is None:
            return

        for _, row in df.iterrows():
            self.following_list.append(self.__from_df_row(row))