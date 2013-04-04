/**
 * XULSchoolChrome namespace.
 */
if ("undefined" == typeof(XULSchoolChrome)) {
  var XULSchoolChrome = {};
};

/**
 * Controls the browser overlay for the Hello World extension.
 */
XULSchoolChrome.BrowserOverlay = {
  /**
   * Says 'Hello' to the user.
   */
  sayHello : function(aEvent) {
    let stringBundle = document.getElementById("xulschoolhello-string-bundle");
    let message = stringBundle.getString("xulschoolhello.greeting.label");

    window.alert(message);
  },
  
  clear : function(aEvent) {
	window.alert(window.top.getBrowser().selectedBrowser.contentWindow.location.href);
	window.alert(window.top.getBrowser().selectedBrowser.contentWindow.location.href + "?clear");
	window.alert(location);
	browserLocation = window.top.getBrowser().selectedBrowser.contentWindow.location.href;
	window.alert(browserLocation);
	
	// Appel Ajax pour clear appli
	x = new XMLHttpRequest();
	x.onreadystatechange = function() { 
		if(x.readyState == 4) { 
			if(x.status == 200) { 
				if (x.responseText == "{\"success\":true}") {
					window.alert(x.responseText); 
					window.top.getBrowser().selectedBrowser.contentWindow.location.href = browserLocation;
				}
			}
		}
	};
	x.open("GET", browserLocation + "?clear", true);
	x.send();
	
  }
  
};
