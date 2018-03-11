import Feature from './feature'

console.log(Feature);
var opts = {
	"title": "Multiple Domains",
	"description": "User should be able to select and add multiple domains to there cart.",
	"client_id": 1,
	"priority_id": 3,
	"target_date": "4/27/2018",
	"product_area_id": 2
};
var ft = new Feature(opts);
console.log(ft.speak());
