const express = require("express")
const fileSystem = require("fs")
const bodyParser = require("body-parser");
const readline = require('readline');

const app = express();
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(__dirname + '/public'));
app.set('view engine', 'ejs');

app.get("/", function(request, response) {
    wrong_password = false;
    response.render('page', {wrong_password: wrong_password})
})


app.post("/", function(req, res) {
    entered_day = req.body.her_birthday;
    wrong_password = false;
    if(entered_day != "08-24-2000") {
        wrong_password = true;
        res.render("page", {wrong_password: wrong_password});
    } else {
        res.redirect("/ascii")
    }
})

app.get("/ascii", function(request, response) {
    let tempArray = []
    fileSystem.readdirSync('./output').forEach(file => {
        let pic_read = {
            image: fileSystem.readFileSync('./output/' + file).toString().split("\n"),
            name: file
        };
        tempArray.push(pic_read);
    });

    response.render("ascii", {tempArray: tempArray});
})

app.get("/ascii/view/:id", function(req, res) {
    image = fileSystem.readFileSync('./output/' + req.params.id).toString().split("\n");
    res.render("asciiViewer", {image: image});
})

app.post("/ascii/view/:id", function(req, res) {
    image = fileSystem.readFileSync('./output/' + req.params.id).toString().split("\n");
    res.render("asciiViewer", {image: image});
})

let port = process.env.PORT;
if (port == null || port == "") {
  port = 8000;
}
app.listen(port);
