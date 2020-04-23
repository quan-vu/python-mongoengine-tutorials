from database import TextPost, LinkPost

# Create a text-based post
post1 = TextPost(title='Using MongoEngine', content='Working with MongoDB in Python.')
post1.tags = ['mongodb', 'mongoengine']

# Create a link-based post
post2 = LinkPost(title='MongoDB with Python tutorial', url='https://github.com/quan-vu/python-mongoengine-tutorials')
post2.tags = ['mongoengine', 'python']


if __name__ == '__main__':
    post1.save()
    post2.save()

