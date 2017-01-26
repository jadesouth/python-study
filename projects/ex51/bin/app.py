import web

urls = ('/hello', 'Index')

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index:
    def GET(self):
        return render.hello_form()
        form = web.input(name = 'Nobody', greet = None)

        if form.greet:
            greeting = "Hello, %s, %s" % (form.name, form.greet)
            return render.index(greeting = greeting) 
        else:
            return "Error: greet is required."

    def POST(self):
        form = web.input(name = "Nobody", greet = "Hello")
        greeting = "Hello, %s, %s" % (form.name, form.greet)
        return render.index(greeting = greeting) 


if __name__ == '__main__':
    app.run()
