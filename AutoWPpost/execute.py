from main import post,scrapplaylist,scrapprofile,deletevariables
ExamplePlaylist = 'https://www.youtube.com/playlist?list='
ExampleProfile = 'https://www.youtube.com/user/username/videos'
scrapplaylist(ExamplePlaylist)
post(kategoria='CATEGORY')
deletevariables()
scrapprofile(ExampleProfile)
post(kategoria='CATEGORY')
