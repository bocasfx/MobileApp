var currentWin = Ti.UI.currentWindow;

var sendit = Ti.Network.createHTTPClient();
sendit.open('GET', 'http://10.0.1.8:8080/api/v1/records');
sendit.send();
sendit.onload = function(){
	console.log(this);
    var json = JSON.parse(this.responseText);
    
    console.log(json);
    console.log("length: " + String(json.length));
	
	var dataArray = [];
	
    var pos;
    for( pos=0; pos < 2; pos++){
    	
    	console.log(json[pos]);
		
		dataArray.push({title:'' + json[pos].name + ''});
		// set the array to the tableView
		tableview.setData(dataArray);
    };
    console.log(dataArray);

};

var tableview = Ti.UI.createTableView({
});

currentWin.add(tableview);
