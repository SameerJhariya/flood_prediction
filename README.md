<!DOCTYPE html>
<html>
<head>
	<title> Flood Prediction model by team phoenix</title>
</head>
<body>

	<h1 align="center"><u>  Flood Prediction Model</u></h1>
	<h3 align="center"> By Team Phoenix </h3>

	<p>It's a web application for prediction flood in a particular area and also alert the people, and give them precaution on how to proceed on daily basis. Basically for our model, We will divide the model city into  different grids,and categorize them on different parameters (describing below) into Red ,Blue & Green . <span style="color: red">Red</span> indicates that region is flood prone,<span style="color: blue">Blue</span>  indicates the region is normal(i.e. for normal rainfall and other conditions,that region will remain safe ) And atlast, <span style="color: green">Green</span>  indicates that region is adaptable for flood condition,or that region don't use to have high rainfall. </p>
	<p> Now the parameters comes into the picture, so the parameters we are including are sewage, development of the city, it's greenery , the area of pasture qnd how much it's close to a river or a dam. </p>
	<ul>
		<li> For the annual and monthly rainfall for the regions , we will take data from some weather forecasting websites.  </li>
		<li> Then we will check that wether the area is near to a river or a dam. then we'll take data of those rivers ,and calculate the capacity of precipitation that will not be a issue. </li>
		<li> For the sewers, we have a different plan. We had assume that on their every main sewers of the city have height sensors attached to it . They regularly used to provide height of the waterflow in the sewers.Assuming that tunnel is of height h, and mean height of water flow through it is 0.4 h and water level is suddenly increasing. We check for the other parameters,and in which region does that region fall i.e. Red,Blue or Green. And acc. to the value of parameters declare that condition of flood are arising. </li>
	</ul>



	<p> As the chances of flood are increasing , We'll notify them about the discreancies they are going to face. The measures they should take.  We'll tell them about the near regions which are green and are safe during flood</p>

	<br>
</body>
</html>
