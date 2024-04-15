class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

class Forum:
    def __init__(self):
        self.posts = []

    def create_post(self, author, content):
        post = Post(author, content)
        self.posts.append(post)

    def get_all_posts(self):
        return self.posts

class User:
    def __init__(self, username):
        self.username = username

    def make_post(self, forum, content):
        forum.create_post(self, content)

    def make_comment(self, post, comment):
        post.add_comment(comment)

# Contoh penggunaan:
if __name__ == "__main__":
    # Membuat forum
    forum = Forum()

    # Membuat pengguna
    user1 = User("user1")
    user2 = User("user2")

    # Pengguna membuat posting
    user1.make_post(forum, "Ini adalah posting pertama.")
    user2.make_post(forum, "Ini adalah posting kedua.")

    # Mendapatkan semua posting di forum
    all_posts = forum.get_all_posts()

    # Menambahkan komentar ke posting pertama
    user2.make_comment(all_posts[0], "Komentar pertama dari user2")
    user1.make_comment(all_posts[0], "Komentar kedua dari user1")

    # Menampilkan semua posting dan komentar
    for post in all_posts:
        print("Posting oleh", post.author.username, ":", post.content)
        print("Komentar:")
        for comment in post.comments:
            print("- ", comment)
        print()
