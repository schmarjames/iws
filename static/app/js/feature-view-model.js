class FeatureViewModel {
  constructor() {
    this.feature_collection = ko.observableArray([]);

  }

  addNewFeature(new_feature) {
    this.feature_collection.push(new_feature);
  }


}
