var http = require('http');
var path = require('path');
var PythonShell = require('python-shell');
var express = require('express'),
    app = module.exports.app = express();
const PORT = process.env.PORT || 3000;
console.log('server running on port 3000');
app.use(express.static(path.join(__dirname, 'public')));

var server = http.createServer(app);
server.listen(PORT)




app.get('/:companyid', function(req,res) {
	var options = {
	  mode: 'text',
	  args: [req.params.companyid]
	};
	/*PythonShell.run('userExtract.py', options, function (err, results) {
  		if (err) throw err;
 		// results is an array consisting of messages collected during execution
    	console.log('results: %j', results);
	});*/
	res.send('never ever '+req.params.companyid)
})
