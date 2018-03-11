import Service from './service'
import Feature from './feature'
import FeatureViewModel from './feature-view-model'

var opts = {
	"title": "Multiple Domains",
	"description": "User should be able to select and add multiple domains to there cart.",
	"client_id": 1,
	"priority_id": 3,
	"target_date": "4/27/2018",
	"product_area_id": 2
};

// start view model
var vm = new FeatureViewModel();
ko.applyBindings(vm);

// get all feature data
Service
  .getAllFeature()
  .then((data) => data.features.forEach(
    feature => vm.addNewFeature(new Feature(feature)))
  );
