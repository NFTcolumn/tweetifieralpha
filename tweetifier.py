#Made by @NFTaanon

### How to use this
# 1. Copy your content into the content.txt file.
# 2. Update the hashtags and website in line x
# 3. Run the program
# 4. Enjoy your new Tweetified content, keep in mind twitter's 240 character Limit  ###

###Example of how this script functions:
# Before script: This is a test and I hate being tested. As a matter of fact, I deserve to have my own line. I'm tired of sharing space with you these other clwons. It's time to Pickle Rick to blow this joint. A star has gotta' shine baby!
# After script: This is a test and I hate being tested. #hashtag1 #hashtag2 #hashtag3 yourwebsite.com
# As a matter of fact, I deserve to have my own line #hashtag1 #hashtag2 #hashtag3 yourwebsite.com
# I'm tired of sharing space with you these other clowns. #hashtag1 #hashtag2 #hashtag3 yourwebsite.com
# It's time to Pickle Rick to blow this joint. #hashtag1 #hashtag2 #hashtag3 yourwebsite.com
# A star has gotta' shine baby! #hashtag1 #hashtag2 #hashtag3 yourwebsite.com

with open('content.txt','r+') as file:
    textcontent = file.read()
new = textcontent.replace('\n','')
#Replace #hashtags with your hashtags, and website with your website to add them after each tweet
#newnew = new.replace('. ','. #hashtag1 #hashtag2 #hashtag3 yourwebsite.com \n')

newnew = new.replace('. ','. #hashtag1 #hashtag2 #hashtag3 yourwebsite.com \n')

newnewnew = newnew.replace('! ','! #hashtag1 #hashtag2 #hashtag3 yourwebsite.com \n')

#Write tweetified conten to new file called tweets.txt
with open('tweets.txt', 'w') as updatedfile:
    updatedfile.write(newnewnew)
print('Your content has been tweetified')