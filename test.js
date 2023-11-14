const express = require("express")
const fileSystem = require("fs")
const bodyParser = require("body-parser");
const readline = require('readline');

const app = express();
app.use(bodyParser.urlencoded({extended: true}));
app.set('view engine', 'ejs');

app.get("/", function(request, response) {
    wrong_password = false;
    response.render('page', {wrong_password: wrong_password})


    const fileStream = fileSystem.createReadStream('out.txt');
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    rl.on('line', function (line) {
        console.log('Line from file:', line);
    });

})

app.listen(3000, function() {
    console.log("Server started on port 3000");
});