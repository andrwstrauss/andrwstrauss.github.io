import os
html_template = """
<html>
<head>
%(scripts)s
</head>
<body>
%(body)s
</body>
"""
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f
scripts = ""
body = ""
directory = '/Users/astrauss/Downloads/website%s'
site_name = 'AndrewJStrauss'
#---Import Javascript
sub_directory = '/js'
for file in listdir_nohidden(directory%(sub_directory)):
	script_import_temp = """<script type="text/javascript" src="%(sub_directory)s/%(file)s"></script>\n""" %vars()
	scripts +=script_import_temp
#---Import CSS
sub_directory = '/css'
for file in listdir_nohidden(directory%(sub_directory)):
	script_import_temp = """<link rel="stylesheet" type="text/css" href="%(sub_directory)s/%(file)s"></script>\n""" %vars()
	scripts +=script_import_temp
print(scripts)


article_template ="""
<div class="col-sm-6 col-md-4">
    <div class="thumbnail">
      <img src="%(img)s" alt="...">
      <div class="caption">
        <h3>%(article_title)s</h3>
      </div>
    </div>
  </div>   
"""
# Create Articles List
sub_directory = '/recipes'
count = 0
articles = ""
for article_title in listdir_nohidden(directory%(sub_directory)):
	if(count==0):
		articles+="""<div class="row">"""
	img = '%(sub_directory)s/%(article_title)s/thumbnail.jpg' %vars()
	article_row = article_template % vars()
	articles+=article_row
	count+=1
	if(count==3):
		articles+="""</div>"""
		count=0
if(count>=1):
	articles+="""</div>"""
	count=0		

body_template = """
<div class="container">
      <div class="header clearfix">
        <nav>
          <ul class="nav nav-pills pull-right">
            <li role="presentation" class="active"><a href="/">Home</a></li>
            <li role="presentation"><a href="/about">About</a></li>
            <li role="presentation"><a href="/contact">Contact</a></li>
          </ul>
        </nav>
        <h3 class="text-muted">Andrew J Strauss</h3>
      </div>

      <div class="jumbotron">
        <h1>Jumbotron heading</h1>
        <p class="lead">Cras justo odio, dapibus ac facilisis in, egestas eget quam. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
        <p><a class="btn btn-lg btn-success" href="#" role="button">Sign up today</a></p>
      </div>
      %(articles)s
</div>
<footer class="footer">
<p>&copy; 2016 %(site_name)s</p>
</footer>
"""
body = body_template %vars()
html = html_template % vars()
print(html)
f = open('index.html', 'w')
f.write(html)  # python will convert \n to os.linesep
f.close()