//by Sharapov
var rand = function (min, max) {
		k = Math.floor(Math.random() * (max - min) + min); 
		return (Math.round( k / s) * s);}

var newA = function () {
		app = [rand(0, innerWidth),rand(0, innerHeight)];},

	newB = function () {
		snakeBody = [{x: 0,y: 0}];}

var canvas = document.getElementById('game'),
	ctx = canvas.getContext('2d'),
	snakeBody = null,
	direc = 1,					// direction
	app = null,					// apple
	s = 35; newB(); newA();		// snake

canvas.width = innerWidth;
canvas.height = innerHeight;

setInterval (function() {
	if (app[0] + s >= canvas.width || app[1] + s >= canvas.height) newA();
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	ctx.fillStyle = "red";
	ctx.fillRect (... app, s, s);
	ctx.fillStyle = "#4ADD4A";

	snakeBody.forEach (function (el, i) {
		if (el.x == snakeBody[snakeBody.length - 1].x && 
			el.y == snakeBody[snakeBody.length - 1].y && 
			i < snakeBody.length - 1) snakeBody.splice(0,snakeBody.length-1), 
			snakeBody = [{x:0,y:0}], direc = 1;
		});

	var m = snakeBody[0], f = {x: m.x,y: m.y}, l = snakeBody[snakeBody.length - 1];
		if (direc == 1) f.x = l.x + s, f.y = Math.round(l.y / s) * s;
		if (direc == 2) f.y = l.y + s, f.x = Math.round(l.x / s) * s;
		if (direc == 3) f.x = l.x - s, f.y = Math.round(l.y / s) * s;
		if (direc == 4) f.y = l.y - s, f.x = Math.round(l.x / s) * s;

	snakeBody.push(f);
	snakeBody.splice(0,1);

	snakeBody.forEach (function (pob, i) {
		if (direc == 1) if (pob.x > Math.round(canvas.width/s)*s)  pob.x=0;
		if (direc == 2) if (pob.y > Math.round(canvas.height/s)*s) pob.y=0;
		if (direc == 3) if (pob.x < 0) pob.x = Math.round(canvas.width/s)*s;
		if (direc == 4) if (pob.y < 0) pob.y = Math.round(canvas.height/s)*s;

		if (pob.x == app[0] && pob.y == app[1]) newA(), snakeBody.unshift({x: f.x - s, y:l.y})
		ctx.fillRect(pob.x, pob.y, s, s);
		});
	}, 1000/20);

onkeydown = function (e) {
	var key = e.keyCode;
	if ([38,39,40,37].indexOf(key) >= 0)
		e.preventDefault();
	if (key==39 && direc != 3) direc = 1;
	if (key==40 && direc != 4) direc = 2;
	if (key==37 && direc != 1) direc = 3;
	if (key==38 && direc != 2) direc = 4;
};