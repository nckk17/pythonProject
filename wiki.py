class WikiPages:

    def GET(self):
        web.header("Content-Type", "text/html; charset=utf-8")
        t = re.compile('^[a-zA-Z_]+$')
        wikipages = os.listdir(wikidir)
        print
        "<html><head><title>wiki pages</title></head><body>"
        print
        "<h1>Wiki Pages:</h1><ul>"
        for wikipage in wikipages:
            if os.path.isfile(os.path.join(wikidir, wikipage)) and t.match(wikipage):
                print
                "<li><a href=" % (path)
                s / page / % (page)
                s
                ">%(page)s</a></li>"
                % {'path': web.ctx.home + web.ctx.path[1:], 'page': wikipage}

    print
    "</ul></body></html>"


class WikiPage:

    def GET(self, name):
        page = os.path.join(wikidir, name)
        web.header("Content-Type", "text/html; charset=utf-8")
        if os.path.exists(page):
            print
            "<html><head><title>%s</title></head><body>" % name
            print
            "<h1>%s</h1>" % name
            print
            "<p>"
            print
            "[<a href=" % s
            ">Pages</a>] "
            % (web.ctx.home + "/")
        print
        "[<a href=" % s
        ">Edit</a>] "
        % (web.ctx.home + '/editor/' + name)

    print
    "</p>"
    print
    Markdown(open(page).read())
    print
    "</body></html>"

else:
web.ctx.status = '404 Not Found'
print
"<html><head><title>Does not exist: %s</title></head><body>" % name
print
"<p>Page %s does not yet exist - " % name
print
"<a href=" % s
">Create</a>" % (web.ctx.home + '/editor/' + name)


def POST(self, name):
    page = os.path.join(wikidir, name)
    if os.path.exists(page):
        newpage = page + '.' + time.strftime("%Y%m%d%H%M%S", time.gmtime())
        os.rename(page, newpage)
    f = open(page, "w")
    f.write(web.input(page='').page)
    f.close()
    web.redirect(web.ctx.home + '/page/' + name)