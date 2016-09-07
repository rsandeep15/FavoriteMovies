import media
import fresh_tomatoes

# Creates instances of different movies to display on the website
nemo = media.Movie("Finding Nemo", "A clown fish in search for his lost son",
"https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
"https://www.youtube.com/watch?v=wZdpNglLbt8")

avatar = media.Movie("The Wolf of Wall Street",
"A man who stops at nothing to conquer the stock market",
"http://sociologylegacy.pbworks.com/f/1426548534/6738.jpg",
"https://www.youtube.com/watch?v=pabEtIERlic")

zindagi = media.Movie("Zindagi Na Milegi Dobara",
"Three freinds turning their dream vacation into a reality",
"https://upload.wikimedia.org/wikipedia/en/3/3d/Zindaginamilegidobara.jpg",
"https://www.youtube.com/watch?v=FJrpcDgC3zU")

gatsby = media.Movie("The Great Gatsby", "A man after the American Dream",
"https://upload.wikimedia.org/wikipedia/en/2/26/TheGreatGatsby2012Poster.jpg",
"https://www.youtube.com/watch?v=rARN6agiW7o")

skyfall = media.Movie("Skyfall", "Another James Bond Movie",
"https://upload.wikimedia.org/wikipedia/en/a/a7/Skyfall_poster.jpg",
"https://www.youtube.com/watch?v=24mTIE4D9JM")

jab = media.Movie("Jab We Met",
"Two people whose paths happened to cross changes everything",
"http://c.saavncdn.com/364/Jab-We-Met-2007-500x500.jpg",
"https://www.youtube.com/watch?v=i7VGyugYCIk")
movies = [nemo, avatar, zindagi, gatsby, skyfall, jab]
fresh_tomatoes.open_movies_page(movies)
